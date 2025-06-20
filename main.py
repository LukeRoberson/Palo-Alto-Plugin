"""
Module: main.py

Palo Alto Firewall plugin. Receives webhooks from Palo Alto Firewalls
    and processes them.

Usage:
    This is a Flask application that should run behind a WSGI server inside
        a Docker container.
    Build the Docker image and run it with the provided Dockerfile.

Dependencies:
    - Flask: For creating the web application.
    - Flask-Session: For session management.
"""

# Standard library imports
import os
import logging
import yaml
from flask import (
    Flask,
    jsonify,
    request,
)
from flask_session import Session

# Custom imports
from event_handler import EventHandler
from sdk import (
    Config,
    SystemLog,
    error_response,
)


CONFIG_URL = "http://core:5100/api/config"
LOG_URL = "http://logging:5100/api/log"


def logging_setup(
    config: dict,
) -> None:
    """
    Set up the root logger for the web service.

    Args:
        config (dict): The global configuration dictionary

    Returns:
        None
    """

    # Get the logging level from the configuration (eg, "INFO")
    log_level_str = config['web']['logging-level'].upper()
    log_level = getattr(logging, log_level_str, logging.INFO)

    # Set up the logging configuration
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging setup complete with level: %s", log_level)


def create_app(
    system_log: SystemLog,
    plugin_config: dict,
) -> Flask:
    """
    Create the Flask application instance and set up the configuration.
    Registers the necessary blueprints for the web service.

    Args:
        config (dict): The global configuration dictionary
        system_log (SystemLog): An instance of SystemLog for logging.
        plugin_config (dict): The plugin configuration loaded from config.yaml.

    Returns:
        Flask: The Flask application instance.
    """

    # Create the Flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('api_master_pw')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = '/app/flask_session'
    app.config['SYSTEM_LOG'] = system_log
    app.config['PLUGIN_CONFIG'] = plugin_config
    Session(app)

    return app


# Load the global configuration from the core service
global_config = {}
with Config(CONFIG_URL) as config_reader:
    global_config = config_reader.read()

# Load the plugin configuration file
with open('config.yaml', 'r') as f:
    config_data = yaml.safe_load(f)

# Set up logging
logging_setup(global_config)

# Initialize the SystemLog with default values
#   Values can be overridden when sending a log
system_log = SystemLog(
    logging_url=LOG_URL,
    source="PaloAlto-plugin",
    destination=["web"],
    group="plugin",
    category="PaloAlto",
    alert="system",
    severity="info",
    teams_chat_id=config_data.get('chats', None).get('default', None)
)

# Initialize the Flask application
app = create_app(
    system_log=system_log,
    plugin_config=config_data,
)


@app.route(
    '/api/health',
    methods=['GET']
)
def health():
    """
    Health check endpoint.
    Returns a JSON response indicating the service is running.
    """

    return jsonify({'status': 'ok'})


@app.route('/webhook', methods=['POST'])
def webhook():
    '''
    Handle incoming webhook requests from a firewall.

    Returns:
        str: A response indicating the result of the processing.
    '''

    # Parse the incoming webhook request
    body = request.get_json()
    if not body:
        logging.error("No JSON body received.")
        return error_response("No JSON body received")

    # Parse the event
    with EventHandler(config=config_data) as event_handler:
        event_handler.process_event(
            event=body,
            headers=dict(request.headers),
        )

    return "Received", 200

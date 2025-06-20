"""
Module: event_handler.py

Handle webhook events from a firewall and process them accordingly.

Classes:
    EventHandler: Class to handle webhook events from firewalls.
        It validates the webhook, extracts common and specific fields,
        and processes the event to send logs to the logging service.

Dependencies:
    requests: For making HTTP requests to the logging service and
        fetching plugin configuration.
    logging: For logging errors and debug messages.
    yaml: For loading event handling configuration from a YAML file.
    flask: For accessing the current application context.
"""


# Standard library imports
import yaml


# Get event handling configuration from the YAML file
with open("events.yaml", "r") as file:
    EVENTS = yaml.safe_load(file)


class EventHandler:
    """
    EventHandler class to handle webhook events from PA firewalls.

    Args:
        config (dict): Configuration dictionary containing necessary settings.
    """

    def __init__(
        self,
        config
    ) -> None:
        """
        Initialize the EventHandler with the provided configuration.

        Args:
            config (dict):
                Configuration dictionary containing necessary settings.

        Returns:
            None
        """

        self.config = config
        self.plugin_name = config['name']

    def __enter__(
        self
    ) -> 'EventHandler':
        """
        Enter the runtime context related to this object.

        Args:
            None

        Returns:
            EventHandler: The current instance of EventHandler.
        """

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ) -> None:
        """
        Exit the runtime context related to this object.

        Args:
            exc_type: The exception type.
            exc_value: The exception value.
            traceback: The traceback object.

        Returns:
            None
        """

        # Handle any cleanup if necessary
        if exc_type is not None:
            # Log the exception or handle it as needed
            print(f"Exception occurred: {exc_value}")

    def process_event(
        self,
        event: dict,
        headers: dict,
    ) -> None:
        """
        Basic processing of a webhook event from Cloudflare.
            Extracts fields from the event and stores them in the instance.

        Args:
            event (dict): The event data received from Cloudflare.

        Returns:
            None
        """

        print(f"Processing event: {event}")
        print(f"Headers: {headers}")

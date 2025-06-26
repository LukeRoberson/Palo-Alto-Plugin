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
import logging
from flask import current_app
from datetime import datetime


# Get event handling configuration from the YAML file
#   See docs/pa_config.md for details on the configuration format
with open("config/pa_config.yaml", "r") as file:
    CONFIG_EVENTS = yaml.safe_load(file)

with open("config/system.yaml", "r") as file:
    SYSTEM_EVENTS = yaml.safe_load(file)

with open("config/userid.yaml", "r") as file:
    USERID_EVENTS = yaml.safe_load(file)

with open("config/globalprotect.yaml", "r") as file:
    GLOBALPROTECT_EVENTS = yaml.safe_load(file)

with open("config/auth.yaml", "r") as file:
    AUTH_EVENTS = yaml.safe_load(file)

with open("config/iptag.yaml", "r") as file:
    IPTAG_EVENTS = yaml.safe_load(file)

with open("config/hip.yaml", "r") as file:
    HIP_EVENTS = yaml.safe_load(file)

with open("config/threat.yaml", "r") as file:
    THREAT_EVENTS = yaml.safe_load(file)

with open("config/url.yaml", "r") as file:
    URL_EVENTS = yaml.safe_load(file)

with open("config/data.yaml", "r") as file:
    DATA_EVENTS = yaml.safe_load(file)

with open("config/wildfire.yaml", "r") as file:
    WILDFIRE_EVENTS = yaml.safe_load(file)

with open("config/traffic.yaml", "r") as file:
    TRAFFIC_EVENTS = yaml.safe_load(file)

with open("config/tunnel.yaml", "r") as file:
    TUNNEL_EVENTS = yaml.safe_load(file)

with open("config/decryption.yaml", "r") as file:
    DECRYPTION_EVENTS = yaml.safe_load(file)


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
        self.chat_list = config.get('chats', {})
        self.default_chat = self.chat_list.get('default', None)
        self.source = "Unknown"

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

    def _extract_fields(
        self,
        event: dict,
    ) -> None:
        """
        Extract common fields from the event data.

        Args:
            event (dict): The event data.

        Returns:
            None
        """

        # Save the event data
        self.event = event

        # Extract common fields
        self.source = event.get("alert", {}).get("source")
        self.timestamp = event.get("alert", {}).get("timestamp")
        self.event_type = event.get("details", {}).get("type")
        self.event_subtype = event.get("details", {}).get("subtype")
        self.device_name = event.get("device", {}).get("device_name")
        self.device_version = event.get("device", {}).get("sender_sw_version")
        self.device_serial = event.get("device", {}).get("serial")

        # Get config events
        if self.source == "config":
            self.config_user = event.get("config", {}).get("user")
            self.config_client = event.get("config", {}).get("client")
            self.config_host = event.get("config", {}).get("host")
            self.config_cmd = event.get("config", {}).get("cmd")
            self.config_full_path = event.get("config", {}).get("full-path")
            self.config_comment = event.get("config", {}).get("comment")
            self.config_result = event.get("config", {}).get("result")

            # Improve event_subtype for config events
            #   Can effectively ignore the built in one, as it is always "0"
            if self.config_cmd == "edit":
                self.event_subtype = "edit"
            elif self.config_cmd == "commit":
                self.event_subtype = "commit"
            elif self.config_cmd == "add":
                self.event_subtype = "add"
            elif self.config_cmd == "clone":
                self.event_subtype = "clone"
            elif self.config_cmd == "delete":
                self.event_subtype = "delete"
            elif self.config_cmd == "move":
                self.event_subtype = "move"
            elif self.config_cmd == "rename":
                self.event_subtype = "rename"
            elif self.config_cmd == "set":
                self.event_subtype = "set"

        # Get system events
        if self.source == "system":
            self.severity = event.get("alert", {}).get("severity")
            self.module = event.get("details", {}).get("module")
            self.name = event.get("details", {}).get("name")
            self.description = event.get("details", {}).get("description")
            self.object = event.get("details", {}).get("object")

    def _parse_event(
        self,
    ) -> dict:
        """
        Parse the event data to extract relevant information.

        Args:
            None

        Returns:
            dict: A dictionary containing the parsed event data.
        """

        message = ""
        handler = {}

        if self.source == "config":
            handler = CONFIG_EVENTS.get(self.event_subtype, None)

        elif self.source == "system":
            handler = SYSTEM_EVENTS.get(self.event_subtype, None)

        elif self.source == "userid":
            handler = USERID_EVENTS.get(self.event_subtype, None)

        elif self.source == "globalprotect":
            handler = GLOBALPROTECT_EVENTS.get(self.event_subtype, None)

        elif self.source == "auth":
            handler = AUTH_EVENTS.get(self.event_subtype, None)

        elif self.source == "iptag":
            handler = IPTAG_EVENTS.get(self.event_subtype, None)

        elif self.source == "hip":
            handler = HIP_EVENTS.get(self.event_subtype, None)

        elif self.source == "threat":
            handler = THREAT_EVENTS.get(self.event_subtype, None)

        elif self.source == "url":
            handler = URL_EVENTS.get(self.event_subtype, None)

        elif self.source == "data":
            handler = DATA_EVENTS.get(self.event_subtype, None)

        elif self.source == "wildfire":
            handler = WILDFIRE_EVENTS.get(self.event_subtype, None)

        elif self.source == "traffic":
            handler = TRAFFIC_EVENTS.get(self.event_subtype, None)

        elif self.source == "tunnel":
            handler = TUNNEL_EVENTS.get(self.event_subtype, None)

        elif self.source == "decryption":
            handler = DECRYPTION_EVENTS.get(self.event_subtype, None)

        # If there's no handler found for the event type
        if handler is None or handler == {}:
            logging.error(
                f"Unknown alert type for event: {self.event}. "
                "Cannot process event."
            )

            self.event_type = "Unknown"
            self.event_subtype = "Unknown"
            self.alert_type = "Unknown Event"
            self.severity = "warning"
            self.timestamp = datetime.now().isoformat()
            message = f"Unknown Palo Alto event:\n{self.event}"
            self.teams_msg = f"Unknown Palo Alto event: {self.event}"

        # If there is a handler for the event type
        else:
            try:
                # Get the formatted message
                message = handler.get(
                    "message",
                    self.event
                ).format(self=self)

                # If there is a Teams message (optional), get it too
                self.teams_msg = handler.get("teams", None)
                if self.teams_msg:
                    self.teams_msg = self.teams_msg.format(self=self)

                self.alert_type = self.name

            except Exception as e:
                logging.error(
                    f"Error formatting event message for {self.event}:"
                    f"\n{e}"
                )
                message = "No message included"
                self.teams_msg = str(self.event)
                self.severity = "warning"

        log = {
            "source": "Palo Alto",
            "log": {
                "group": self.event_type,
                "category": self.event_subtype,
                "alert": self.alert_type,
                "severity": self.severity,
                "timestamp": self.timestamp,
                "message": message,
            },
            "teams": {
                "destination": self.default_chat,
                "message": message,
            }
        }

        return log

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

        # Extract common fields from the event
        self._extract_fields(event)

        # Parse the event
        log = self._parse_event()

        # Get the actions to perform
        if self.source in self.config:
            if self.event_subtype in self.config[self.source]:
                actions = self.config[self.source][self.event_subtype]
            else:
                actions = self.config["default"]
        else:
            actions = self.config["default"]

        # Convert this to a list of actions
        action_list = []
        action_list = [
            k for k in ("web", "teams", "syslog", "sql") if actions.get(k)
        ]
        log["destination"] = action_list

        # Check if there's a Teams chat specified
        teams_chat = None
        if 'chat' in actions:
            logging.info(f"Using chat: {actions['chat']}")
            teams_chat = self.chat_list.get(
                actions['chat'], None
            )
        else:
            logging.info("Using default chat")
            teams_chat = self.default_chat
        if teams_chat is None:
            logging.error(
                "No Teams chat specified in the configuration. "
                "Using default chat."
            )
            teams_chat = self.default_chat

        # If no actions are specified, do nothing
        if not action_list:
            return

        # Log to logging service
        system_log = current_app.config['SYSTEM_LOG']
        system_log.log(
            message=log['log']['message'],
            destination=log['destination'],
            group=log['log']['group'],
            category=log['log']['category'],
            alert=log['log']['alert'],
            severity=log['log']['severity'],
            teams_msg=log['teams']['message'],
            chat_id=teams_chat,
        )

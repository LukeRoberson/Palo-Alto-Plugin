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

        self.event = {}
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

    def _config_events(
        self,
    ) -> None:
        """
        Extract config specific events.
        """

        self.config_user = self.event.get("config", {}).get("user")
        self.config_client = self.event.get("config", {}).get("client")
        self.config_host = self.event.get("config", {}).get("host")
        self.config_cmd = self.event.get("config", {}).get("cmd")
        self.config_full_path = self.event.get("config", {}).get("full-path")
        self.config_comment = self.event.get("config", {}).get("comment")
        self.config_result = self.event.get("config", {}).get("result")

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
        elif self.config_cmd == "audit-commit":
            self.event_subtype = "audit-commit"

        # Set severity based on result
        if self.config_result == "success":
            self.severity = "info"
        elif self.config_result == "failure":
            self.severity = "error"
        else:
            self.severity = "warning"

    def _system_events(
        self,
    ) -> None:
        """
        Extract system specific events.
        """

        self.severity = self.event.get("alert", {}).get("severity")
        self.module = self.event.get("details", {}).get("module")
        self.name = self.event.get("details", {}).get("name")
        self.description = self.event.get("details", {}).get("description")
        self.object = self.event.get("details", {}).get("object")

        # General events use the module name
        if self.event_subtype == "general":
            self.event_subtype = f"general_{self.module}"

    def _userid_events(
        self,
    ) -> None:
        """
        Extract User-ID specific events.
        """

        self.userid_srctype = self.event.get("source", {}).get("type")
        self.userid_srcname = self.event.get("source", {}).get("name")

        self.userid_clientip = self.event.get("client", {}).get("ip")
        self.userid_clientntlm = self.event.get("client", {}).get("ntlm")
        self.userid_clientupn = self.event.get("client", {}).get("upn")
        self.userid_clienttag = self.event.get("client", {}).get("tag")

    def _gp_events(
        self,
    ) -> None:
        """
        Extract Global Protect specific events.
        """

        self.gp_client_srcuser = (
            self.event.get("client", {}).get("srcuser")
        )
        self.gp_client_os = (
            self.event.get("client", {}).get("os")
        )
        self.gp_client_osver = (
            self.event.get("client", {}).get("os_ver")
        )
        self.gp_client_hostname = (
            self.event.get("client", {}).get("host_name")
        )
        self.gp_client_hostserial = (
            self.event.get("client", {}).get("host_serial")
        )
        self.gp_client_gpver = (
            self.event.get("client", {}).get("globalprotect_ver")
        )
        self.gp_client_privateip = (
            self.event.get("client", {}).get("private_ip")
        )
        self.gp_client_publicip = (
            self.event.get("client", {}).get("public_ip")
        )
        self.gp_client_privateipv6 = (
            self.event.get("client", {}).get("private_ipv6")
        )
        self.gp_client_publicipv6 = (
            self.event.get("client", {}).get("public_ipv6")
        )
        self.gp_client_srcregion = (
            self.event.get("client", {}).get("srcregion")
        )
        self.gp_client_loginduration = (
            self.event.get("client", {}).get("login_duration")
        )
        self.gp_client_authmethod = (
            self.event.get("client", {}).get("auth_method")
        )

        self.gp_portal = (
            self.event.get("gateway_portal", {}).get("portal")
        )
        self.gp_gateway = (
            self.event.get("gateway_portal", {}).get("gateway")
        )
        self.gp_attempted = (
            self.event.get("gateway_portal", {}).get("attempted_gateways")
        )
        self.gp_priority = (
            self.event.get("gateway_portal", {}).get("gateway_priority")
        )
        self.gp_selection = (
            self.event.get("gateway_portal", {}).get("gateway_selection")
        )
        self.gp_method = (
            self.event.get("gateway_portal", {}).get("gateway_method")
        )
        self.gp_location = (
            self.event.get("gateway_portal", {}).get("location")
        )
        self.gp_tunneltype = (
            self.event.get("gateway_portal", {}).get("tunnel_type")
        )

        self.gp_event_name = (
            self.event.get("event", {}).get("event_name")
        )
        self.gp_event_description = (
            self.event.get("event", {}).get("description")
        )
        self.gp_event_error = (
            self.event.get("event", {}).get("error")
        )
        self.gp_event_errorcode = (
            self.event.get("event", {}).get("error_code")
        )
        self.gp_event_stage = (
            self.event.get("event", {}).get("stage")
        )
        self.gp_event_status = (
            self.event.get("event", {}).get("status")
        )
        self.gp_event_quarantine = (
            self.event.get("event", {}).get("quarantine_reason")
        )

        # Subtype is not used, so remap the event ID to the subtype
        self.event_subtype = self.gp_event_name

        # Severity is not included in the event data
        if self.gp_event_status == "success":
            self.severity = "info"
        else:
            self.severity = "error"

    def _auth_events(
        self,
    ) -> None:
        """
        Extract Authentication specific events.
        """

        self.auth_client_user = self.event.get("client", {}).get("user")
        self.auth_client_normalised_user = (
            self.event.get("client", {}).get("normalize_user")
        )
        self.auth_client_ip = self.event.get("client", {}).get("ip")
        self.auth_client_region = self.event.get("client", {}).get("region")
        self.auth_client_type = self.event.get("client", {}).get("type")

        self.auth_policy = self.event.get("auth", {}).get("authpolicy")
        self.auth_proto = self.event.get("auth", {}).get("authproto")
        self.auth_factorno = self.event.get("auth", {}).get("factorno")
        self.auth_serverprofile = (
            self.event.get("auth", {}).get("serverprofile")
        )
        self.auth_vendor = self.event.get("auth", {}).get("vendor")

        self.auth_event_desc = self.event.get("event", {}).get("desc")
        self.auth_event = self.event.get("event", {}).get("event")
        self.auth_event_object = self.event.get("event", {}).get("object")

    def _iptag_events(
        self,
    ) -> None:
        """
        Extract IP-Tag specific events.
        """

        self.iptag_tag_name = self.event.get("tag", {}).get("name")
        self.iptag_tag_ip = self.event.get("tag", {}).get("ip")
        self.iptag_tag_subnet = self.event.get("tag", {}).get("subnet_range")

        self.iptag_event_id = self.event.get("event", {}).get("event_id")
        self.iptag_event_sourcetype = (
            self.event.get("event", {}).get("datasource_type")
        )
        self.iptag_event_sourcesubtype = (
            self.event.get("event", {}).get("datasource_subtype")
        )
        self.iptag_event_sourcename = (
            self.event.get("event", {}).get("datasource_name")
        )

        # Subtype is not used for IP-Tag events,
        #   so remap the event ID to the subtype
        self.event_subtype = self.iptag_event_id

    def _hip_events(
        self,
    ) -> None:
        """
        Extract HIP Check specific events.
        """

        self.hip_host_machinename = (
            self.event.get("host", {}).get("machinename")
        )
        self.hip_host_os = self.event.get("host", {}).get("os")
        self.hip_host_serial = self.event.get("host", {}).get("serialnumber")
        self.hip_host_mac = self.event.get("host", {}).get("mac")
        self.hip_host_ip = self.event.get("host", {}).get("src")
        self.hip_host_ipv6 = self.event.get("host", {}).get("srcipv6")

        self.hip_user_name = self.event.get("user", {}).get("srcuser")

        self.hip_match_name = self.event.get("match", {}).get("matchname")
        self.hip_match_type = self.event.get("match", {}).get("matchtype")

        # Subtypes not used for HIP events
        self.event_subtype = "hip_match"

    def _security_events(
        self,
    ) -> None:
        """
        Extract security specific events.
        These are Threat, URL, Data, and Wildfire events
        """

        self.security_tuple_proto = self.event.get("tuple", {}).get("proto")
        self.security_tuple_src = self.event.get("tuple", {}).get("src")
        self.security_tuple_dst = self.event.get("tuple", {}).get("dst")
        self.security_tuple_sport = self.event.get("tuple", {}).get("sport")
        self.security_tuple_dport = self.event.get("tuple", {}).get("dport")

        self.security_match_inboundif = (
            self.event.get("match", {}).get("inbound_if")
        )
        self.security_match_outboundif = (
            self.event.get("match", {}).get("outbound_if")
        )
        self.security_match_fromzone = (
            self.event.get("match", {}).get("from_zone")
        )
        self.security_match_tozone = self.event.get("match", {}).get("to_zone")
        self.security_match_direction = (
            self.event.get("match", {}).get("direction")
        )
        self.security_match_srccountry = (
            self.event.get("match", {}).get("src_country")
        )
        self.security_match_dstcountry = (
            self.event.get("match", {}).get("dst_country")
        )
        self.security_match_srcuser = (
            self.event.get("match", {}).get("src_user")
        )
        self.security_match_dstuser = (
            self.event.get("match", {}).get("dst_user")
        )
        self.security_match_natsrcip = (
            self.event.get("match", {}).get("nat_src_ip")
        )
        self.security_match_natdstip = (
            self.event.get("match", {}).get("nat_dst_ip")
        )
        self.security_match_natsport = (
            self.event.get("match", {}).get("nat_sport")
        )
        self.security_match_natdport = (
            self.event.get("match", {}).get("nat_dport")
        )

        self.security_threat_fwrule = (
            self.event.get("threat", {}).get("fw_rule")
        )
        self.security_threat_id = self.event.get("threat", {}).get("id")
        self.security_threat_name = self.event.get("threat", {}).get("name")
        self.security_threat_category = (
            self.event.get("threat", {}).get("category")
        )
        self.security_threat_severity = (
            self.event.get("threat", {}).get("severity")
        )
        self.security_threat_action = (
            self.event.get("threat", {}).get("action")
        )
        self.security_threat_reason = (
            self.event.get("threat", {}).get("reason")
        )
        self.security_threat_justification = (
            self.event.get("threat", {}).get("justification")
        )

        self.security_app = self.event.get("app", {}).get("app")
        self.security_app_type = self.event.get("app", {}).get("app_type")
        self.security_app_sanctioned = (
            self.event.get("app", {}).get("sanctioned")
        )

        self.security_tunnel = self.event.get("tunnel", {}).get("tunnel")
        self.security_tunnel_app = (
            self.event.get("tunnel", {}).get("tunneled_app")
        )

        self.security_edl_srcedl = self.event.get("edl", {}).get("src_edl")
        self.security_edl_dstedl = self.event.get("edl", {}).get("dst_edl")
        self.security_edl_domainedl = (
            self.event.get("edl", {}).get("domain_edl")
        )

        self.security_content_filetype = (
            self.event.get("content_filter", {}).get("filetype")
        )
        self.security_content_filedigest = (
            self.event.get("content_filter", {}).get("filedigest")
        )
        self.security_content_category = (
            self.event.get("content_filter", {}).get("category")
        )
        self.security_content_xff = (
            self.event.get("content_filter", {}).get("xff")
        )
        self.security_content_misc = (
            self.event.get("content_filter", {}).get("misc")
        )

        # Subtype for URL and WildFire is effectively unused
        #   so remap the category to the subtype
        if self.source == "url" or self.source == "wildfire":
            self.event_subtype = self.security_content_category

    def _traffic_events(
        self,
    ) -> None:
        """
        Extract Traffic specific events.
        """

        self.traffic_tuple_proto = self.event.get("tuple", {}).get("proto")
        self.traffic_tuple_src = self.event.get("tuple", {}).get("src")
        self.traffic_tuple_dst = self.event.get("tuple", {}).get("dst")
        self.traffic_tuple_sport = self.event.get("tuple", {}).get("sport")
        self.traffic_tuple_dport = self.event.get("tuple", {}).get("dport")

        self.traffic_match_inboundif = (
            self.event.get("match", {}).get("inbound_if")
        )
        self.traffic_match_outboundif = (
            self.event.get("match", {}).get("outbound_if")
        )
        self.traffic_match_fromzone = (
            self.event.get("match", {}).get("from_zone")
        )
        self.traffic_match_tozone = (
            self.event.get("match", {}).get("to_zone")
        )
        self.traffic_match_direction = (
            self.event.get("match", {}).get("direction")
        )
        self.traffic_match_srccountry = (
            self.event.get("match", {}).get("src_country")
        )
        self.traffic_match_dstcountry = (
            self.event.get("match", {}).get("dst_country")
        )
        self.traffic_match_srcuser = (
            self.event.get("match", {}).get("src_user")
        )
        self.traffic_match_dstuser = (
            self.event.get("match", {}).get("dst_user")
        )
        self.traffic_match_natsrcip = (
            self.event.get("match", {}).get("nat_src_ip")
        )
        self.traffic_match_natdstip = (
            self.event.get("match", {}).get("nat_dst_ip")
        )
        self.traffic_match_natsport = (
            self.event.get("match", {}).get("nat_sport")
        )
        self.traffic_match_natdport = (
            self.event.get("match", {}).get("nat_dport")
        )

        self.traffic_app = (
            self.event.get("app", {}).get("app")
        )
        self.traffic_app_category = (
            self.event.get("app", {}).get("category_of_app")
        )
        self.traffic_app_sanctioned = (
            self.event.get("app", {}).get("sanctioned_state_of_app")
        )
        self.traffic_app_technology = (
            self.event.get("app", {}).get("technology_of_app")
        )

        self.traffic_counters_bytes = (
            self.event.get("counters", {}).get("bytes")
        )
        self.traffic_counters_bytesreceived = (
            self.event.get("counters", {}).get("bytes_received")
        )
        self.traffic_counters_bytessent = (
            self.event.get("counters", {}).get("bytes_sent")
        )
        self.traffic_counters_packets = (
            self.event.get("counters", {}).get("packets")
        )
        self.traffic_counters_packetsreceived = (
            self.event.get("counters", {}).get("pkts_received")
        )
        self.traffic_counters_packetssent = (
            self.event.get("counters", {}).get("pkts_sent")
        )

        self.traffic_session_rule = (
            self.event.get("session", {}).get("rule")
        )
        self.traffic_session_action = (
            self.event.get("session", {}).get("action")
        )
        self.traffic_session_actionsource = (
            self.event.get("session", {}).get("action_source")
        )
        self.traffic_session_verdict = (
            self.event.get("session", {}).get("verdict")
        )
        self.traffic_session_start = (
            self.event.get("session", {}).get("start")
        )
        self.traffic_session_elapsed = (
            self.event.get("session", {}).get("elapsed")
        )
        self.traffic_session_endreason = (
            self.event.get("session", {}).get("session_end_reason")
        )
        self.traffic_session_xff = (
            self.event.get("session", {}).get("xff_ip")
        )
        self.traffic_session_dstedl = (
            self.event.get("session", {}).get("dst_edl")
        )
        self.traffic_session_srcedl = (
            self.event.get("session", {}).get("src_edl")
        )

        self.traffic_tunnel = (
            self.event.get("tunnel", {}).get("tunnel")
        )
        self.traffic_tunnel_parentid = (
            self.event.get("tunnel", {}).get("parent_session_id")
        )
        self.traffic_tunnel_parentstart = (
            self.event.get("tunnel", {}).get("parent_start_time")
        )
        self.traffic_tunnel_app = (
            self.event.get("tunnel", {}).get("tunneled_app")
        )

    def _tunnel_events(
        self,
    ) -> None:
        """
        Extract Tunnel specific events.
        """

        self.tunnel_tuple_proto = self.event.get("tuple", {}).get("proto")
        self.tunnel_tuple_src = self.event.get("tuple", {}).get("src")
        self.tunnel_tuple_dst = self.event.get("tuple", {}).get("dst")
        self.tunnel_tuple_sport = self.event.get("tuple", {}).get("sport")
        self.tunnel_tuple_dport = self.event.get("tuple", {}).get("dport")

        self.tunnel_match_inboundif = (
            self.event.get("match", {}).get("inbound_if")
        )
        self.tunnel_match_outboundif = (
            self.event.get("match", {}).get("outbound_if")
        )
        self.tunnel_match_fromzone = (
            self.event.get("match", {}).get("from_zone")
        )
        self.tunnel_match_tozone = (
            self.event.get("match", {}).get("to_zone")
        )

        self.tunnel_app = (
            self.event.get("app", {}).get("app")
        )
        self.tunnel_app_category = (
            self.event.get("app", {}).get("category_of_app")
        )
        self.tunnel_app_sanctioned = (
            self.event.get("app", {}).get("sanctioned_state_of_app")
        )
        self.tunnel_app_technology = (
            self.event.get("app", {}).get("technology_of_app")
        )

        self.tunnel_counters_bytes = (
            self.event.get("counters", {}).get("bytes")
        )
        self.tunnel_counters_bytesreceived = (
            self.event.get("counters", {}).get("bytes_received")
        )
        self.tunnel_counters_bytessent = (
            self.event.get("counters", {}).get("bytes_sent")
        )
        self.tunnel_counters_packets = (
            self.event.get("counters", {}).get("packets")
        )
        self.tunnel_counters_packetsreceived = (
            self.event.get("counters", {}).get("pkts_received")
        )
        self.tunnel_counters_packetssent = (
            self.event.get("counters", {}).get("pkts_sent")
        )

        self.tunnel_session_rule = (
            self.event.get("session", {}).get("rule")
        )
        self.tunnel_session_action = (
            self.event.get("session", {}).get("action")
        )
        self.tunnel_session_actionsource = (
            self.event.get("session", {}).get("action_source")
        )
        self.tunnel_session_verdict = (
            self.event.get("session", {}).get("verdict")
        )
        self.tunnel_session_start = (
            self.event.get("session", {}).get("start")
        )
        self.tunnel_session_elapsed = (
            self.event.get("session", {}).get("elapsed")
        )
        self.tunnel_session_endreason = (
            self.event.get("session", {}).get("session_end_reason")
        )

        self.tunnel = (
            self.event.get("tunnel", {}).get("tunnel")
        )
        self.tunnel_start = (
            self.event.get("tunnel", {}).get("start")
        )
        self.tunnel_parentid = (
            self.event.get("tunnel", {}).get("parent_session_id")
        )
        self.tunnel_parentstart = (
            self.event.get("tunnel", {}).get("parent_start_time")
        )
        self.tunnel_closed = (
            self.event.get("tunnel", {}).get("sessions_closed")
        )
        self.tunnel_created = (
            self.event.get("tunnel", {}).get("sessions_created")
        )

        self.tunnel_drops_maxencap = (
            self.event.get("drops", {}).get("max_encap")
        )
        self.tunnel_drops_strict = (
            self.event.get("drops", {}).get("strict_check")
        )
        self.tunnel_drops_fragment = (
            self.event.get("drops", {}).get("tunnel_fragment")
        )
        self.tunnel_drops_inspection = (
            self.event.get("drops", {}).get("tunnel_insp_rule")
        )
        self.tunnel_drops_unknownproto = (
            self.event.get("drops", {}).get("unknown_proto")
        )

    def _decryption_events(
        self,
    ) -> None:
        """
        Extract Decryption specific events.
        """

        self.decryption_tuple_proto = self.event.get("tuple", {}).get("proto")
        self.decryption_tuple_src = self.event.get("tuple", {}).get("src")
        self.decryption_tuple_dst = self.event.get("tuple", {}).get("dst")
        self.decryption_tuple_sport = self.event.get("tuple", {}).get("sport")
        self.decryption_tuple_dport = self.event.get("tuple", {}).get("dport")

        self.decryption_match_inboundif = (
            self.event.get("match", {}).get("inbound_if")
        )
        self.decryption_match_outboundif = (
            self.event.get("match", {}).get("outbound_if")
        )
        self.decryption_match_fromzone = (
            self.event.get("match", {}).get("from_zone")
        )
        self.decryption_match_tozone = (
            self.event.get("match", {}).get("to_zone")
        )

        self.decryption_app = (
            self.event.get("app", {}).get("app")
        )
        self.decryption_app_category = (
            self.event.get("app", {}).get("category_of_app")
        )
        self.decryption_app_sanctioned = (
            self.event.get("app", {}).get("sanctioned_state_of_app")
        )
        self.decryption_app_technology = (
            self.event.get("app", {}).get("technology_of_app")
        )

        self.decryption_cert_cn = (
            self.event.get("certificate", {}).get("cn")
        )
        self.decryption_cert_sni = (
            self.event.get("certificate", {}).get("sni")
        )
        self.decryption_cert_serial = (
            self.event.get("certificate", {}).get("cert_serial")
        )
        self.decryption_cert_size = (
            self.event.get("certificate", {}).get("cert_size")
        )
        self.decryption_cert_notafter = (
            self.event.get("certificate", {}).get("notafter")
        )
        self.decryption_cert_notbefore = (
            self.event.get("certificate", {}).get("notbefore")
        )
        self.decryption_cert_issuercn = (
            self.event.get("certificate", {}).get("issuer_cn")
        )
        self.decryption_cert_rootcn = (
            self.event.get("certificate", {}).get("root_cn")
        )
        self.decryption_cert_rootstatus = (
            self.event.get("certificate", {}).get("root_status")
        )
        self.decryption_cert_chainstatus = (
            self.event.get("certificate", {}).get("chain_status")
        )

        self.decryption_crypto_ec = (
            self.event.get("crypto", {}).get("ec_curve")
        )
        self.decryption_crypto_tlsauth = (
            self.event.get("crypto", {}).get("tls_auth")
        )
        self.decryption_crypto_tlsenc = (
            self.event.get("crypto", {}).get("tls_enc")
        )
        self.decryption_crypto_tlsexchange = (
            self.event.get("crypto", {}).get("tls_keyxchg")
        )
        self.decryption_crypto_tlsver = (
            self.event.get("crypto", {}).get("tls_version")
        )
        self.decryption_crypto_stagec2f = (
            self.event.get("crypto", {}).get("hs_stage_c2f")
        )
        self.decryption_crypto_stagef2s = (
            self.event.get("crypto", {}).get("hs_stage_f2s")
        )

        self.decryption_event_errindex = (
            self.event.get("event", {}).get("err_index")
        )
        self.decryption_event_error = (
            self.event.get("event", {}).get("error")
        )
        self.decryption_event_policyname = (
            self.event.get("event", {}).get("policy_name")
        )
        self.decryption_event_proxytype = (
            self.event.get("event", {}).get("proxy_type")
        )

        # subtype is not used for Decryption events,
        #   so remap the error index to the subtype
        self.event_subtype = self.decryption_event_errindex

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
            self._config_events()

        # Get system events
        elif self.source == "system":
            self._system_events()

        # Get User-ID events
        elif self.source == "userid":
            self._userid_events()

        # Get Global Protect events
        elif self.source == "globalprotect":
            self._gp_events()

        # Get Authentication events
        elif self.source == "auth":
            self._auth_events()

        # Get IP-Tag events
        elif self.source == "iptag":
            self._iptag_events()

        # Get HIP Check events
        elif self.source == "hip":
            self._hip_events()

        # Get Security events (these have the same format)
        elif (
            self.source == "threat" or
            self.source == "url" or
            self.source == "data" or
            self.source == "wildfire"
        ):
            self._security_events()

        # Get Traffic events
        elif self.source == "traffic":
            self._traffic_events()

        # Get Tunnel events
        elif self.source == "tunnel":
            self._tunnel_events()

        # Get Decryption events
        elif self.source == "decryption":
            self._decryption_events()

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
        tshoot_handler = None

        if self.source == "config":
            tshoot_handler = 'config'
            handler = CONFIG_EVENTS.get(self.event_subtype, None)

        elif self.source == "system":
            tshoot_handler = 'system'
            handler = SYSTEM_EVENTS.get(self.event_subtype, None)

        elif self.source == "userid":
            tshoot_handler = 'userid'
            handler = USERID_EVENTS.get(self.event_subtype, None)

        elif self.source == "globalprotect":
            tshoot_handler = 'globalprotect'
            handler = GLOBALPROTECT_EVENTS.get(self.event_subtype, None)

        elif self.source == "auth":
            tshoot_handler = 'auth'
            handler = AUTH_EVENTS.get(self.event_subtype, None)

        elif self.source == "iptag":
            tshoot_handler = 'iptag'
            handler = IPTAG_EVENTS.get(self.event_subtype, None)

        elif self.source == "hip":
            tshoot_handler = 'hip'
            handler = HIP_EVENTS.get(self.event_subtype, None)

        elif self.source == "threat":
            tshoot_handler = 'threat'
            handler = THREAT_EVENTS.get(self.event_subtype, None)

        elif self.source == "url":
            tshoot_handler = 'url'
            handler = URL_EVENTS.get(self.event_subtype, None)

        elif self.source == "data":
            tshoot_handler = 'data'
            handler = DATA_EVENTS.get(self.event_subtype, None)

        elif self.source == "wildfire":
            tshoot_handler = 'wildfire'
            handler = WILDFIRE_EVENTS.get(self.event_subtype, None)

        elif self.source == "traffic":
            tshoot_handler = 'traffic'
            handler = TRAFFIC_EVENTS.get(self.event_subtype, None)

        elif self.source == "tunnel":
            tshoot_handler = 'tunnel'
            handler = TUNNEL_EVENTS.get(self.event_subtype, None)

        elif self.source == "decryption":
            tshoot_handler = 'decryption'
            handler = DECRYPTION_EVENTS.get(self.event_subtype, None)

        # If there's no handler found for the event type
        if handler is None or handler == {}:
            tshoot = {
                'tshoot': {
                    'source': self.source,
                    'event_type': self.event_type,
                    'event_subtype': self.event_subtype,
                    'handler': tshoot_handler,
                }
            }
            self.event.update(tshoot)

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

                self.alert_type = self.event_subtype

            except Exception as e:
                logging.error(
                    f"Error formatting event message for {self.event}:"
                    f"\n{e}"
                )
                message = "No message included"
                self.teams_msg = str(self.event)
                self.severity = "warning"
                self.alert_type = "Unknown Event"

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
            teams_chat = self.chat_list.get(
                actions['chat'], None
            )
        else:
            teams_chat = self.default_chat
        if teams_chat is None:
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

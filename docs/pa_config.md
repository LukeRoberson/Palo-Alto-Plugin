# Configuring the PA

The PA needs to be configured to send alerts to the agent. This is effectively a webhook, but in PA terms it's called an HTTP log forwarder.

The main difference is that there's no fixed webhook body format, as in most systems. An admin needs to configure these manually.

On each PA, configure:
1. An HTTP server profile
2. Log Settings
</br></br>


## HTTP Server Profile

Browse to Device > Server Profiles > HTTP, and create a new profile.
</br></br>

### Server Definition

Give the profile a name, and add a server. This should contain:
* A friendly name
* The server FQDN (not the URL to send webhooks to)
* Protocol, port, TLS version
* Certificate profile (optional)
* HTTP method (set to _POST_)
* Username and password (for Basic auth)
</br></br>


### Payload Format

In the _Payload Format_ tab, there are a series of log types (config, system, etc). These define the messages that are sent to the agent, and the format they take.

Edit each of these formats, and give it a name. Leave _Pre-defined Formats_ empty.

In the _URI Format_, enter the rest of the URL for the webhook destination. For example, **/plugin/paloalto/webhook**.

In the _HTTP Headers_ section, add a **content-type** header with the value of **application/json**.

Leave the _Parameters_ section empty.
</br></br>

The _Payload_ is the body that's sent to the agent. This will be JSON data, and will vary depending on the alert type.

The **payload.md** file contains information on the different fields that are supported here.

To work with the agent, this needs to be formated in a particular way, as shown in the **Payload Format** section below.
</br></br>


## Log Configuration - System, Configuration, User-ID

Browse to Device > Log Settings. Here is a series of log types (system, configuration, etc).

Add an entry to each one as needed (or edit an existing one if you want). More than one definition is supported here.

Edit the filter if desired. For example, to send only a particular log type, or only logs that match some conditions. For some of these, leaving the default _All Logs_ will add strain to the system.

In the _HTTP_ area, add the HTTP server profile that you have created.
</br></br>


## Log Configuration - Traffic, Threat, URL, Data, Auth, Decryption, Tunnel, Wildfire

Browse to Objects > Log Forwarding. Create or edit a profile.

Add an item for each Log type you want to forward to the agent.
1. Give it a Name
2. Optionally add a description
3. Choose the log type from the drop-down
4. Optionally configure filters
5. Set the HTTP profile in the _Forward Method_ area.


----
# Payload Format

The payloads for each log type should be configured as shown below, so they can be parsed by the agent.
</br></br>


## Config

```json
{
    "alert": {
        "source": "config",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "config": {
        "user": "$admin",
        "client": "$client",
        "host": "$host",
        "cmd": "$cmd",
        "full-path": "$full-path",
        "comment": "$comment",
        "result": "$result"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    }
}
```
</br></br>

Optionally, include these:
```json
{
    "after-change-detail": "$after-change-detail",
    "before-change-detail": "$before-change-detail"
}
```
</br></br>

However, these will make the payload much larger, so it's recommended not to use them. A separate API call could be used to get this information in the cases where it's needed.
</br></br>



## System

Reports on global system events.
</br></br>

```json
{
    "alert": {
        "source": "system",
        "severity": "$severity",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype",
        "module": "$module",
        "name": "$eventid",
        "description": "$opaque",
        "object": "$object"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    }
}
```
</br></br>




## User-ID

Reports on anything related to User-ID, such as when a user is associated with an IP or port range.
</br></br>


```json
{
    "alert": {
        "source": "userid",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "source": {
        "type": "$datasource",
        "name": "$datasourcename"
    },
    "client": {
        "ip": "$ip",
        "ntlm": "$user",
        "upn": "$userbysource",
        "tag_name": "$tag_name"
    }
}
```
</br></br>



## Globalprotect

Associated with Global Protect events (logon, logoff, failures, etc)
</br></br>


```json
{
    "alert": {
        "source": "globalprotect",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "client": {
        "srcuser": "$srcuser",
        "os": "$client_os",
        "os_ver": "$client_os_ver",
        "host_name": "$machinename",
        "host_serial": "$serialnumber",
        "globalprotect_ver": "$client_ver",
        "private_ip": "$private_ip",
        "private_ipv6": "$private_ipv6",
        "public_ip": "$public_ip",
        "public_ipv6": "$public_ipv6",
        "srcregion": "$srcregion",
        "login_duration": "$login_duration",
        "auth_method": "$auth_method"
    },
    "gateway_portal": {
        "portal": "$portal",
        "gateway": "$gateway",
        "attempted_gateways": "$attempted_gateways",
        "gateway_priority": "$priority",
        "gateway_selection": "$selection_type",
        "gateway_method": "$connect_method",
        "location": "$location",
        "tunnel_type": "$tunnel_type"
    },
    "event": {
        "event_name": "$eventid",
        "description": "$opaque",
        "error": "$error",
        "error_code": "$error_code",
        "stage": "$stage",
        "status": "$status",
        "quarantine_reason": "$reason"
    }
}
```
</br></br>


## Authentication

Used with Authentication policies. Policies > Authentication > Edit Policy > Set Log Forwarding action.
</br></br>


```json
{
    "alert": {
        "source": "auth",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "client": {
        "user": "$user",
        "normalize_user": "$normalize_user",
        "ip": "$ip",
        "region": "$region",
        "clienttype": "$clienttype"
    },
    "auth": {
        "authpolicy": "$authpolicy",
        "authproto": "$authproto",
        "factorno": "$factorno",
        "serverprofile": "$serverprofile",
        "vendor": "$vendor"
    },
    "event": {
        "desc": "$desc",
        "event": "$event",
        "object": "$object"
    }
}
```
</br></br>


## Iptag

Anything related to IP tagging.

https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/policy/register-ip-addresses-and-tags-dynamically
</br></br>


```json
{
    "alert": {
        "source": "iptag",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tag": {
        "name": "$tag_name",
        "ip": "$ip",
        "subnet_range": "$ip_subnet_range"
    },
    "event": {
        "event_id": "$event_id",
        "datasource_subtype": "$datasource_subtype",
        "datasource_type": "$datasource_type",
        "datasourcename": "$datasourcename"
    }
}
```
</br></br>


## HIP Match

```json
{
    "alert": {
        "source": "hip",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "host": {
        "machinename": "$machinename",
        "os": "$os",
        "serialnumber": "$serialnumber",
        "mac": "$mac",
        "src": "$src",
        "srcipv6": "$srcipv6"
    },
    "user": {
        "srcuser": "$srcuser"
    },
    "match": {
        "matchname": "$matchname",
        "matchtype": "$matchtype"
    }
}
```
</br></br>


## Threat

Associated with security policies. Policies > Security > Edit a security policy > Set a log forwarding action.
</br></br>


```json
{
    "alert": {
        "source": "threat",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to",
        "direction": "$direction",
        "src_country": "$srcloc",
        "dst_country": "$dstloc",
        "src_user": "$srcuser",
        "dst_user": "$dstuser",
        "nat_src_ip": "$natsrc",
        "nat_dst_ip": "$natdst",
        "nat_sport": "$natsport",
        "nat_dport": "$natdport"
    },
    "threat": {
        "fw_rule": "$rule",
        "id": "$threatid",
        "name": "$threat_name",
        "category": "$thr_category",
        "severity": "$severity",
        "action": "$action",
        "reason": "$reason",
        "justification": "$justification"
    },
    "app": {
        "app": "$app",
        "app_type": "$technology_of_app",
        "sanctioned": "$sanctioned_state_of_app"
    },
    "tunnel": {
        "tunnel": "$tunnel",
        "tunneled_app": "$tunneled_app"
    },
    "edl": {
        "src_edl": "$src_edl",
        "dst_edl": "$dst_edl",
        "domain_edl": "$domain_edl"
    },
    "content_filter": {
        "filetype": "$filetype",
        "filedigest": "$filedigest",
        "category": "$category",
        "xff": "$xff",
        "misc": "$misc"
    }
}
```
</br></br>


## URL

```json
{
    "alert": {
        "source": "url",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to",
        "direction": "$direction",
        "src_country": "$srcloc",
        "dst_country": "$dstloc",
        "src_user": "$srcuser",
        "dst_user": "$dstuser",
        "nat_src_ip": "$natsrc",
        "nat_dst_ip": "$natdst",
        "nat_sport": "$natsport",
        "nat_dport": "$natdport"
    },
    "threat": {
        "fw_rule": "$rule",
        "id": "$threatid",
        "name": "$threat_name",
        "category": "$thr_category",
        "severity": "$severity",
        "action": "$action",
        "reason": "$reason",
        "justification": "$justification"
    },
    "app": {
        "app": "$app",
        "app_type": "$technology_of_app",
        "sanctioned": "$sanctioned_state_of_app"
    },
    "tunnel": {
        "tunnel": "$tunnel",
        "tunneled_app": "$tunneled_app"
    },
    "edl": {
        "src_edl": "$src_edl",
        "dst_edl": "$dst_edl",
        "domain_edl": "$domain_edl"
    },
    "content_filter": {
        "filetype": "$filetype",
        "filedigest": "$filedigest",
        "category": "$category",
        "xff": "$xff",
        "misc": "$misc"
    }
}
```
</br></br>


## Data

```json
{
    "alert": {
        "source": "data",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to",
        "direction": "$direction",
        "src_country": "$srcloc",
        "dst_country": "$dstloc",
        "src_user": "$srcuser",
        "dst_user": "$dstuser",
        "nat_src_ip": "$natsrc",
        "nat_dst_ip": "$natdst",
        "nat_sport": "$natsport",
        "nat_dport": "$natdport"
    },
    "threat": {
        "fw_rule": "$rule",
        "id": "$threatid",
        "name": "$threat_name",
        "category": "$thr_category",
        "severity": "$severity",
        "action": "$action",
        "reason": "$reason",
        "justification": "$justification"
    },
    "app": {
        "app": "$app",
        "app_type": "$technology_of_app",
        "sanctioned": "$sanctioned_state_of_app"
    },
    "tunnel": {
        "tunnel": "$tunnel",
        "tunneled_app": "$tunneled_app"
    },
    "edl": {
        "src_edl": "$src_edl",
        "dst_edl": "$dst_edl",
        "domain_edl": "$domain_edl"
    },
    "content_filter": {
        "filetype": "$filetype",
        "filedigest": "$filedigest",
        "category": "$category",
        "xff": "$xff",
        "misc": "$misc"
    }
}
```
</br></br>


## WildFire

```json
{
    "alert": {
        "source": "wildfire",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to",
        "direction": "$direction",
        "src_country": "$srcloc",
        "dst_country": "$dstloc",
        "src_user": "$srcuser",
        "dst_user": "$dstuser",
        "nat_src_ip": "$natsrc",
        "nat_dst_ip": "$natdst",
        "nat_sport": "$natsport",
        "nat_dport": "$natdport"
    },
    "threat": {
        "fw_rule": "$rule",
        "id": "$threatid",
        "name": "$threat_name",
        "category": "$thr_category",
        "severity": "$severity",
        "action": "$action",
        "reason": "$reason",
        "justification": "$justification"
    },
    "app": {
        "app": "$app",
        "app_type": "$technology_of_app",
        "sanctioned": "$sanctioned_state_of_app"
    },
    "tunnel": {
        "tunnel": "$tunnel",
        "tunneled_app": "$tunneled_app"
    },
    "edl": {
        "src_edl": "$src_edl",
        "dst_edl": "$dst_edl",
        "domain_edl": "$domain_edl"
    },
    "content_filter": {
        "filetype": "$filetype",
        "filedigest": "$filedigest",
        "category": "$category",
        "xff": "$xff",
        "misc": "$misc"
    }
}
```
</br></br>


## Traffic


```json
{
    "alert": {
        "source": "traffic",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to",
        "src_country": "$srcloc",
        "dst_country": "$dstloc",
        "src_user": "$srcuser",
        "dst_user": "$dstuser"
    },
    "app": {
        "app": "$app",
        "category_of_app": "$category_of_app",
        "sanctioned_state_of_app": "$sanctioned_state_of_app",
        "technology_of_app": "$technology_of_app"
    },
    "counters": {
        "bytes": "$bytes",
        "bytes_received": "$bytes_received",
        "bytes_sent": "$bytes_sent",
        "packets": "$packets",
        "pkts_received": "$pkts_received",
        "pkts_sent": "$pkts_sent"
    },
    "session": {
        "rule": "$rule",
        "action": "$action",
        "action_source": "$action_source",
        "verdict": "$category",
        "start": "$start",
        "elapsed": "$elapsed",
        "session_end_reason": "$session_end_reason",
        "xff_ip": "$xff_ip",
        "dst_edl": "$dst_edl",
        "src_edl": "$src_edl"
    },
    "tunnel": {
        "tunnel": "$tunnel",
        "parent_session_id": "$parent_session_id",
        "parent_start_time": "$parent_start_time",
        "tunneled_app": "$tunneled_app"
    }
}
```
</br></br>


## Tunnel


```json
{
    "alert": {
        "source": "tunnel",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to"
    },
    "app": {
        "app": "$app",
        "category_of_app": "$category_of_app",
        "sanctioned_state_of_app": "$sanctioned_state_of_app",
        "technology_of_app": "$technology_of_app"
    },
    "counters": {
        "bytes": "$bytes",
        "bytes_received": "$bytes_received",
        "bytes_sent": "$bytes_sent",
        "packets": "$packets",
        "pkts_received": "$pkts_received",
        "pkts_sent": "$pkts_sent"
    },
    "session": {
        "rule": "$rule",
        "action": "$action",
        "action_source": "$action_source",
        "verdict": "$category",
        "start": "$start",
        "elapsed": "$elapsed",
        "session_end_reason": "$session_end_reason"
    },
    "tunnel": {
        "tunnel": "$tunnel",
        "start": "$start",
        "parent_session_id": "$parent_session_id",
        "parent_start_time": "$parent_start_time",
        "sessions_closed": "$sessions_closed",
        "sessions_created": "$sessions_created"
    },
    "drops": {
        "max_encap": "$max_encap",
        "strict_check": "$strict_check",
        "tunnel_fragment": "$tunnel_fragment",
        "tunnel_insp_rule": "$tunnel_insp_rule",
        "unknown_proto": "$unknown_proto"
    }
}
```
</br></br>


## Decryption


```json
{
    "alert": {
        "source": "decryption",
        "timestamp": "$time_generated"
    },
    "details": {
        "type": "$type",
        "subtype": "$subtype"
    },
    "device": {
        "device_name": "$device_name",
        "sender_sw_version": "$sender_sw_version",
        "serial": "$serial"
    },
    "tuple": {
        "proto": "$proto",
        "src": "$src",
        "dst": "$dst",
        "sport": "$sport",
        "dport": "$dport"
    },
    "match": {
        "inbound_if": "$inbound_if",
        "outbound_if": "$outbound_if",
        "from_zone": "$from",
        "to_zone": "$to"
    },
    "app": {
        "app": "$app",
        "category_of_app": "$category_of_app",
        "sanctioned_state_of_app": "$sanctioned_state_of_app",
        "technology_of_app": "$technology_of_app"
    },
    "certificate": {
        "cn": "$cn",
        "sni": "$sni",
        "cert_serial": "$cert_serial",
        "cert_size": "$cert_size",
        "notafter": "$notafter",
        "notbefore": "$notbefore",
        "issuer_cn": "$issuer_cn",
        "root_cn": "$root_cn",
        "root_status": "$root_status",
        "chain_status": "$chain_status"
    },
    "crypto": {
        "ec_curve": "$ec_curve",
        "tls_auth": "$tls_auth",
        "tls_enc": "$tls_enc",
        "tls_keyxchg": "$tls_keyxchg",
        "tls_version": "$tls_version",
        "hs_stage_c2f": "$hs_stage_c2f",
        "hs_stage_f2s": "$hs_stage_f2s"
    },
    "event": {
        "err_index": "$err_index",
        "error": "$error",
        "policy_name": "$policy_name",
        "proxy_type": "$proxy_type"
    }
}
```
</br></br>


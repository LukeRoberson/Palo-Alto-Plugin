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

Common fields to use:
```json
{
    "alert": {
        "source": "<SOURCE>",
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
    }
}
```


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

## Threat

```json
{
    "alert": {
        "source": "<SOURCE>",
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

TBA

```json
{

}
```
</br></br>

## URL

TBA

```json
{

}
```
</br></br>

## Data

TBA

```json
{

}
```
</br></br>

## WildFire

TBA

```json
{

}
```
</br></br>

## Tunnel

TBA

```json
{

}
```
</br></br>

## Authentication

TBA

```json
{

}
```
</br></br>

## User-ID

```json
{
    "alert": {
        "source": "<SOURCE>",
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



## HIP Match

TBA

```json
{

}
```
</br></br>

## Globalprotect

TBA

```json
{

}
```
</br></br>

## Iptag

TBA

```json
{

}
```
</br></br>

## Decryption

TBA

```json
{

}
```
</br></br>


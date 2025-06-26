# Payload Fields

On the Palo Alto, the webhook message is customizable. The **payload** section of each log type has various variables that can be used.

Variables are referenced by a leading dollar-sign. They can be included in the message body, headers, or parameters.

When sending these in a JSON body, the variable still needs to be inside double-quotes. There is a maximum of 2048 characters in the payload body.

For example:

```json
{
    "admin": "$admin"
}
```
</br></br>


## Log Types

This page is for general log types, including:
* System
* Configuration
* Authentication
* User-ID
* HIP Match
* Global Protect
* IP Tag

For other types, see **traffic_payloads.md** and **threat_payloads.md**..
</br></br>


# Common Fields

These fields are available to all log types:

| Variable                     | Description                                    | Example Value                 |
| ---------------------------- | ---------------------------------------------- | ----------------------------- |
| actionflags                  | For sending to Panorama                        | 0x8000000000                  |
| cef-formatted-receive_time   | Timestamp in CEF format                        | Jun 20 2025 05:22:38 GMT      |
| cef-formatted-time_generated | Timestamp in CEF format                        | Jun 20 2025 05:22:37 GMT      |
| device_name                  | The hostname of the firewall                   | PM-8-0-VM                     |
| dg_hier_level_1              | Device Group hierarchy                         |                               |
| dg_hier_level_2              | Device Group hierarchy                         |                               |
| dg_hier_level_3              | Device Group hierarchy                         |                               |
| dg_hier_level_4              | Device Group hierarchy                         |                               |
| receive_time                 | Time logs was received at the management plane | 2025/06/20 15:22:38           |
| high_res_timestamp           | receive_time in milliseconds                   | 1970-01-01T10:00:00.000+10:00 |
| sender_sw_version            | PANOS version                                  | 11.2.5                        |
| seqno                        | Unique log sequence number                     | 7492210632692619605           |
| serial                       | Serial number of the firewall                  | 7200002624                    |
| type                         | Main log type                                  | SYSTEM                        |
| subtype                      | System daemon generating the log               | device-telemetry              |
| time_generated               | Time the log was generated on the dataplane    | 2025/06/20 15:22:37           |
| vsys                         | Virtual System associated with the log         |                               |
| vsys_id                      | ID of the Virtual System                       |                               |
| vsys_name                    | Name of the Virtual System                     |                               |
</br></br>

```json
{
    "actionflags": "$actionflags",
    "cef-formatted-receive_time": "$cef-formatted-receive_time",
    "cef-formatted-time_generated": "$cef-formatted-time_generated",
    "device_name": "$device_name",
    "dg_hier_level_1": "$dg_hier_level_1",
    "dg_hier_level_2": "$dg_hier_level_2",
    "dg_hier_level_3": "$dg_hier_level_3",
    "dg_hier_level_4": "$dg_hier_level_4",
    "high_res_timestamp": "$high_res_timestamp",
    "receive_time": "$receive_time",
    "sender_sw_version": "$sender_sw_version",
    "seqno": "$seqno",
    "serial": "$serial",
    "subtype": "$subtype",
    "time_generated": "$time_generated",
    "type": "$type",
    "vsys": "$vsys",
    "vsys_id": "$vsys_id",
    "vsys_name": "$vsys_name"
}
```
</br></br>



# Unique Fields

## Config

Events relating to configuration changes.

https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/config-log-fields
</br></br>


| Variable                     | Description                                           | Example Value                 |
| ---------------------------- | ----------------------------------------------------- | ----------------------------- |
| admin                        | Admin user name                                       | test                          |
| after-change-detail          | Full xpath after the change                           |                               |
| before-change-detail         | Full xpath before the change                          |                               |
| client                       | Web or CLI client used                                | Web                           |
| cmd                          | Command performed by admin                            | set                           |
| comment                      | Commit comment                                        | test comment                  |
| dg_id                        | The device group the firewall is in                   |                               |
| path                         | The path of the configuration command (max 512 bytes) |                               |
| full-path                    |                                                       |                               |
| host                         | Hostname or IP of the client machine                  |                               |
| result                       | Result of commit                                      | Succeeded                     |
| tpl_id                       |                                                       |                               |
</br></br>

```json
{
    "admin": "$admin",
    "after-change-detail": "$after-change-detail",
    "before-change-detail": "$before-change-detail",
    "client": "$client",
    "cmd": "$cmd",
    "comment": "$comment",
    "dg_id": "$dg_id",
    "full-path": "$full_path",
    "host": "$host",
    "path": "$path",
    "result": "$result",
    "tpl_id": "$tpl_id",
}
```
</br></br>

Command types:
* add
* clone
* commit
* delete
* edit
* move
* rename
* set

Notes:
* _subtype_ is unused in the config log. It is set to "0".
</br></br>



----
## System

| Variable                     | Description                      | Example Value                                       |
| ---------------------------- | -------------------------------- | --------------------------------------------------- |
| cef-number-of-severity       | Severity, CEF format (0-10)      | 1                                                   |
| device_type                  | Alert message                    | RASMGR daemon configuration load phase-2 succeeded. |
| dg_id                        | Device group ID                  |                                                     |
| eventid                      | Name of the event                | rasmgr-config-p2-success                            |
| module                       | Additional 'subtype' information | general                                             |
| number-of-severity           |                                  | 1                                                   |
| object                       | Name of the associated object    |                                                     |
| opaque                       | The description of the event     |                                                     |
| sdwan_cluster                |                                  |                                                     |
| sdwan_site                   |                                  |                                                     |
| severity                     | Alert severity                   | informational                                       |
| tpl_id                       |                                  |                                                     |
</br></br>

```json
{
    "cef-number-of-severity": "$cef-number-of-severity",
    "device_type": "$device_type",
    "dg_id": "$dg_id",
    "eventid": "$eventid",
    "module": "$module",
    "number-of-severity": "$number-of-severity",
    "object": "$object",
    "opaque": "$opaque",
    "sdwan_cluster": "$sdwan_cluster",
    "sdwan_site": "$sdwan_site",
    "severity": "$severity",
    "tpl_id": "$tpl_id",
}
```
</br></br>

Subtypes for a system log:
* crypto
* dhcp
* dnsproxy
* dos
* general
* global-protect
* ha
* hw
* nat
* ntpd
* pbf
* port
* pppoe
* ras
* routing
* satd
* sslmgr
* sslvpn
* userid
* url-filtering
* vpn
</br></br>

In addition to the documented types above, these have been observed:
* lacp
</br></br>


The _module_ field is used when the subtype is set to _general_. It provides more information about the sub-system that generates the log.

Values can be:
* general
* management
* auth
* ha
* upgrade
* chassis
</br></br>

https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/system-log-fields
</br></br>


----
## Authentication

| Variable         | Description                         | Example Value |
|------------------|-------------------------------------|---------------|
| authid           | Unique authentication ID            |               |
| authpolicy       | Authentication policy               |               |
| authproto        | Auth protocol on the server         |               |
| clienttype       | Type of client used to authenticate |               |
| cluster_name     |                                     |               |
| desc             | Description (extra info)            |               |
| event            | Result of auth attempt              |               |
| factorno         | Primary or additional auth factors  |               |
| ip               | Source IP                           |               |
| logset           | Log forwarding profile              |               |
| normalize_user   | Normalized version of username      |               |
| object           | Object associated with the event    |               |
| region           | Geo region                          |               |
| repeatcnt        | Identical sessions within 5 seconds |               |
| rule_uuid        | Identify the rule in use            |               |
| serverprofile    | Authentication server               |               |
| sessionid        |                                     |               |
| src_category     | Device-ID: Category                 |               |
| src_host         | Device-ID: Hostname                 |               |
| src_mac          | Device-ID: MAC address              |               |
| src_model        | Device-ID: Model                    |               |
| src_osfamily     | Device-ID: OS Family                |               |
| src_osversion    | Device-ID: OS Version               |               |
| src_profile      | Device-ID: Profile                  |               |
| src_vendor       | Device-ID: Vendor                   |               |
| user             | The user being authenticated        |               |
| user_agent       | User-Agent HTTP header              |               |
| vendor           | Vendor providing MFA                |               |
</br></br>


https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/authentication-log-fields
</br></br>


```json
{
    "authid": "$authid",
    "authpolicy": "$authpolicy",
    "authproto": "$authproto",
    "clienttype": "$clienttype",
    "cluster_name": "$cluster_name",
    "desc": "$desc",
    "event": "$event",
    "factorno": "$factorno",
    "ip": "$ip",
    "logset": "$logset",
    "normalize_user": "$normalize_user",
    "object": "$object",
    "region": "$region",
    "repeatcnt": "$repeatcnt",
    "rule_uuid": "$rule_uuid",
    "serverprofile": "$serverprofile",
    "sessionid": "$sessionid",
    "src_category": "$src_category",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_vendor": "$src_vendor",
    "user": "$user",
    "user_agent": "$user_agent",
    "vendor": "$vendor"
}
```
</br></br>

----
## User-ID

| Variable             | Description                                                   | Example Value |
|----------------------|---------------------------------------------------------------|---------------|
| beginport            | Source port used in the session                               |               |
| cluster_name         |                                                               |               |
| datasource           | Source the mapping was collected from                         |               |
| datasourcename       | Sender of the Port-User mapping                               |               |
| datasourcetype       | Method of mapping users to IP addresses                       |               |
| direction            |                                                               |               |
| endport              | Destination port used in the session                          |               |
| eventid              | The name of the event                                         |               |
| factorcompletiontime | Time the authentication was completed                         |               |
| factorno             | Indicates the use of primary or additional MFA factors        |               |
| factortype           | Vendor used to auth a user when MFA is present                |               |
| ip                   | Original session source IP                                    |               |
| origindatasource     |                                                               |               |
| repeatcnt            | Num sessions with same src-ip/dst-ip/app/subtype in 5 seconds |               |
| tag_name             | Name of the tag associated with the dynamic user group        |               |
| timeout              | Timeout, after which User-IP mappings are cleared             |               |
| ugflags              | User Group flags                                              |               |
| user                 | The end user                                                  |               |
| userbysource         | The username received from the source                         |               |

</br></br>

```json
{
    "beginport": "$beginport",
    "cluster_name": "$cluster_name",
    "datasource": "$datasource",
    "datasourcename": "$datasourcename",
    "datasourcetype": "$datasourcetype",
    "direction": "$direction",
    "endport": "$endport",
    "eventid": "$eventid",
    "factorcompletiontime": "$factorcompletiontime",
    "factorno": "$factorno",
    "factortype": "$factortype",
    "ip": "$ip",
    "origindatasource": "$origindatasource",
    "repeatcnt": "$repeatcnt",
    "tag_name": "$tag_name",
    "timeout": "$timeout",
    "ugflags": "$ugflags",
    "user": "$user",
    "userbysource": "$userbysource"
}
```
</br></br>

**Subtypes** can be:
* login - User logged in.
* logout - User logged out.
* register-tag - Indicates a tag or tags were registered for the user.
* unregister-tag - Indicates a tag or tags were unregistered for the user.
</br></br>


**ugflags** can be:
* User Group Found - Indicates whether the user could be mapped to a group.
* Duplicate User - Indicates whether duplicate users were found in a user group. Displays N/A if no user group is found.


https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/user-id-log-fields
</br></br>


----
## HIP Match

Note: The _subtype_ field is unused for a HIP match.
</br></br>


| Variable     | Description                           | Example Value |
|--------------|---------------------------------------|---------------|
| cluster_name |                                       |               |
| hostid       | ID Global Protect assigns to the host |               |
| mac          | User machine's MAC                    |               |
| machinename  | Hostname of the machine               |               |
| matchname    | HIP object/profile                    |               |
| matchtype    | HIP field or HIP object               |               |
| os           | Host operating system                 |               |
| reclassified |                                       |               |
| repeatcnt    | Times the HIP profile is matched      |               |
| serialnumber | Serial number of the user's machine   |               |
| src          | IP of the source user                 |               |
| srcipv6      | IP of the source user                 |               |
| srcuser      | User initiating the session           |               |
</br></br>


```json
{
    "cluster_name": "$cluster_name",
    "hostid": "$hostid",
    "mac": "$mac",
    "machinename": "$machinename",
    "matchname": "$matchname",
    "matchtype": "$matchtype",
    "os": "$os",
    "reclassified": "$reclassified",
    "repeatcnt": "$repeatcnt",
    "serialnumber": "$serialnumber",
    "src": "$src",
    "srcipv6": "$srcipv6",
    "srcuser": "$srcuser",
}
```
</br></br>

----
## Globalprotect

https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/globalprotect-log-fields
</br></br>


| Variable           | Description                                                        | Example Value |
|--------------------|--------------------------------------------------------------------|---------------|
| attempted_gateways | Gateways that were available and attempted for the client location |               |
| auth_method        | auth method used for the connection                                | saml                              |
| client_os          | Client's OS                                                        | Windows                           |
| client_os_ver      | Version of client's OS                                             | Microsoft Windows 11 Pro , 64-bit |
| client_ver         | Global protect version                                             | 6.3.3                             |
| cluster_name       |                                                                    |                                   |
| connect_method     | How the GlobalProtect app connected to the the Gateway             | user-logon                        |
| error              | Error information for an unsuccessful connection                   |               |
| error_code         | A code assigned to the error                                       |               |
| eventid            | The name of the event                                              | portal-prelogin                   |
| gateway            | The name of the gateway in the portal config                       |               |
| hostid             | A unique ID assigned to the host                                   |               |
| location           | Location of the portal or gateway                                  |               |
| login_duration     | Total duration of the session                                      |               |
| machinename        | Hostname of the user's machine                                     | PC-001                            |
| opaque             | Additional information (description)                               | SAML request sent                 |
| portal             | The name of the portal/gateway                                     | GP_Portal                         |
| priority           | The priority order of the gateway                                  |               |
| private_ip         | Client's private IP                                                |               |
| private_ipv6       | Client's private IP                                                |               |
| project_name       |                                                                    |               |
| public_ip          | Client's public IP                                                 | 1.2.3.4                           |
| public_ipv6        | Client's public IP                                                 |               |
| reason             | The reason for quarantine                                          |               |
| repeatcnt          | Number of identical sessions in the last 5 seconds                 |               |
| response_time      | SSL response time (in ms)                                          |               |
| selection_type     | The method of selecting the gateway                                |               |
| serialnumber       | Serial number of the client device                                 | 2ZM3V04                           |
| srcregion          | The region for the source user                                     | AU                                |
| srcuser            | The user who initiated the session                                 | user@domain                       |
| stage              | The stage of the connection                                        | before-login                      |
| status             | Success or failure                                                 | success                           |
| tunnel_type        | SSLVPN or IPSec tunnel                                             |               |

</br></br>

```json
{
    "attempted_gateways": "$attempted_gateways",
    "auth_method": "$auth_method",
    "client_os": "$client_os",
    "client_os_ver": "$client_os_ver",
    "client_ver": "$client_ver",
    "cluster_name": "$cluster_name",
    "connect_method": "$connect_method",
    "error": "$error",
    "error_code": "$error_code",
    "eventid": "$eventid",
    "gateway": "$gateway",
    "hostid": "$hostid",
    "location": "$location",
    "login_duration": "$login_duration",
    "machinename": "$machinename",
    "opaque": "$opaque",
    "portal": "$portal",
    "priority": "$priority",
    "private_ip": "$private_ip",
    "private_ipv6": "$private_ipv6",
    "project_name": "$project_name",
    "public_ip": "$public_ip",
    "public_ipv6": "$public_ipv6",
    "reason": "$reason",
    "repeatcnt": "$repeatcnt",
    "response_time": "$response_time",
    "selection_type": "$selection_type",
    "serialnumber": "$serialnumber",
    "srcregion": "$srcregion",
    "srcuser": "$srcuser",
    "stage": "$stage",
    "status": "$status",
    "tunnel_type": "$tunnel_type"
}
```
</br></br>

**Subtypes** aren't used in the Global Protect log type. It is better to use **eventid**. These events are below

Portal events:
* portal-auth - Indicates a GlobalProtect portal authentication stage
* portal-gen-cookie - Indicates a GlobalProtect portal authentication override cookie generation event
* portal-getconfig - Indicates a GlobalProtect portal event for generating GlobalProtect client configuration, such as dynamic app configuration or gateway list.
* portal-prelogin - Indicates a GlobalProtect portal pre-login event: Checks certificate, generates SAML request, triggers kerberos authentication

Gateway events:
* gateway-agent-msg - Indicates a GlobalProtect gateway event for a message received from the GlobalProtect client, such as GlobalProtect client disable reason message.
* gateway-auth - Indicates GlobalProtect gateway authentication stage.
* gateway-config-release - Indicates a GlobalProtect gateway event for configuration release, such as remove ip-user mapping or remove tunnel.
* gateway-connected - Indicates a GlobalProtect gateway event for a GlobalProtect client successful connection for tunnel or non-tunnel mode.
* gateway-framed-ip - Indicates a GlobalProtect gateway event where the gateway retrieved a framed IPv4 address from RADIUS for a GlobalProtect client.
* gateway-getconfig - Indicates a GlobalProtect gateway event for generating GlobalProtect client configuration, such as split-tunnel, virtual IP, or tunnel information.
* gateway-hip-check - Confirm whether a GlobalProtect HIP report was updated or not, and to refresh ip-user mapping
* gateway-hip-report - Confirm whether a HIP report was received from a GlobalProtect client, to update ip-user mapping, and to enforce HIP policy
* gateway-inheritance - GlobalProtect gateway is using a dynamic IP address and the IP address changed.
* gateway-logout - Client logout
* gateway-prelogin - Indicates a GlobalProtect gateway pre-login event: Checks certificate, generates SAML request, triggers kerberos authentication
* gateway-register - Indicates GlobalProtect client user information, such as username, domain-name, computer name, hostid, serial number, public ip, or login time is added on the gateway.
* gateway-setup-ipsec - Indicates a GlobalProtect gateway event for setting up an IPSec VPN tunnel.
* gateway-setup-ssl - Indicates a GlobalProtect gateway event for setting up a SSL VPN tunnel.
* gateway-switch-to-ssl - Indicates a GlobalProtect gateway tunnel switch from IPSec to SSL considering IPSec tunnel was not successful.
* gateway-tunnel-latency - GlobalProtect gateway latency provided by a GlobalProtect client
* quarantine-add - The client is added to the quarantine list
* quarantine-delete - The client is removed from the quarantine list

Clientless VPN events:
* clientlessvpn-login - Portal event for GlobalProtect Clientless VPN login
* clientlessvpn-logout - Portal event for GlobalProtect Clientless VPN logout
* clientlessvpn-prelogin - Indicates a GlobalProtect portal pre-login event: Checks certificate, generates SAML request, triggers kerberos authentication

https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/logging-for-globalprotect-in-pan-os/event-descriptions-for-the-globalprotect-logs-in-pan-os
</br></br>


The **stage** field indicates the stage of the connection. This can be:
* before-login
* login
* tunnel
</br></br>


The **auth_method** field shows the authentication type, which can be:
* LDAP
* RADIUS
* SAML
</br></br>


The **connect_method** field shows how the app connects to the gateway. These can be:
* on-demand
* user-login
</br></br>


**selection_type** is how the gateway was selected:
* manual - The gateway to which you want the GlobalProtect app to manually connect.
* preferred - The preferred gateway to which you want the GlobalProtect app to connect.
* auto - Automatically connect to the Best Available gateway based on the priority assigned to the gateway and the response time.



----
## Iptag

| Variable           | Description                           | Example Value |
|--------------------|---------------------------------------|---------------|
| cluster_name       |                                       |               |
| datasource_subtype | Mechanism used to map IPs to tags     |               |
| datasource_type    | The type of source                    |               |
| datasourcename     | The source of the mapping information |               |
| event_id           | The name of the event                 |               |
| ip                 | IP address being mapped               |               |
| ip_subnet_range    | IP range being mapped                 |               |
| repeatcnt          | Identical sessions within 5 seconds   |               |
| tag_name           | The tag mapped to the source IP       |               |
| timeout            | Time before IP-Tag mapping expires    |               |
</br></br>


```json
{
    "cluster_name": "$cluster_name",
    "datasource_subtype": "$datasource_subtype",
    "datasource_type": "$datasource_type",
    "datasourcename": "$datasourcename",
    "event_id": "$event_id",
    "ip": "$ip",
    "ip_subnet_range": "$ip_subnet_range",
    "repeatcnt": "$repeatcnt",
    "tag_name": "$tag_name",
    "timeout": "$timeout"
}
```
</br></br>


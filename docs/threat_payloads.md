# Threat Payloads

This page is for log types that are based on threats. These include:
* Threat
* URL
* Data
* WildFire

For other types, see **payload.md** and **traffic_payloads.md**.
</br></br>


# Common Fields

These types of alerts use common fields, which have been roughly organised into categories here.
</br></br>


## Fields
### Network

| Variable                 | Description                                  | Example Value    |
|--------------------------|----------------------------------------------|------------------|
| dport                    | Destination port                             | 443              |
| dst                      | Original session destination IP              | 222.222.222.222  |
| dstloc                   | Destination country                          | Germany          |
| dstuser                  | User to which the session was destined       |                  |
| from                     | The source zone                              | inside           |
| inbound_if               | Interface the session came from              | ae1              |
| natdport                 | Post NAT destination port                    | 33123            |
| natdst                   | Post-NAT destination IP                      | 222.222.222.222  |
| natsport                 | Post NAT source port                         | 443              |
| natsrc                   | Post-NAT source IP                           | 1.2.3.4          |
| outbound_if              | Interface the session goes to                | ae2              |
| proto                    | IP protocol of the session                   | tcp              |
| rule                     | The rule that matched the session            | Web Traffic      |
| rule_uuid                | UUID to identify the rule                    |                  |
| sport                    | source port                                  | 64555            |
| src                      | Original session source IP                   | 10.1.1.1         |
| srcloc                   | Source country                               | Australia        |
| srcuser                  | Username who initiated the session           | domain\\user     |
| to                       | The destination zone                         | outside          |
</br></br>


```json
{
    "dport": "$dport",
    "dst": "$dst",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "from": "$from",
    "inbound_if": "$inbound_if",
    "outbound_if": "$outbound_if",
    "proto": "$proto",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "sport": "$sport",
    "src": "$src",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "to": "$to"
}
```
</br></br>


### Application Details

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| app                      | Application                                  | web-browsing  |
| category_of_app          | Application category                         |               |
| characteristic_of_app    | App characteristics                          |               |
| is_saas_of_app           | '1' if this is a SaaS app                    |               |
| risk_of_app              | Application risk                             |               |
| sanctioned_state_of_app  | '1' is app is sanctioned                     | no            |
| subcategory_of_app       | Application subcategory                      |               |
| technology_of_app        | Application technology                       | browser-based |
</br></br>


```json
{
    "app": "$app",
    "category_of_app": "$category_of_app",
    "characteristic_of_app": "$characteristic_of_app",
    "is_saas_of_app": "$is_saas_of_app",
    "risk_of_app": "$risk_of_app",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "subcategory_of_app": "$subcategory_of_app",
    "technology_of_app": "$technology_of_app"
}
```
</br></br>


### Tunnel Details

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| parent_session_id        | ID of the session in which this is tunnelled |               |
| parent_session_id_64     |                                              |               |
| parent_start_time        | Time parent tunnel session began             |               |
| tunnel                   | Tunnel type (GRE/IPSec)                      | N/A           |
| tunneled_app             | Tunneled application                         | web-browsing  |
</br></br>


```json
{
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app"
}
```
</br></br>


### Session Information

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| dst_dag                  | Destination dynamic address group            |               |
| flags                    | Provides details on the session              |               |
| pcap_id                  | ID of the PCAP file                          |               |
| repeatcnt                | Sessions with the same match in 5 sec        |               |
| sessionid                | Unique session number                        |               |
| sessionid_64             |                                              |               |
| src_dag                  | Source dynamic address group                 |               |
</br></br>


```json
{
    "dst_dag": "$dst_dag",
    "flags": "$flags",
    "pcap_id": "$pcap_id",
    "repeatcnt": "$repeatcnt",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "src_dag": "$src_dag",
}
```
</br></br>


### Threat Information

| Variable                 | Description                                  | Example Value                    |
|--------------------------|----------------------------------------------|----------------------------------|
| contentver               | App and Threats verion                       |                                  |
| severity                 | Threat severity                              | high                             |
| thr_category             | Threat category                              | spyware                          |
| threat_name              |                                              | EICAR Test File Detection(86708) |
| threatid                 | The PA identifier for the type of threat     | EICAR Test File Detection(86708) |
</br></br>


```json
{
    "contentver": "$contentver",
    "severity": "$severity",
    "thr_category": "$thr_category",
    "threat_name": "$threat_name",
    "threatid": "$threatid"
}
```
</br></br>


### Actions

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| action                   | Action taken on the session                  | reset-both    |
| justification            | Justification for data filtering action      |               |
| logset                   | Applied log forwarding profile               |               |
| reason                   | Reason for data filtering action             |               |
</br></br>


```json
{
    "action": "$action",
    "justification": "$justification",
    "logset": "$logset",
    "reason": "$reason",
}
```
</br></br>


### Wildfire and URL

| Variable                 | Description                                  | Example Value                                 |
|--------------------------|----------------------------------------------|-----------------------------------------------|
| category                 | URL or wildfire verdict                      | computer-and-internet-info                    |
| cloud                    | Wildfire: FQDN of wildfire                   |                                               |
| contenttype              | URL: the HTTP content-type                   |                                               |
| filedigest               | Wildfire: binary hash of the file            |                                               |
| filetype                 | Wildfire: Type of file to be analyzed        |                                               |
| http2_connection         | HTTP/2 session ID                            |                                               |
| http2_connection_64      |                                              |                                               |
| http_headers             | URL: Additional HTTP headers                 |                                               |
| http_method              | URL: HTTP Method                             |                                               |
| misc                     | URL or filename                              | www.eicar.org/download-anti-malware-testfile/ |
| referer                  | URL: Referrer HTTP header                    |                                               |
| reportid                 | Wildfire: Analysis request ID                |                                               |
| url_category_list        | URL filtering category                       |                                               |
| url_idx                  | Foreign key to match to other logs           |                                               |
| user_agent               | URL: Browser details                         |                                               |
| xff                      | URL: X-Forwarded-For header                  |                                               |
| xff_ip                   | X-Forwarded-For header                       |                                               |
</br></br>


```json
{
    "category": "$category",
    "cloud": "$cloud",
    "contenttype": "$contenttype",
    "filedigest": "$filedigest",
    "filetype": "$filetype",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "http_headers": "$http_headers",
    "http_method": "$http_method",
    "misc": "$misc",
    "referer": "$referer",
    "reportid": "$reportid",
    "url_category_list": "$url_category_list",
    "url_idx": "$url_idx",
    "user_agent": "$user_agent",
    "xff": "$xff",
    "xff_ip": "$xff_ip"
}
```
</br></br>



### Email

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| recipient                | Recipient on an email                        |               |
| sender                   | Sender of an email                           |               |
| subject                  | Subject of an email                          |               |
</br></br>


```json
{
    "recipient": "$recipient",
    "sender": "$sender",
    "subject": "$subject"
}
```
</br></br>


### Device ID

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| container_id             | Container ID of Kubernetes NGFW pod          |               |
| dst_category             | Device-ID: Destination device category       |               |
| dst_host                 | Device-ID: Destination device hostname       |               |
| dst_mac                  | Device-ID: Destination device MAC address    |               |
| dst_model                | Device-ID: Destination device model          |               |
| dst_osfamily             | Device-ID: Destination device OS family      |               |
| dst_osversion            | Device-ID: Destination device OS version     |               |
| dst_profile              | Device-ID: Destination device profile        |               |
| dst_uuid                 | Unique ID for the destination VM             |               |
| dst_vendor               | Device-ID: Destination device vendor         |               |
| pod_name                 | The application Pod being secured            |               |
| pod_namespace            | Namespace of Pod being secured               |               |
| src_category             | Device-ID: Source device category            |               |
| src_host                 | Device-ID: Source device hostname            |               |
| src_mac                  | Device-ID: Source device MAC address         |               |
| src_model                | Device-ID: Source device model               |               |
| src_osfamily             | Device-ID: Source device OS family           |               |
| src_osversion            | Device-ID: Source device OS version          |               |
| src_profile              | Device-ID: Source device profile             |               |
| src_uuid                 | Unique ID for a guest Virtual Machine        |               |
| src_vendor               | Device-ID: Source device vendor              |               |
</br></br>


```json
{
    "container_id": "$container_id",
    "dst_category": "$dst_category",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "src_category": "$src_category",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor"
}
```
</br></br>


### Cellular

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| monitortag               | IMEI tag for a mobile number                 |               |
| nssai_sst                | Slice Service Type of Network Slice ID (5G)  |               |
| tunnelid                 | IMSI number for mobile subscriber            |               |
</br></br>


```json
{
    "monitortag": "$monitortag",
    "nssai_sst": "$nssai_sst",
    "tunnelid": "$tunnelid"
}
```
</br></br>


### Other Fields

| Variable                 | Description                                  | Example Value    |
|--------------------------|----------------------------------------------|------------------|
| additional_headers       |                                              |                  |
| assoc_id                 | ID for SCTP endpoints                        |                  |
| cef-number-of-severity   |                                              |                  |
| cloud_reportid           |                                              |                  |
| cluster_name             |                                              |                  |
| container_of_app         |                                              |                  |
| direction                | c2s (0) or s2c (1)                           | server-to-client |
| domain_edl               | EDL containing the domain name               |                  |
| dst_edl                  | EDL containing the destination IP            |                  |
| dynusergroup_name        | Name of the dynamic group the user is in     |                  |
| endpoint_id              |                                              |                  |
| file_url                 |                                              |                  |
| flow_type                |                                              |                  |
| hostid                   | Unique Globalprotect host ID                 |                  |
| k8s_cluster_id           |                                              |                  |
| local_deep_learning      |                                              |                  |
| number-of-severity       |                                              |                  |
| partial_hash             | Machine learning partial hash                |                  |
| ppid                     | ID of the protocol for the payload           |                  |
| s_decrypted              |                                              |                  |
| s_encrypted              |                                              |                  |
| saas_sid                 |                                              |                  |
| saas_sidx                |                                              |                  |
| saas_tenant              |                                              |                  |
| saas_type                |                                              |                  |
| saas_user                |                                              |                  |
| security_key             |                                              |                  |
| serialnumber             |                                              |                  |
| sig_flags                |                                              |                  |
| src_edl                  | EDL containing the source IP                 |                  |
| time_received            |                                              |                  |
| vpc_id                   |                                              |                  |
</br></br>


```json
{
    "additional_headers": "$additional_headers",
    "assoc_id": "$assoc_id",
    "cef-number-of-severity": "$cef-number-of-severity",
    "cloud_reportid": "$cloud_reportid",
    "cluster_name": "$cluster_name",
    "container_of_app": "$container_of_app",
    "direction": "$direction",
    "domain_edl": "$domain_edl",
    "dst_edl": "$dst_edl",
    "dynusergroup_name": "$dynusergroup_name",
    "endpoint_id": "$endpoint_id",
    "file_url": "$file_url",
    "flow_type": "$flow_type",
    "hostid": "$hostid",
    "k8s_cluster_id": "$k8s_cluster_id",
    "local_deep_learning": "$local_deep_learning",
    "number-of-severity": "$number-of-severity",
    "partial_hash": "$partial_hash",
    "ppid": "$ppid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "saas_sid": "$saas_sid",
    "saas_sidx": "$saas_sidx",
    "saas_tenant": "$saas_tenant",
    "saas_type": "$saas_type",
    "saas_user": "$saas_user",
    "security_key": "$security_key",
    "serialnumber": "$serialnumber",
    "sig_flags": "$sig_flags",
    "src_edl": "$src_edl",
    "time_received": "$time_received",
    "vpc_id": "$vpc_id"
}
```
</br></br>




----
# Field Details
## Flags Field

The _flags_ field is a 32-bit field where bits indicate some additional information about the session.
* 0x80000000 - session has a packet capture (PCAP)
* 0x40000000 - option is enabled to allow a client to use multiple paths to connect to a destination host
* 0x20000000 - indicates whether a sample has been submitted for analysis using the WildFire public or private cloud channel
* 0x10000000 - enterprise credential submission by end user detected
* 0x08000000 - source for the flow is on an allow list and not subject to recon protection
* 0x02000000 - IPv6 session
* 0x01000000 - SSL session is decrypted (SSL Proxy)
* 0x00800000 - session is denied via URL filtering
* 0x00400000 - session has a NAT translation performed
* 0x00200000 - user information for the session was captured through Authentication Portal
* 0x00100000 - application traffic is on a non-standard destination port
* 0x00080000 - X-Forwarded-For value from a proxy is in the source user field
* 0x00040000 - log corresponds to a transaction within a http proxy session (Proxy Transaction)
* 0x00020000 - Client to Server flow is subject to policy based forwarding
* 0x00010000 - Server to Client flow is subject to policy based forwarding
* 0x00008000 - session is a container page access (Container Page)
* 0x00002000 - session has a temporary match on a rule for implicit application dependency handling. Available in PAN-OS 5.0.0 and above.
* 0x00000800 - symmetric return is used to forward traffic for this session
* 0x00000400 - decrypted traffic is being sent out clear text through a mirror port
* 0x00000010 - payload of the outer tunnel is being inspected
</br></br>


## Actions

Actions can be:
* alert - threat or URL detected but not blocked
* allow - flood detection alert
* deny - flood detection mechanism activated and deny traffic based on configuration
* drop - threat detected and session remains, but drops all packets
* reset-client - threat detected and a TCP RST is sent to the client
* reset-server - threat detected and a TCP RST is sent to the server
* reset-both - threat detected and a TCP RST is sent to both the client and the server
* block-url - URL request was blocked because it matched a URL category that was set to be blocked
* block-ip - threat detected and client IP is blocked
* random-drop - flood detected and packet was randomly dropped
* sinkhole - DNS sinkhole activated
* syncookie - sent—syncookie alert
* block-continue (URL subtype only) - a HTTP request is blocked and redirected to a Continue page with a button for confirmation to proceed
* continue (URL subtype only) - response to a block-continue URL continue page indicating a block-continue request was allowed to proceed
* block-override (URL subtype only) - a HTTP request is blocked and redirected to an Admin override page that requires a pass code from the firewall administrator to continue
* override-lockout (URL subtype only) - too many failed admin override pass code attempts from the source IP. IP is now blocked from the block-override redirect page
* override (URL subtype only) - response to a block-override page where a correct pass code is provided and the request is allowed
* block (Wildfire only) - file was blocked by the firewall and uploaded to Wildfire
</br></br>


# Traffic Payloads

This page is for log types that are based on traffic. These include:
* Threat
* Traffic
* URL
* Data
* WildFire
* Tunnel
* Decryption

For other types, see **payload.md**
</br></br>


# Threat Logs
## Fields
### Network

| Variable                 | Description                                  | Example Value    |
|--------------------------|----------------------------------------------|------------------|
| proto                    | IP protocol of the session                   | tcp              |
| src                      | Original session source IP                   | 10.1.1.1         |
| dst                      | Original session destination IP              | 222.222.222.222  |
| sport                    | source port                                  | 64555            |
| dport                    | Destination port                             | 443              |
| inbound_if               | Interface the session came from              | ae1              |
| outbound_if              | Interface the session goes to                | ae2              |
| from                     | The source zone                              | inside           |
| to                       | The destination zone                         | outside          |
| srcuser                  | Username who initiated the session           | domain\\user     |
| dstuser                  | User to which the session was destined       |                  |
| direction                | c2s (0) or s2c (1)                           | server-to-client |***Not in 'Traffic', 'Tunnel', 'decryption'
| srcloc                   | Source country                               | Australia        |
| dstloc                   | Destination country                          | Germany          |
| natsrc                   | Post-NAT source IP                           | 1.2.3.4          |
| natdst                   | Post-NAT destination IP                      | 222.222.222.222  |
| natdport                 | Post NAT destination port                    | 33123            |
| natsport                 | Post NAT source port                         | 443              |
| rule                     | The rule that matched the session            | Web Traffic      |
| rule_uuid                | UUID to identify the rule                    |                  |
</br></br>


### Application Details

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| app                      | Application                                  | web-browsing  |
| category_of_app          | Application category                         |               |
| subcategory_of_app       | Application subcategory                      |               |
| technology_of_app        | Application technology                       | browser-based |
| risk_of_app              | Application risk                             |               |
| characteristic_of_app    | App characteristics                          |               |
| is_saas_of_app           | '1' if this is a SaaS app                    |               |
| sanctioned_state_of_app  | '1' is app is sanctioned                     | no            |
</br></br>


### Tunnel Details

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| tunnel                   | Tunnel type (GRE/IPSec)                      | N/A           |
| parent_session_id        | ID of the session in which this is tunnelled |               |
| parent_start_time        | Time parent tunnel session began             |               |
| tunneled_app             | Tunneled application                         | web-browsing  |
</br></br>


### Session Information

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| sessionid                | Unique session number                        |               |
| repeatcnt                | Sessions with the same match in 5 sec        |               |
| flags                    | Provides details on the session              |               |
| pcap_id                  | ID of the PCAP file                          |               |
| src_dag                  | Source dynamic address group                 |               |
| dst_dag                  | Destination dynamic address group            |               |
</br></br>


### Threat Information

| Variable                 | Description                                  | Example Value                    |
|--------------------------|----------------------------------------------|----------------------------------|
| threatid                 | The PA identifier for the type of threat     | EICAR Test File Detection(86708) |
| threat_name              |                                              | EICAR Test File Detection(86708) |
| thr_category             | Threat category                              | spyware                          |
| severity                 | Threat severity                              | high                             |
| contentver               | App and Threats verion                       |                                  |
</br></br>


### Actions

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| action                   | Action taken on the session                  | reset-both    |
| logset                   | Applied log forwarding profile               |               |
| reason                   | Reason for data filtering action             |               |
| justification            | Justification for data filtering action      |               |
</br></br>


### Wildfire and URL

| Variable                 | Description                                  | Example Value                                 |
|--------------------------|----------------------------------------------|-----------------------------------------------|
| cloud                    | Wildfire: FQDN of wildfire                   |                                               |
| filedigest               | Wildfire: binary hash of the file            |                                               |
| filetype                 | Wildfire: Type of file to be analyzed        |                                               |
| reportid                 | Wildfire: Analysis request ID                |                                               |
| category                 | URL or wildfire verdict                      | computer-and-internet-info                    |
| contenttype              | URL: the HTTP content-type                   |                                               |
| referer                  | URL: Referrer HTTP header                    |                                               |
| http_method              | URL: HTTP Method                             |                                               |
| user_agent               | URL: Browser details                         |                                               |
| xff                      | URL: X-Forwarded-For header                  |                                               |
| xff_ip                   | X-Forwarded-For header                       |                                               |
| http_headers             | URL: Additional HTTP headers                 |                                               |
| url_category_list        | URL filtering category                       |                                               |
| url_idx                  | Foreign key to match to other logs           |                                               |
| http2_connection         | HTTP/2 session ID                            |                                               |
| misc                     | URL or filename                              | www.eicar.org/download-anti-malware-testfile/ |
</br></br>


### Email

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| sender                   | Sender of an email                           |               |
| recipient                | Recipient on an email                        |               |
| subject                  | Subject of an email                          |               |
</br></br>


### Device ID

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| src_category             | Device-ID: Source device category            |               |
| src_host                 | Device-ID: Source device hostname            |               |
| src_mac                  | Device-ID: Source device MAC address         |               |
| src_model                | Device-ID: Source device model               |               |
| src_osfamily             | Device-ID: Source device OS family           |               |
| src_osversion            | Device-ID: Source device OS version          |               |
| src_profile              | Device-ID: Source device profile             |               |
| src_vendor               | Device-ID: Source device vendor              |               |
| dst_category             | Device-ID: Destination device category       |               |
| dst_host                 | Device-ID: Destination device hostname       |               |
| dst_mac                  | Device-ID: Destination device MAC address    |               |
| dst_model                | Device-ID: Destination device model          |               |
| dst_osfamily             | Device-ID: Destination device OS family      |               |
| dst_osversion            | Device-ID: Destination device OS version     |               |
| dst_profile              | Device-ID: Destination device profile        |               |
| dst_vendor               | Device-ID: Destination device vendor         |               |
| src_uuid                 | Unique ID for a guest Virtual Machine        |               |
| dst_uuid                 | Unique ID for the destination VM             |               |
| container_id             | Container ID of Kubernetes NGFW pod          |               |
| pod_name                 | The application Pod being secured            |               |
| pod_namespace            | Namespace of Pod being secured               |               |
</br></br>


### Cellular

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| monitortag               | IMEI tag for a mobile number                 |               |
| tunnelid                 | IMSI number for mobile subscriber            |               |
| nssai_sst                | Slice Service Type of Network Slice ID (5G)  |               |
</br></br>


### Other Fields

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| additional_headers       |                                              |               |
| assoc_id                 | ID for SCTP endpoints                        |               |
| cef-number-of-severity   |                                              |               |
| cloud_reportid           |                                              |               |
| cluster_name             |                                              |               |
| container_of_app         |                                              |               |
| domain_edl               | EDL containing the domain name               |               |
| dst_edl                  | EDL containing the destination IP            |               |
| src_edl                  | EDL containing the source IP                 |               |
| dynusergroup_name        | Name of the dynamic group the user is in     |               |
| endpoint_id              |                                              |               |
| file_url                 |                                              |               |
| flow_type                |                                              |               |
| hostid                   | Unique Globalprotect host ID                 |               |
| http2_connection_64      |                                              |               |
| k8s_cluster_id           |                                              |               |
| local_deep_learning      |                                              |               |
| number-of-severity       |                                              |               |
| parent_session_id_64     |                                              |               |
| partial_hash             | Machine learning partial hash                |               |
| ppid                     | ID of the protocol for the payload           |               |
| s_decrypted              |                                              |               |
| s_encrypted              |                                              |               |
| saas_sid                 |                                              |               |
| saas_sidx                |                                              |               |
| saas_tenant              |                                              |               |
| saas_type                |                                              |               |
| saas_user                |                                              |               |
| security_key             |                                              |               |
| serialnumber             |                                              |               |
| sessionid_64             |                                              |               |
| sig_flags                |                                              |               |
| time_received            |                                              |               |
| vpc_id                   |                                              |               |
</br></br>


## Additional Information
### Flags Field

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


### Actions

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


## Payload

```json
{
    "additional_headers": "$additional_headers",
    "app": "$app",
    "assoc_id": "$assoc_id",
    "category": "$category",
    "category_of_app": "$category_of_app",
    "cef-number-of-severity": "$cef-number-of-severity",
    "characteristic_of_app": "$characteristic_of_app",
    "cloud": "$cloud",
    "cloud_reportid": "$cloud_reportid",
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "contenttype": "$contenttype",
    "contentver": "$contentver",
    "direction": "$direction",
    "domain_edl": "$domain_edl",
    "dport": "$dport",
    "dst": "$dst",
    "dst_category": "$dst_category",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "dynusergroup_name": "$dynusergroup_name",
    "endpoint_id": "$endpoint_id",
    "file_url": "$file_url",
    "filedigest": "$filedigest",
    "filetype": "$filetype",
    "flags": "$flags",
    "flow_type": "$flow_type",
    "from": "$from",
    "hostid": "$hostid",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "http_headers": "$http_headers",
    "http_method": "$http_method",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "justification": "$justification",
    "k8s_cluster_id": "$k8s_cluster_id",
    "local_deep_learning": "$local_deep_learning",
    "logset": "$logset",
    "misc": "$misc",
    "monitortag": "$monitortag",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "nssai_sst": "$nssai_sst",
    "number-of-severity": "$number-of-severity",
    "outbound_if": "$outbound_if",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "partial_hash": "$partial_hash",
    "pcap_id": "$pcap_id",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "ppid": "$ppid",
    "proto": "$proto",
    "reason": "$reason",
    "recipient": "$recipient",
    "referer": "$referer",
    "repeatcnt": "$repeatcnt",
    "reportid": "$reportid",
    "risk_of_app": "$risk_of_app",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "saas_sid": "$saas_sid",
    "saas_sidx": "$saas_sidx",
    "saas_tenant": "$saas_tenant",
    "saas_type": "$saas_type",
    "saas_user": "$saas_user",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "security_key": "$security_key",
    "sender": "$sender",
    "serialnumber": "$serialnumber",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "severity": "$severity",
    "sig_flags": "$sig_flags",
    "sport": "$sport",
    "src": "$src",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "subcategory_of_app": "$subcategory_of_app",
    "subject": "$subject",
    "technology_of_app": "$technology_of_app",
    "thr_category": "$thr_category",
    "threat_name": "$threat_name",
    "threatid": "$threatid",
    "time_received": "$time_received",
    "to": "$to",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
    "tunnelid": "$tunnelid",
    "url_category_list": "$url_category_list",
    "url_idx": "$url_idx",
    "user_agent": "$user_agent",
    "vpc_id": "$vpc_id",
    "xff": "$xff",
    "xff_ip": "$xff_ip"
}
```
</br></br>



----
## Traffic

| Variable                     | Description                | Example Value                 |
| ---------------------------- | -------------------------- | ----------------------------- |
| action                       |                            |                               |
| action_source                |                            |                               |
| ai_fwd_error                 |                            |                               |
| ai_traffic                   |                            |                               |
| app                          |                            |                               |
| assoc_id                     |                            |                               |
| bytes                        |                            |                               |
| bytes_received               |                            |                               |
| bytes_sent                   |                            |                               |
| category                     |                            |                               |
| category_of_app              |                            |                               |
| characteristic_of_app        |                            |                               |
| chunks                       |                            |                               |
| chunks_received              |                            |                               |
| chunks_sent                  |                            |                               |
| cluster_name                 |                            |                               |
| container_id                 |                            |                               |
| container_of_app             |                            |                               |
| dst_category                 |                            |                               |
| dst_dag                      |                            |                               |
| dst_edl                      |                            |                               |
| dst_host                     |                            |                               |
| dst_mac                      |                            |                               |
| dst_model                    |                            |                               |
| dst_osfamily                 |                            |                               |
| dst_osversion                |                            |                               |
| dst_profile                  |                            |                               |
| dst_uuid                     |                            |                               |
| dst_vendor                   |                            |                               |
| dynusergroup_name            |                            |                               |
| elapsed                      |                            |                               |
| endpoint_id                  |                            |                               |
| flags                        |                            |                               |
| flow_type                    |                            |                               |
| hostid                       |                            |                               |
| http2_connection             |                            |                               |
| http2_connection_64          |                            |                               |
| is_saas_of_app               |                            |                               |
| k8s_cluster_id               |                            |                               |
| link_change_count            |                            |                               |
| link_switches                |                            |                               |
| logset                       |                            |                               |
| monitortag                   |                            |                               |
| ndpmatches                   |                            |                               |
| nftrans                      |                            |                               |
| nssai_sd                     |                            |                               |
| nssai_sst                    |                            |                               |
| nthreats                     |                            |                               |
| nurlcount                    |                            |                               |
| offloaded                    |                            |                               |
| packets                      |                            |                               |
| parent_session_id            |                            |                               |
| parent_session_id_64         |                            |                               |
| parent_start_time            |                            |                               |
| pkts_received                |                            |                               |
| pkts_sent                    |                            |                               |
| pod_name                     |                            |                               |
| pod_namespace                |                            |                               |
| policy_id                    |                            |                               |
| repeatcnt                    |                            |                               |
| risk_of_app                  |                            |                               |
| s_decrypted                  |                            |                               |
| s_encrypted                  |                            |                               |
| sanctioned_state_of_app      |                            |                               |
| sdwan_cluster                |                            |                               |
| sdwan_cluster_type           |                            |                               |
| sdwan_device_type            |                            |                               |
| sdwan_ec_applied             |                            |                               |
| sdwan_ec_session             |                            |                               |
| sdwan_fec_data               |                            |                               |
| sdwan_fec_ratio              |                            |                               |
| sdwan_impacted_link_rx_bytes |                            |                               |
| sdwan_impacted_link_tx_bytes |                            |                               |
| sdwan_impacted_session       |                            |                               |
| sdwan_link                   |                            |                               |
| sdwan_link_rx_bytes          |                            |                               |
| sdwan_link_tag               |                            |                               |
| sdwan_link_tx_bytes          |                            |                               |
| sdwan_link_type              |                            |                               |
| sdwan_pd_session             |                            |                               |
| sdwan_phyintf                |                            |                               |
| sdwan_session                |                            |                               |
| sdwan_site                   |                            |                               |
| security_key                 |                            |                               |
| serialnumber                 |                            |                               |
| session_end_reason           |                            |                               |
| session_owner                |                            |                               |
| sessionid                    |                            |                               |
| sessionid_64                 |                            |                               |
| src_category                 |                            |                               |
| src_dag                      |                            |                               |
| src_edl                      |                            |                               |
| src_host                     |                            |                               |
| src_mac                      |                            |                               |
| src_model                    |                            |                               |
| src_osfamily                 |                            |                               |
| src_osversion                |                            |                               |
| src_profile                  |                            |                               |
| src_uuid                     |                            |                               |
| src_vendor                   |                            |                               |
| start                        |                            |                               |
| subcategory_of_app           |                            |                               |
| tcp_retransit_cnt_c2s        |                            |                               |
| tcp_retransit_cnt_s2c        |                            |                               |
| tcp_rtt_c2s                  |                            |                               |
| tcp_rtt_s2c                  |                            |                               |
| tcp_zero_window_cnt_c2s      |                            |                               |
| tcp_zero_window_cnt_s2c      |                            |                               |
| technology_of_app            |                            |                               |
| time_received                |                            |                               |
| total_n_ooseq_c2s            |                            |                               |
| total_n_ooseq_s2c            |                            |                               |
| traffic_flags                |                            |                               |
| tunnel                       |                            |                               |
| tunneled_app                 |                            |                               |
| tunnelid                     |                            |                               |
| vpc_id                       |                            |                               |
| xff_ip                       |                            |                               |

```json
{
    "action": "$action",
    "action_source": "$action_source",
    "ai_fwd_error": "$ai_fwd_error",
    "ai_traffic": "$ai_traffic",
    "app": "$app",
    "assoc_id": "$assoc_id",
    "bytes": "$bytes",
    "bytes_received": "$bytes_received",
    "bytes_sent": "$bytes_sent",
    "category": "$category",
    "category_of_app": "$category_of_app",
    "characteristic_of_app": "$characteristic_of_app",
    "chunks": "$chunks",
    "chunks_received": "$chunks_received",
    "chunks_sent": "$chunks_sent",
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "dport": "$dport",
    "dst": "$dst",
    "dst_category": "$dst_category",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "dynusergroup_name": "$dynusergroup_name",
    "elapsed": "$elapsed",
    "endpoint_id": "$endpoint_id",
    "flags": "$flags",
    "flow_type": "$flow_type",
    "from": "$from",
    "hostid": "$hostid",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "k8s_cluster_id": "$k8s_cluster_id",
    "link_change_count": "$link_change_count",
    "link_switches": "$link_switches",
    "logset": "$logset",
    "monitortag": "$monitortag",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "ndpmatches": "$ndpmatches",
    "nftrans": "$nftrans",
    "nssai_sd": "$nssai_sd",
    "nssai_sst": "$nssai_sst",
    "nthreats": "$nthreats",
    "nurlcount": "$nurlcount",
    "offloaded": "$offloaded",
    "outbound_if": "$outbound_if",
    "packets": "$packets",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "pkts_received": "$pkts_received",
    "pkts_sent": "$pkts_sent",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "policy_id": "$policy_id",
    "proto": "$proto",
    "repeatcnt": "$repeatcnt",
    "risk_of_app": "$risk_of_app",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "sdwan_cluster": "$sdwan_cluster",
    "sdwan_cluster_type": "$sdwan_cluster_type",
    "sdwan_device_type": "$sdwan_device_type",
    "sdwan_ec_applied": "$sdwan_ec_applied",
    "sdwan_ec_session": "$sdwan_ec_session",
    "sdwan_fec_data": "$sdwan_fec_data",
    "sdwan_fec_ratio": "$sdwan_fec_ratio",
    "sdwan_impacted_link_rx_bytes": "$sdwan_impacted_link_rx_bytes",
    "sdwan_impacted_link_tx_bytes": "$sdwan_impacted_link_tx_bytes",
    "sdwan_impacted_session": "$sdwan_impacted_session",
    "sdwan_link": "$sdwan_link",
    "sdwan_link_rx_bytes": "$sdwan_link_rx_bytes",
    "sdwan_link_tag": "$sdwan_link_tag",
    "sdwan_link_tx_bytes": "$sdwan_link_tx_bytes",
    "sdwan_link_type": "$sdwan_link_type",
    "sdwan_pd_session": "$sdwan_pd_session",
    "sdwan_phyintf": "$sdwan_phyintf",
    "sdwan_session": "$sdwan_session",
    "sdwan_site": "$sdwan_site",
    "security_key": "$security_key",
    "serialnumber": "$serialnumber",
    "session_end_reason": "$session_end_reason",
    "session_owner": "$session_owner",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "sport": "$sport",
    "src": "$src",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "start": "$start",
    "subcategory_of_app": "$subcategory_of_app",
    "tcp_retransit_cnt_c2s": "$tcp_retransit_cnt_c2s",
    "tcp_retransit_cnt_s2c": "$tcp_retransit_cnt_s2c",
    "tcp_rtt_c2s": "$tcp_rtt_c2s",
    "tcp_rtt_s2c": "$tcp_rtt_s2c",
    "tcp_zero_window_cnt_c2s": "$tcp_zero_window_cnt_c2s",
    "tcp_zero_window_cnt_s2c": "$tcp_zero_window_cnt_s2c",
    "technology_of_app": "$technology_of_app",
    "time_received": "$time_received",
    "to": "$to",
    "total_n_ooseq_c2s": "$total_n_ooseq_c2s",
    "total_n_ooseq_s2c": "$total_n_ooseq_s2c",
    "traffic_flags": "$traffic_flags",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
    "tunnelid": "$tunnelid",
    "vpc_id": "$vpc_id",
    "xff_ip": "$xff_ip"
}
```
</br></br>


----
## URL

| Variable                     | Description                | Example Value                 |
| ---------------------------- | -------------------------- | ----------------------------- |
| action                       |                            |                               |
| additional_headers           |                            |                               |
| app                          |                            |                               |
| assoc_id                     |                            |                               |
| category                     |                            |                               |
| category_of_app              |                            |                               |
| cef-number-of-severity       |                            |                               |
| characteristic_of_app        |                            |                               |
| cloud                        |                            |                               |
| cloud_reportid               |                            |                               |
| cluster_name                 |                            |                               |
| container_id                 |                            |                               |
| container_of_app             |                            |                               |
| contenttype                  |                            |                               |
| contentver                   |                            |                               |
| domain_edl                   |                            |                               |
| dst_category                 |                            |                               |
| dst_dag                      |                            |                               |
| dst_edl                      |                            |                               |
| dst_host                     |                            |                               |
| dst_mac                      |                            |                               |
| dst_model                    |                            |                               |
| dst_osfamily                 |                            |                               |
| dst_osversion                |                            |                               |
| dst_profile                  |                            |                               |
| dst_uuid                     |                            |                               |
| dst_vendor                   |                            |                               |
| dynusergroup_name            |                            |                               |
| endpoint_id                  |                            |                               |
| file_url                     |                            |                               |
| filedigest                   |                            |                               |
| filetype                     |                            |                               |
| flags                        |                            |                               |
| flow_type                    |                            |                               |
| hostid                       |                            |                               |
| http2_connection             |                            |                               |
| http2_connection_64          |                            |                               |
| http_headers                 |                            |                               |
| http_method                  |                            |                               |
| is_saas_of_app               |                            |                               |
| justification                |                            |                               |
| k8s_cluster_id               |                            |                               |
| local_deep_learning          |                            |                               |
| logset                       |                            |                               |
| misc                         |                            |                               |
| monitortag                   |                            |                               |
| nssai_sst                    |                            |                               |
| number-of-severity           |                            |                               |
| parent_session_id            |                            |                               |
| parent_session_id_64         |                            |                               |
| parent_start_time            |                            |                               |
| partial_hash                 |                            |                               |
| pcap_id                      |                            |                               |
| pod_name                     |                            |                               |
| pod_namespace                |                            |                               |
| ppid                         |                            |                               |
| reason                       |                            |                               |
| recipient                    |                            |                               |
| referer                      |                            |                               |
| repeatcnt                    |                            |                               |
| reportid                     |                            |                               |
| risk_of_app                  |                            |                               |
| s_decrypted                  |                            |                               |
| s_encrypted                  |                            |                               |
| saas_sid                     |                            |                               |
| saas_sidx                    |                            |                               |
| saas_tenant                  |                            |                               |
| saas_type                    |                            |                               |
| saas_user                    |                            |                               |
| sanctioned_state_of_app      |                            |                               |
| security_key                 |                            |                               |
| sender                       |                            |                               |
| serialnumber                 |                            |                               |
| sessionid                    |                            |                               |
| sessionid_64                 |                            |                               |
| severity                     |                            |                               |
| sig_flags                    |                            |                               |
| src_category                 |                            |                               |
| src_dag                      |                            |                               |
| src_edl                      |                            |                               |
| src_host                     |                            |                               |
| src_mac                      |                            |                               |
| src_model                    |                            |                               |
| src_osfamily                 |                            |                               |
| src_osversion                |                            |                               |
| src_profile                  |                            |                               |
| src_uuid                     |                            |                               |
| src_vendor                   |                            |                               |
| subcategory_of_app           |                            |                               |
| subject                      |                            |                               |
| technology_of_app            |                            |                               |
| thr_category                 |                            |                               |
| threat_name                  |                            |                               |
| threatid                     |                            |                               |
| time_received                |                            |                               |
| tunnel                       |                            |                               |
| tunneled_app                 |                            |                               |
| tunnelid                     |                            |                               |
| url_category_list            |                            |                               |
| url_idx                      |                            |                               |
| user_agent                   |                            |                               |
| vpc_id                       |                            |                               |
| xff                          |                            |                               |
| xff_ip                       |                            |                               |

```json
{
    "action": "$action",
    "additional_headers": "$additional_headers",
    "app": "$app",
    "assoc_id": "$assoc_id",
    "category": "$category",
    "category_of_app": "$category_of_app",
    "cef-number-of-severity": "$cef-number-of-severity",
    "characteristic_of_app": "$characteristic_of_app",
    "cloud": "$cloud",
    "cloud_reportid": "$cloud_reportid",
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "contenttype": "$contenttype",
    "contentver": "$contentver",
    "direction": "$direction",
    "domain_edl": "$domain_edl",
    "dport": "$dport",
    "dst": "$dst",
    "dst_category": "$dst_category",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "dynusergroup_name": "$dynusergroup_name",
    "endpoint_id": "$endpoint_id",
    "file_url": "$file_url",
    "filedigest": "$filedigest",
    "filetype": "$filetype",
    "flags": "$flags",
    "flow_type": "$flow_type",
    "from": "$from",
    "hostid": "$hostid",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "http_headers": "$http_headers",
    "http_method": "$http_method",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "justification": "$justification",
    "k8s_cluster_id": "$k8s_cluster_id",
    "local_deep_learning": "$local_deep_learning",
    "logset": "$logset",
    "misc": "$misc",
    "monitortag": "$monitortag",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "nssai_sst": "$nssai_sst",
    "number-of-severity": "$number-of-severity",
    "outbound_if": "$outbound_if",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "partial_hash": "$partial_hash",
    "pcap_id": "$pcap_id",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "ppid": "$ppid",
    "proto": "$proto",
    "reason": "$reason",
    "recipient": "$recipient",
    "referer": "$referer",
    "repeatcnt": "$repeatcnt",
    "reportid": "$reportid",
    "risk_of_app": "$risk_of_app",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "saas_sid": "$saas_sid",
    "saas_sidx": "$saas_sidx",
    "saas_tenant": "$saas_tenant",
    "saas_type": "$saas_type",
    "saas_user": "$saas_user",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "security_key": "$security_key",
    "sender": "$sender",
    "serialnumber": "$serialnumber",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "severity": "$severity",
    "sig_flags": "$sig_flags",
    "sport": "$sport",
    "src": "$src",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "subcategory_of_app": "$subcategory_of_app",
    "subject": "$subject",
    "technology_of_app": "$technology_of_app",
    "thr_category": "$thr_category",
    "threat_name": "$threat_name",
    "threatid": "$threatid",
    "time_received": "$time_received",
    "to": "$to",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
    "tunnelid": "$tunnelid",
    "url_category_list": "$url_category_list",
    "url_idx": "$url_idx",
    "user_agent": "$user_agent",
    "vpc_id": "$vpc_id",
    "xff": "$xff",
    "xff_ip": "$xff_ip"
}
```
</br></br>

----
## Data

| Variable                   | Description | Example Value |
|----------------------------|-------------|---------------|
| action                     |             |               |
| additional_headers         |             |               |
| app                        |             |               |
| assoc_id                   |             |               |
| category                   |             |               |
| category_of_app            |             |               |
| cef-number-of-severity     |             |               |
| characteristic_of_app      |             |               |
| cloud                      |             |               |
| cloud_reportid             |             |               |
| cluster_name               |             |               |
| container_id               |             |               |
| container_of_app           |             |               |
| contenttype                |             |               |
| contentver                 |             |               |
| domain_edl                 |             |               |
| dst_category               |             |               |
| dst_dag                    |             |               |
| dst_edl                    |             |               |
| dst_host                   |             |               |
| dst_mac                    |             |               |
| dst_model                  |             |               |
| dst_osfamily               |             |               |
| dst_osversion              |             |               |
| dst_profile                |             |               |
| dst_uuid                   |             |               |
| dst_vendor                 |             |               |
| dynusergroup_name          |             |               |
| endpoint_id                |             |               |
| file_url                   |             |               |
| filedigest                 |             |               |
| filetype                   |             |               |
| flags                      |             |               |
| flow_type                  |             |               |
| hostid                     |             |               |
| http2_connection           |             |               |
| http2_connection_64        |             |               |
| http_headers               |             |               |
| http_method                |             |               |
| is_saas_of_app             |             |               |
| justification              |             |               |
| k8s_cluster_id             |             |               |
| local_deep_learning        |             |               |
| logset                     |             |               |
| misc                       |             |               |
| monitortag                 |             |               |
| nssai_sst                  |             |               |
| number-of-severity         |             |               |
| parent_session_id          |             |               |
| parent_session_id_64       |             |               |
| parent_start_time          |             |               |
| partial_hash               |             |               |
| pcap_id                    |             |               |
| pod_name                   |             |               |
| pod_namespace              |             |               |
| ppid                       |             |               |
| reason                     |             |               |
| recipient                  |             |               |
| referer                    |             |               |
| repeatcnt                  |             |               |
| reportid                   |             |               |
| risk_of_app                |             |               |
| s_decrypted                |             |               |
| s_encrypted                |             |               |
| saas_sid                   |             |               |
| saas_sidx                  |             |               |
| saas_tenant                |             |               |
| saas_type                  |             |               |
| saas_user                  |             |               |
| sanctioned_state_of_app    |             |               |
| security_key               |             |               |
| sender                     |             |               |
| serialnumber               |             |               |
| sessionid                  |             |               |
| sessionid_64               |             |               |
| severity                   |             |               |
| sig_flags                  |             |               |
| src_category               |             |               |
| src_dag                    |             |               |
| src_edl                    |             |               |
| src_host                   |             |               |
| src_mac                    |             |               |
| src_model                  |             |               |
| src_osfamily               |             |               |
| src_osversion              |             |               |
| src_profile                |             |               |
| src_uuid                   |             |               |
| src_vendor                 |             |               |
| subcategory_of_app         |             |               |
| subject                    |             |               |
| technology_of_app          |             |               |
| thr_category               |             |               |
| threat_name                |             |               |
| threatid                   |             |               |
| time_received              |             |               |
| tunnel                     |             |               |
| tunneled_app               |             |               |
| tunnelid                   |             |               |
| url_category_list          |             |               |
| url_idx                    |             |               |
| user_agent                 |             |               |
| vpc_id                     |             |               |
| xff                        |             |               |
| xff_ip                     |             |               |

```json
{
    "action": "$action",
    "additional_headers": "$additional_headers",
    "app": "$app",
    "assoc_id": "$assoc_id",
    "category": "$category",
    "category_of_app": "$category_of_app",
    "cef-number-of-severity": "$cef-number-of-severity",
    "characteristic_of_app": "$characteristic_of_app",
    "cloud": "$cloud",
    "cloud_reportid": "$cloud_reportid",
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "contenttype": "$contenttype",
    "contentver": "$contentver",
    "irection": "$irection",
    "domain_edl": "$domain_edl",
    "dport": "$dport",
    "dst": "$dst",
    "dst_category": "$dst_category",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "dynusergroup_name": "$dynusergroup_name",
    "endpoint_id": "$endpoint_id",
    "file_url": "$file_url",
    "filedigest": "$filedigest",
    "filetype": "$filetype",
    "flags": "$flags",
    "flow_type": "$flow_type",
    "from": "$from",
    "hostid": "$hostid",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "http_headers": "$http_headers",
    "http_method": "$http_method",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "justification": "$justification",
    "k8s_cluster_id": "$k8s_cluster_id",
    "local_deep_learning": "$local_deep_learning",
    "logset": "$logset",
    "misc": "$misc",
    "monitortag": "$monitortag",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "nssai_sst": "$nssai_sst",
    "number-of-severity": "$number-of-severity",
    "outbound_if": "$outbound_if",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "partial_hash": "$partial_hash",
    "pcap_id": "$pcap_id",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "ppid": "$ppid",
    "proto": "$proto",
    "reason": "$reason",
    "recipient": "$recipient",
    "referer": "$referer",
    "repeatcnt": "$repeatcnt",
    "reportid": "$reportid",
    "risk_of_app": "$risk_of_app",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "saas_sid": "$saas_sid",
    "saas_sidx": "$saas_sidx",
    "saas_tenant": "$saas_tenant",
    "saas_type": "$saas_type",
    "saas_user": "$saas_user",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "security_key": "$security_key",
    "sender": "$sender",
    "serialnumber": "$serialnumber",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "severity": "$severity",
    "sig_flags": "$sig_flags",
    "sport": "$sport",
    "src": "$src",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "subcategory_of_app": "$subcategory_of_app",
    "subject": "$subject",
    "technology_of_app": "$technology_of_app",
    "thr_category": "$thr_category",
    "threat_name": "$threat_name",
    "threatid": "$threatid",
    "time_received": "$time_received",
    "to": "$to",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
    "tunnelid": "$tunnelid",
    "url_category_list": "$url_category_list",
    "url_idx": "$url_idx",
    "user_agent": "$user_agent",
    "vpc_id": "$vpc_id",
    "xff": "$xff",
    "xff_ip": "$xff_ip"
}
```
</br></br>

----
## WildFire

| Variable                   | Description | Example Value |
|----------------------------|-------------|---------------|
| action                     |             |               |
| additional_headers         |             |               |
| app                        |             |               |
| assoc_id                   |             |               |
| category                   |             |               |
| category_of_app            |             |               |
| cef-number-of-severity     |             |               |
| characteristic_of_app      |             |               |
| cloud                      |             |               |
| cloud_reportid             |             |               |
| cluster_name               |             |               |
| container_id               |             |               |
| container_of_app           |             |               |
| contenttype                |             |               |
| contentver                 |             |               |
| domain_edl                 |             |               |
| dst_category               |             |               |
| dst_dag                    |             |               |
| dst_edl                    |             |               |
| dst_host                   |             |               |
| dst_mac                    |             |               |
| dst_model                  |             |               |
| dst_osfamily               |             |               |
| dst_osversion              |             |               |
| dst_profile                |             |               |
| dst_uuid                   |             |               |
| dst_vendor                 |             |               |
| dynusergroup_name          |             |               |
| endpoint_id                |             |               |
| file_url                   |             |               |
| filedigest                 |             |               |
| filetype                   |             |               |
| flags                      |             |               |
| flow_type                  |             |               |
| hostid                     |             |               |
| http2_connection           |             |               |
| http2_connection_64        |             |               |
| http_headers               |             |               |
| http_method                |             |               |
| is_saas_of_app             |             |               |
| justification              |             |               |
| k8s_cluster_id             |             |               |
| local_deep_learning        |             |               |
| logset                     |             |               |
| misc                       |             |               |
| monitortag                 |             |               |
| nssai_sst                  |             |               |
| number-of-severity         |             |               |
| parent_session_id          |             |               |
| parent_session_id_64       |             |               |
| parent_start_time          |             |               |
| partial_hash               |             |               |
| pcap_id                    |             |               |
| pod_name                   |             |               |
| pod_namespace              |             |               |
| ppid                       |             |               |
| reason                     |             |               |
| recipient                  |             |               |
| referer                    |             |               |
| repeatcnt                  |             |               |
| reportid                   |             |               |
| risk_of_app                |             |               |
| s_decrypted                |             |               |
| s_encrypted                |             |               |
| saas_sid                   |             |               |
| saas_sidx                  |             |               |
| saas_tenant                |             |               |
| saas_type                  |             |               |
| saas_user                  |             |               |
| sanctioned_state_of_app    |             |               |
| security_key               |             |               |
| sender                     |             |               |
| serialnumber               |             |               |
| sessionid                  |             |               |
| sessionid_64               |             |               |
| severity                   |             |               |
| sig_flags                  |             |               |
| src_category               |             |               |
| src_dag                    |             |               |
| src_edl                    |             |               |
| src_host                   |             |               |
| src_mac                    |             |               |
| src_model                  |             |               |
| src_osfamily               |             |               |
| src_osversion              |             |               |
| src_profile                |             |               |
| src_uuid                   |             |               |
| src_vendor                 |             |               |
| subcategory_of_app         |             |               |
| subject                    |             |               |
| technology_of_app          |             |               |
| thr_category               |             |               |
| threat_name                |             |               |
| threatid                   |             |               |
| time_received              |             |               |
| tunnel                     |             |               |
| tunneled_app               |             |               |
| tunnelid                   |             |               |
| url_category_list          |             |               |
| url_idx                    |             |               |
| user_agent                 |             |               |
| vpc_id                     |             |               |
| xff                        |             |               |
| xff_ip                     |             |               |

```json
{
    "action": "$action",
    "additional_headers": "$additional_headers",
    "app": "$app",
    "assoc_id": "$assoc_id",
    "category": "$category",
    "category_of_app": "$category_of_app",
    "cef-number-of-severity": "$cef-number-of-severity",
    "characteristic_of_app": "$characteristic_of_app",
    "cloud": "$cloud",
    "cloud_reportid": "$cloud_reportid",
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "contenttype": "$contenttype",
    "contentver": "$contentver",
    "direction": "$direction",
    "domain_edl": "$domain_edl",
    "dport": "$dport",
    "dst": "$dst",
    "dst_category": "$dst_category",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "dynusergroup_name": "$dynusergroup_name",
    "endpoint_id": "$endpoint_id",
    "file_url": "$file_url",
    "filedigest": "$filedigest",
    "filetype": "$filetype",
    "flags": "$flags",
    "flow_type": "$flow_type",
    "from": "$from",
    "hostid": "$hostid",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "http_headers": "$http_headers",
    "http_method": "$http_method",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "justification": "$justification",
    "k8s_cluster_id": "$k8s_cluster_id",
    "local_deep_learning": "$local_deep_learning",
    "logset": "$logset",
    "misc": "$misc",
    "monitortag": "$monitortag",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "nssai_sst": "$nssai_sst",
    "number-of-severity": "$number-of-severity",
    "outbound_if": "$outbound_if",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "partial_hash": "$partial_hash",
    "pcap_id": "$pcap_id",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "ppid": "$ppid",
    "proto": "$proto",
    "reason": "$reason",
    "recipient": "$recipient",
    "referer": "$referer",
    "repeatcnt": "$repeatcnt",
    "reportid": "$reportid",
    "risk_of_app": "$risk_of_app",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "saas_sid": "$saas_sid",
    "saas_sidx": "$saas_sidx",
    "saas_tenant": "$saas_tenant",
    "saas_type": "$saas_type",
    "saas_user": "$saas_user",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "security_key": "$security_key",
    "sender": "$sender",
    "serialnumber": "$serialnumber",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "severity": "$severity",
    "sig_flags": "$sig_flags",
    "sport": "$sport",
    "src": "$src",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "subcategory_of_app": "$subcategory_of_app",
    "subject": "$subject",
    "technology_of_app": "$technology_of_app",
    "thr_category": "$thr_category",
    "threat_name": "$threat_name",
    "threatid": "$threatid",
    "time_received": "$time_received",
    "to": "$to",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
    "tunnelid": "$tunnelid",
    "url_category_list": "$url_category_list",
    "url_idx": "$url_idx",
    "user_agent": "$user_agent",
    "vpc_id": "$vpc_id",
    "xff": "$xff",
    "xff_ip": "$xff_ip"
}
```
</br></br>

----
## Tunnel

| Variable                | Description | Example Value |
|-------------------------|-------------|---------------|
| action                  |             |               |
| action_source           |             |               |
| app                     |             |               |
| bytes                   |             |               |
| bytes_received          |             |               |
| bytes_sent              |             |               |
| category                |             |               |
| category_of_app         |             |               |
| characteristic_of_app   |             |               |
| cluster_name            |             |               |
| container_id            |             |               |
| container_of_app        |             |               |
| dst_dag                 |             |               |
| dst_edl                 |             |               |
| dst_uuid                |             |               |
| dynusergroup_name       |             |               |
| elapsed                 |             |               |
| endpoint_id             |             |               |
| flags                   |             |               |
| is_saas_of_app          |             |               |
| k8s_cluster_id          |             |               |
| logset                  |             |               |
| max_encap               |             |               |
| monitortag              |             |               |
| nssai_sd                |             |               |
| nssai_sst               |             |               |
| packets                 |             |               |
| parent_session_id       |             |               |
| parent_session_id_64    |             |               |
| parent_start_time       |             |               |
| pcap                    |             |               |
| pcap_id                 |             |               |
| pdu_session_id          |             |               |
| pkts_received           |             |               |
| pkts_sent               |             |               |
| pod_name                |             |               |
| pod_namespace           |             |               |
| repeatcnt               |             |               |
| risk_of_app             |             |               |
| s_decrypted             |             |               |
| s_encrypted             |             |               |
| sanctioned_state_of_app |             |               |
| security_key            |             |               |
| session_end_reason      |             |               |
| sessionid               |             |               |
| sessionid_64            |             |               |
| sessions_closed         |             |               |
| sessions_created        |             |               |
| src_dag                 |             |               |
| src_edl                 |             |               |
| src_uuid                |             |               |
| start                   |             |               |
| strict_check            |             |               |
| subcategory_of_app      |             |               |
| technology_of_app       |             |               |
| time_received           |             |               |
| traffic_flags           |             |               |
| tunnel                  |             |               |
| tunnel_fragment         |             |               |
| tunnel_insp_rule        |             |               |
| tunneled_app            |             |               |
| tunnelid                |             |               |
| unknown_proto           |             |               |
| vpc_id                  |             |               |

</br></br>

```json
{
    "action": "$action",
    "action_source": "$action_source",
    "app": "$app",
    "bytes": "$bytes",
    "bytes_received": "$bytes_received",
    "bytes_sent": "$bytes_sent",
    "category": "$category",
    "category_of_app": "$category_of_app",
    "characteristic_of_app": "$characteristic_of_app",
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "dport": "$dport",
    "dst": "$dst",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_uuid": "$dst_uuid",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "dynusergroup_name": "$dynusergroup_name",
    "elapsed": "$elapsed",
    "endpoint_id": "$endpoint_id",
    "flags": "$flags",
    "from": "$from",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "k8s_cluster_id": "$k8s_cluster_id",
    "logset": "$logset",
    "max_encap": "$max_encap",
    "monitortag": "$monitortag",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "nssai_sd": "$nssai_sd",
    "nssai_sst": "$nssai_sst",
    "outbound_if": "$outbound_if",
    "packets": "$packets",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "pcap": "$pcap",
    "pcap_id": "$pcap_id",
    "pdu_session_id": "$pdu_session_id",
    "pkts_received": "$pkts_received",
    "pkts_sent": "$pkts_sent",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "proto": "$proto",
    "repeatcnt": "$repeatcnt",
    "risk_of_app": "$risk_of_app",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "security_key": "$security_key",
    "session_end_reason": "$session_end_reason",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "sessions_closed": "$sessions_closed",
    "sessions_created": "$sessions_created",
    "sport": "$sport",
    "src": "$src",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_uuid": "$src_uuid",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "start": "$start",
    "strict_check": "$strict_check",
    "subcategory_of_app": "$subcategory_of_app",
    "technology_of_app": "$technology_of_app",
    "time_received": "$time_received",
    "to": "$to",
    "traffic_flags": "$traffic_flags",
    "tunnel": "$tunnel",
    "tunnel_fragment": "$tunnel_fragment",
    "tunnel_insp_rule": "$tunnel_insp_rule",
    "tunneled_app": "$tunneled_app",
    "tunnelid": "$tunnelid",
    "unknown_proto": "$unknown_proto",
    "vpc_id": "$vpc_id"
}
```
</br></br>


----
## Decryption

| Variable                | Description | Example Value |
|-------------------------|-------------|---------------|
| action                  |             |               |
| app                     |             |               |
| category_of_app         |             |               |
| cert_flags              |             |               |
| cert_serial             |             |               |
| cert_size               |             |               |
| cert_ver                |             |               |
| chain_status            |             |               |
| characteristic_of_app   |             |               |
| cluster_name            |             |               |
| cn                      |             |               |
| cn_len                  |             |               |
| container_id            |             |               |
| container_of_app        |             |               |
| dst_category            |             |               |
| dst_dag                 |             |               |
| dst_edl                 |             |               |
| dst_host                |             |               |
| dst_mac                 |             |               |
| dst_model               |             |               |
| dst_osfamily            |             |               |
| dst_osversion           |             |               |
| dst_profile             |             |               |
| dst_uuid                |             |               |
| dst_vendor              |             |               |
| ec_curve                |             |               |
| endpoint_id             |             |               |
| err_index               |             |               |
| error                   |             |               |
| fingerprint             |             |               |
| flags                   |             |               |
| hs_stage_c2f            |             |               |
| hs_stage_f2s            |             |               |
| is_saas_of_app          |             |               |
| issuer_cn               |             |               |
| issuer_len              |             |               |
| k8s_cluster_id          |             |               |
| logset                  |             |               |
| notafter                |             |               |
| notbefore               |             |               |
| pod_name                |             |               |
| pod_namespace           |             |               |
| policy_name             |             |               |
| proxy_type              |             |               |
| repeatcnt               |             |               |
| risk_of_app             |             |               |
| root_cn                 |             |               |
| root_status             |             |               |
| rootcn_len              |             |               |
| s_decrypted             |             |               |
| s_encrypted             |             |               |
| sanctioned_state_of_app |             |               |
| security_key            |             |               |
| sessionid               |             |               |
| sessionid_64            |             |               |
| sni                     |             |               |
| sni_len                 |             |               |
| src_category            |             |               |
| src_dag                 |             |               |
| src_edl                 |             |               |
| src_host                |             |               |
| src_mac                 |             |               |
| src_model               |             |               |
| src_osfamily            |             |               |
| src_osversion           |             |               |
| src_profile             |             |               |
| src_uuid                |             |               |
| src_vendor              |             |               |
| subcategory_of_app      |             |               |
| technology_of_app       |             |               |
| time_generated          |             |               |
| time_received           |             |               |
| tls_auth                |             |               |
| tls_enc                 |             |               |
| tls_keyxchg             |             |               |
| tls_version             |             |               |
| tunnel                  |             |               |
| tunneled_app            |             |               |
| vpc_id                  |             |               |

</br></br>

```json
{
    "action": "$action",
    "app": "$app",
    "category_of_app": "$category_of_app",
    "cert_flags": "$cert_flags",
    "cert_serial": "$cert_serial",
    "cert_size": "$cert_size",
    "cert_ver": "$cert_ver",
    "chain_status": "$chain_status",
    "characteristic_of_app": "$characteristic_of_app",
    "cluster_name": "$cluster_name",
    "cn": "$cn",
    "cn_len": "$cn_len",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "dport": "$dport",
    "dst": "$dst",
    "dst_category": "$dst_category",
    "dst_dag": "$dst_dag",
    "dst_edl": "$dst_edl",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_uuid": "$dst_uuid",
    "dst_vendor": "$dst_vendor",
    "dstloc": "$dstloc",
    "dstuser": "$dstuser",
    "ec_curve": "$ec_curve",
    "endpoint_id": "$endpoint_id",
    "err_index": "$err_index",
    "error": "$error",
    "fingerprint": "$fingerprint",
    "flags": "$flags",
    "from": "$from",
    "hs_stage_c2f": "$hs_stage_c2f",
    "hs_stage_f2s": "$hs_stage_f2s",
    "inbound_if": "$inbound_if",
    "is_saas_of_app": "$is_saas_of_app",
    "issuer_cn": "$issuer_cn",
    "issuer_len": "$issuer_len",
    "k8s_cluster_id": "$k8s_cluster_id",
    "logset": "$logset",
    "natdport": "$natdport",
    "natdst": "$natdst",
    "natsport": "$natsport",
    "natsrc": "$natsrc",
    "notafter": "$notafter",
    "notbefore": "$notbefore",
    "outbound_if": "$outbound_if",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "policy_name": "$policy_name",
    "proto": "$proto",
    "proxy_type": "$proxy_type",
    "repeatcnt": "$repeatcnt",
    "risk_of_app": "$risk_of_app",
    "root_cn": "$root_cn",
    "root_status": "$root_status",
    "rootcn_len": "$rootcn_len",
    "rule": "$rule",
    "rule_uuid": "$rule_uuid",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "sanctioned_state_of_app": "$sanctioned_state_of_app",
    "security_key": "$security_key",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "sni": "$sni",
    "sni_len": "$sni_len",
    "sport": "$sport",
    "src": "$src",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_edl": "$src_edl",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_uuid": "$src_uuid",
    "src_vendor": "$src_vendor",
    "srcloc": "$srcloc",
    "srcuser": "$srcuser",
    "subcategory_of_app": "$subcategory_of_app",
    "technology_of_app": "$technology_of_app",
    "time_generated": "$time_generated",
    "time_received": "$time_received",
    "tls_auth": "$tls_auth",
    "tls_enc": "$tls_enc",
    "tls_keyxchg": "$tls_keyxchg",
    "tls_version": "$tls_version",
    "to": "$to",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
    "vpc_id": "$vpc_id"
}
```
</br></br>


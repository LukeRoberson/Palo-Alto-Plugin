# Traffic Payloads

This page is for log types that are based on traffic. These include:
* Traffic
* Tunnel
* Decryption

For other types, see **payload.md** and **threat_payloads.md**.
</br></br>



# Common Fields

There are many fields which are common to all these types of alerts.

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
| category_of_app          | Application category                         | networking    |
| characteristic_of_app    | App characteristics                          |               |
| is_saas_of_app           | '1' if this is a SaaS app                    |               |
| risk_of_app              | Application risk                             |               |
| sanctioned_state_of_app  | '1' is app is sanctioned                     | no            |
| subcategory_of_app       | Application subcategory                      |               |
| technology_of_app        | Application technology                       | browser-based |
| tunnel                   | Tunnel type (GRE/IPSec)                      | N/A           |
| tunneled_app             | Tunneled application                         | web-browsing  |
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
    "technology_of_app": "$technology_of_app",
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
| repeatcnt                | Sessions with the same match in 5 sec        |               |
| sessionid                | Unique session number                        |               |
| sessionid_64             |                                              |               |
| src_dag                  | Source dynamic address group                 |               |
</br></br>


```json
{
    "dst_dag": "$dst_dag",
    "flags": "$flags",
    "repeatcnt": "$repeatcnt",
    "sessionid": "$sessionid",
    "sessionid_64": "$sessionid_64",
    "src_dag": "$src_dag"
}
```
</br></br>


### Actions

| Variable                 | Description                                  | Example Value |
|--------------------------|----------------------------------------------|---------------|
| action                   | Action taken on the session                  | reset-both    |
| logset                   | Applied log forwarding profile               |               |
</br></br>


```json
{
    "action": "$action",
    "logset": "$logset"
}
```
</br></br>



### Other

| Variable                     | Description                                        | Example Value                 |
|------------------------------|----------------------------------------------------|-------------------------------|
| cluster_name                 |                                                    |                               |
| container_id                 | Kubernetes container ID where VM FW resides        |                               |
| container_of_app             | The parent application for an application.         |                               |
| dst_edl                      | EDL containing the destination IP                  |                               |
| dst_uuid                     | Destination VM UUID                                |                               |
| endpoint_id                  |                                                    |                               |
| k8s_cluster_id               |                                                    |                               |
| pod_name                     | The application POD being secured                  |                               |
| pod_namespace                | The namespace of the application POD being secured |                               |
| s_decrypted                  |                                                    |                               |
| s_encrypted                  |                                                    |                               |
| security_key                 |                                                    |                               |
| src_edl                      | EDL containting the source IP                      |                               |
| src_uuid                     | Source VM UUID                                     |                               |
| time_received                |                                                    |                               |
| vpc_id                       |                                                    |                               |
</br></br>


```json
{
    "cluster_name": "$cluster_name",
    "container_id": "$container_id",
    "container_of_app": "$container_of_app",
    "dst_edl": "$dst_edl",
    "dst_uuid": "$dst_uuid",
    "endpoint_id": "$endpoint_id",
    "k8s_cluster_id": "$k8s_cluster_id",
    "pod_name": "$pod_name",
    "pod_namespace": "$pod_namespace",
    "s_decrypted": "$s_decrypted",
    "s_encrypted": "$s_encrypted",
    "security_key": "$security_key",
    "src_edl": "$src_edl",
    "src_uuid": "$src_uuid",
    "time_received": "$time_received",
    "vpc_id": "$vpc_id",
}
```
</br></br>




----
## Traffic

| Variable                     | Description                                          | Example Value                 |
| ---------------------------- | ---------------------------------------------------- | ----------------------------- |
| action_source                | Whether the allow/block comes from the app or policy | from-policy                   |
| ai_fwd_error                 |                                                      |                               |
| ai_traffic                   |                                                      |                               |
| assoc_id                     | SCTP Association ID                                  |                               |
| bytes                        | Total bytes in the session                           | 48120                         |
| bytes_received               | Bytes in s2c direction                               | 6345                          |
| bytes_sent                   | Bytes in c2s direction                               | 41775                         |
| category                     | app category                                         | computer-and-internet-info    |
| chunks                       | SCTP Chunks                                          |                               |
| chunks_received              | SCTP Chunks Received                                 |                               |
| chunks_sent                  | SCTP Chunks Sent                                     |                               |
| dst_category                 | Device-ID: Category                                  |                               |
| dst_host                     | Device-ID: Hostname                                  |                               |
| dst_mac                      | Device-ID: MAC address                               |                               |
| dst_model                    | Device-ID: Model                                     |                               |
| dst_osfamily                 | Device-ID: OS family                                 |                               |
| dst_osversion                | Device-ID: OS version                                |                               |
| dst_profile                  | Device-ID: Profile                                   |                               |
| dst_vendor                   | Device-ID: Vendor                                    |                               |
| dynusergroup_name            | Dynamic user group of the user                       |                               |
| elapsed                      | Elapsed time of the session                          |                               |
| flow_type                    |                                                      |                               |
| hostid                       |                                                      |                               |
| http2_connection             | HTTP/2 session ID                                    |                               |
| http2_connection_64          |                                                      |                               |
| link_change_count            | Number of link flaps during the session              |                               |
| link_switches                | Embedded details of up to four link flap entries     |                               |
| monitortag                   |                                                      |                               |
| ndpmatches                   |                                                      |                               |
| nftrans                      |                                                      |                               |
| nssai_sd                     | A Slice Differentiator (5G)                          |                               |
| nssai_sst                    | A Slice Service Type (5G)                            |                               |
| nthreats                     |                                                      |                               |
| nurlcount                    |                                                      |                               |
| offloaded                    | '1' if the traffic was offloaded                     |                               |
| packets                      | Number of total packets for the session              | 65                            |
| parent_session_id            | ID of the session in which this is tunnelled         |                               |
| parent_session_id_64         |                                                      |                               |
| parent_start_time            | Time parent tunnel session began                     |                               |
| pkts_received                | Number of s2c packets                                | 26                            |
| pkts_sent                    | Number of c2s packets                                | 39                            |
| policy_id                    | Name of the SD-WAN policy                            |                               |
| sdwan_cluster                | SD-WAN: Cluster name                                 |                               |
| sdwan_cluster_type           | SD-WAN: Cluster type                                 |                               |
| sdwan_device_type            | SD-WAN: Type of device                               |                               |
| sdwan_ec_applied             |                                                      |                               |
| sdwan_ec_session             |                                                      |                               |
| sdwan_fec_data               |                                                      |                               |
| sdwan_fec_ratio              |                                                      |                               |
| sdwan_impacted_link_rx_bytes |                                                      |                               |
| sdwan_impacted_link_tx_bytes |                                                      |                               |
| sdwan_impacted_session       |                                                      |                               |
| sdwan_link                   |                                                      |                               |
| sdwan_link_rx_bytes          |                                                      |                               |
| sdwan_link_tag               |                                                      |                               |
| sdwan_link_tx_bytes          |                                                      |                               |
| sdwan_link_type              |                                                      |                               |
| sdwan_pd_session             |                                                      |                               |
| sdwan_phyintf                |                                                      |                               |
| sdwan_session                |                                                      |                               |
| sdwan_site                   | SD-WAN: Name of the site                             |                               |
| serialnumber                 | Serial number of the users device                    |                               |
| session_end_reason           | The reason the session was terminated                | tcp-rst-from-client           |
| session_owner                | The original HA peer session owner                   |                               |
| src_category                 | Device-ID: Category                                  |                               |
| src_host                     | Device-ID: Hostname                                  |                               |
| src_mac                      | Device-ID: MAC address                               |                               |
| src_model                    | Device-ID: Model                                     |                               |
| src_osfamily                 | Device-ID: OS Family                                 |                               |
| src_osversion                | Device-ID: OS Version                                |                               |
| src_profile                  | Device-ID: Profile                                   |                               |
| src_vendor                   | Device-ID: Vendor                                    |                               |
| start                        | Time of the session start                            |                               |
| tcp_retransit_cnt_c2s        |                                                      |                               |
| tcp_retransit_cnt_s2c        |                                                      |                               |
| tcp_rtt_c2s                  |                                                      |                               |
| tcp_rtt_s2c                  |                                                      |                               |
| tcp_zero_window_cnt_c2s      |                                                      |                               |
| tcp_zero_window_cnt_s2c      |                                                      |                               |
| total_n_ooseq_c2s            |                                                      |                               |
| total_n_ooseq_s2c            |                                                      |                               |
| traffic_flags                |                                                      |                               |
| tunnelid                     | IMSI number (cellular)                               |                               |
| xff_ip                       | X-Forwarded-For header                               |                               |



```json
{
    "action_source": "$action_source",
    "ai_fwd_error": "$ai_fwd_error",
    "ai_traffic": "$ai_traffic",
    "assoc_id": "$assoc_id",
    "bytes": "$bytes",
    "bytes_received": "$bytes_received",
    "bytes_sent": "$bytes_sent",
    "category": "$category",
    "chunks": "$chunks",
    "chunks_received": "$chunks_received",
    "chunks_sent": "$chunks_sent",
    "dst_category": "$dst_category",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_vendor": "$dst_vendor",
    "dynusergroup_name": "$dynusergroup_name",
    "elapsed": "$elapsed",
    "flow_type": "$flow_type",
    "hostid": "$hostid",
    "http2_connection": "$http2_connection",
    "http2_connection_64": "$http2_connection_64",
    "link_change_count": "$link_change_count",
    "link_switches": "$link_switches",
    "logset": "$logset",
    "monitortag": "$monitortag",
    "ndpmatches": "$ndpmatches",
    "nftrans": "$nftrans",
    "nssai_sd": "$nssai_sd",
    "nssai_sst": "$nssai_sst",
    "nthreats": "$nthreats",
    "nurlcount": "$nurlcount",
    "offloaded": "$offloaded",
    "packets": "$packets",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "pkts_received": "$pkts_received",
    "pkts_sent": "$pkts_sent",
    "policy_id": "$policy_id",
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
    "serialnumber": "$serialnumber",
    "session_end_reason": "$session_end_reason",
    "session_owner": "$session_owner",
    "src_category": "$src_category",
    "src_dag": "$src_dag",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_vendor": "$src_vendor",
    "start": "$start",
    "subcategory_of_app": "$subcategory_of_app",
    "tcp_retransit_cnt_c2s": "$tcp_retransit_cnt_c2s",
    "tcp_retransit_cnt_s2c": "$tcp_retransit_cnt_s2c",
    "tcp_rtt_c2s": "$tcp_rtt_c2s",
    "tcp_rtt_s2c": "$tcp_rtt_s2c",
    "tcp_zero_window_cnt_c2s": "$tcp_zero_window_cnt_c2s",
    "tcp_zero_window_cnt_s2c": "$tcp_zero_window_cnt_s2c",
    "total_n_ooseq_c2s": "$total_n_ooseq_c2s",
    "total_n_ooseq_s2c": "$total_n_ooseq_s2c",
    "traffic_flags": "$traffic_flags",
    "tunnelid": "$tunnelid",
    "xff_ip": "$xff_ip"
}
```
</br></br>



----
## Tunnel

| Variable                | Description                                          | Example Value              |
|-------------------------|------------------------------------------------------|----------------------------|
| action_source           | Whether the allow/block comes from policy or the app |                            |
| bytes                   | Total byte count                                     |                            |
| bytes_received          | Bytes received (s2c)                                 |                            |
| bytes_sent              | Bytes send (c2s)                                     |                            |
| category                | URL or wildfire verdict                              | URL-Whitelist              |
| dynusergroup_name       | The user's dynamic group                             |               |
| elapsed                 | Session time                                         |               |
| max_encap               | Packets dropped due to max encap levels exceeded     |               |
| monitortag              |                                                      |               |
| nssai_sd                | The A Slice Differentiator (5G)                      |               |
| nssai_sst               | A Slice Service Type of the Network Slice ID (5G)    |               |
| packets                 | Total packets sent/received                          |               |
| parent_session_id       | ID of the session in which this is tunnelled         |               |
| parent_session_id_64    |                                                      |               |
| parent_start_time       | Time parent tunnel session began                     |               |
| pcap_id                 | ID of the PCAP file                                  |               |
| pdu_session_id          | Session ID for L4 segments inside a tunnel           |               |
| pkts_received           |                                                      |               |
| pkts_sent               |                                                      |               |
| session_end_reason      | The reason a session terminated                      |               |
| sessions_closed         | Number of completed/closed sessions created          |               |
| sessions_created        | Number of inner sessions created                     |               |
| start                   | Start time of the session                            |               |
| strict_check            | packets dropped due to tunnel protocol header        |               |
| traffic_flags           |                                                      |               |
| tunnel_fragment         | Number of packets dropped because of fragmentation   |               |
| tunnel_insp_rule        | Tunnel inspection rule matching cleartext traffic    |               |
| tunnelid                | IMSI ID (cellular)                                   |               |
| unknown_proto           | Packets dropped due to unknown protocol              |               |

</br></br>

```json
{
    "action_source": "$action_source",
    "bytes": "$bytes",
    "bytes_received": "$bytes_received",
    "bytes_sent": "$bytes_sent",
    "category": "$category",
    "dynusergroup_name": "$dynusergroup_name",
    "elapsed": "$elapsed",
    "max_encap": "$max_encap",
    "monitortag": "$monitortag",
    "nssai_sd": "$nssai_sd",
    "nssai_sst": "$nssai_sst",
    "packets": "$packets",
    "parent_session_id": "$parent_session_id",
    "parent_session_id_64": "$parent_session_id_64",
    "parent_start_time": "$parent_start_time",
    "pcap": "$pcap",
    "pcap_id": "$pcap_id",
    "pdu_session_id": "$pdu_session_id",
    "pkts_received": "$pkts_received",
    "pkts_sent": "$pkts_sent",
    "session_end_reason": "$session_end_reason",
    "sessions_closed": "$sessions_closed",
    "sessions_created": "$sessions_created",
    "start": "$start",
    "strict_check": "$strict_check",
    "traffic_flags": "$traffic_flags",
    "tunnel_fragment": "$tunnel_fragment",
    "tunnel_insp_rule": "$tunnel_insp_rule",
    "tunnelid": "$tunnelid",
    "unknown_proto": "$unknown_proto",
}
```
</br></br>


----
## Decryption

| Variable                | Description                              | Example Value |
|-------------------------|------------------------------------------|---------------|
| cert_flags              | Flags containing cert information        |               |
| cert_serial             | The unique identifier of the certificate |               |
| cert_size               | The certificate key size                 |               |
| cert_ver                | The certificate version                  |               |
| chain_status            | Whether the chain is trusted             |               |
| cn                      | Common Name                              |               |
| cn_len                  | CN Length                                |               |
| contentver              | App and Threats verion                   |               |
| dst_category            | Device-ID: Category                      |               |
| dst_host                | Device-ID: Hostname                      |               |
| dst_mac                 | Device-ID: MAC address                   |               |
| dst_model               | Device-ID: Model                         |               |
| dst_osfamily            | Device-ID: OS family                     |               |
| dst_osversion           | Device-ID: OS version                    |               |
| dst_profile             | Device-ID: Profile                       |               |
| dst_vendor              | Device-ID: Vendor                        |               |
| ec_curve                | Elliptic Curve                           |               |
| err_index               | The type of error that occurred          |               |
| error                   | The error that has occurred in the event |               |
| fingerprint             | Certificate fingerprint                  |               |
| hs_stage_c2f            | Stage for Client to Firewall             |               |
| hs_stage_f2s            | Stage for Firewall to Server             |               |
| issuer_cn               | Issuer CN                                |               |
| issuer_len              | Issuer CN length                         |               |
| notafter                | Cert validity end                        |               |
| notbefore               | Cert validity start                      |               |
| policy_name             | The policy name that was encountered     |               |
| proxy_type              | Decryption proxy type                    |               |
| root_cn                 | CN of the root cert                      |               |
| root_status             | Root cert status (trusted, etc)          |               |
| rootcn_len              | Length of the root CN                    |               |
| sni                     | Server Name Indication                   |               |
| sni_len                 | SNI (hostname) length                    |               |
| src_category            | Device-ID: Category                      |               |
| src_host                | Device-ID: Hostname                      |               |
| src_mac                 | Device-ID: MAC address                   |               |
| src_model               | Device-ID: Model                         |               |
| src_osfamily            | Device-ID: OS Family                     |               |
| src_osversion           | Device-ID: OS Version                    |               |
| src_profile             | Device-ID: Profile                       |               |
| src_vendor              | Device-ID: Vendor                        |               |
| tls_auth                | The authentication algorithm             |               |
| tls_enc                 | The encryption algorithm                 |               |
| tls_keyxchg             | The key exchange algorithm               |               |
| tls_version             | The version of TLS protocol              |               |

</br></br>

```json
{
    "action": "$action",
    "cert_flags": "$cert_flags",
    "cert_serial": "$cert_serial",
    "cert_size": "$cert_size",
    "cert_ver": "$cert_ver",
    "chain_status": "$chain_status",
    "cn": "$cn",
    "cn_len": "$cn_len",
    "contentver": "$contentver",
    "dst_category": "$dst_category",
    "dst_host": "$dst_host",
    "dst_mac": "$dst_mac",
    "dst_model": "$dst_model",
    "dst_osfamily": "$dst_osfamily",
    "dst_osversion": "$dst_osversion",
    "dst_profile": "$dst_profile",
    "dst_vendor": "$dst_vendor",
    "ec_curve": "$ec_curve",
    "err_index": "$err_index",
    "error": "$error",
    "fingerprint": "$fingerprint",
    "hs_stage_c2f": "$hs_stage_c2f",
    "hs_stage_f2s": "$hs_stage_f2s",
    "issuer_cn": "$issuer_cn",
    "issuer_len": "$issuer_len",
    "notafter": "$notafter",
    "notbefore": "$notbefore",
    "policy_name": "$policy_name",
    "proxy_type": "$proxy_type",
    "root_cn": "$root_cn",
    "root_status": "$root_status",
    "rootcn_len": "$rootcn_len",
    "sni": "$sni",
    "sni_len": "$sni_len",
    "src_category": "$src_category",
    "src_host": "$src_host",
    "src_mac": "$src_mac",
    "src_model": "$src_model",
    "src_osfamily": "$src_osfamily",
    "src_osversion": "$src_osversion",
    "src_profile": "$src_profile",
    "src_vendor": "$src_vendor",
    "time_generated": "$time_generated",
    "tls_auth": "$tls_auth",
    "tls_enc": "$tls_enc",
    "tls_keyxchg": "$tls_keyxchg",
    "tls_version": "$tls_version",
    "tunnel": "$tunnel",
    "tunneled_app": "$tunneled_app",
}
```
</br></br>


----
# Field Values
## Subtypes

**Traffic** subtypes can be:

* Start - session started
* End - session ended
* Drop - session dropped before the application is identified and there is no rule that allows the session.
* Deny - session dropped after the application is identified and there is a rule to block or no rule that allows the session.

</br></br>


## Actions

The _action_ field in a **Traffic** log can be:

* allow - session was allowed by policy
* deny - session was denied by policy
* drop - session was dropped silently
* drop ICMP - session was silently dropped with an ICMP unreachable message to the host or application
* reset both - session was terminated and a TCP reset is sent to both the sides of the connection
* reset client - session was terminated and a TCP reset is sent to the client
* reset server - session was terminated and a TCP reset is sent to the server

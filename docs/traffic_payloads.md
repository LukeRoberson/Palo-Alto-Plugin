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
| category_of_app          | Application category                         |               |
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
    "src_dag": "$src_dag",
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
    "logset": "$logset",
}
```
</br></br>



### Other

| Variable                     | Description                | Example Value                 |
|------------------------------|----------------------------|-------------------------------|
| cluster_name                 |                            |                               |
| container_id                 |                            |                               |
| container_of_app             |                            |                               |
| dst_edl                      |                            |                               |
| dst_uuid                     |                            |                               |
| endpoint_id                  |                            |                               |
| k8s_cluster_id               |                            |                               |
| pod_name                     |                            |                               |
| pod_namespace                |                            |                               |
| s_decrypted                  |                            |                               |
| s_encrypted                  |                            |                               |
| security_key                 |                            |                               |
| src_edl                      |                            |                               |
| src_uuid                     |                            |                               |
| time_received                |                            |                               |
| vpc_id                       |                            |                               |
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

| Variable                     | Description                                  | Example Value                 |
| ---------------------------- | -------------------------------------------- | ----------------------------- |
| action_source                |                                              |                               |
| ai_fwd_error                 |                                              |                               |
| ai_traffic                   |                                              |                               |
| assoc_id                     |                                              |                               |
| bytes                        |                                              |                               |
| bytes_received               |                                              |                               |
| bytes_sent                   |                                              |                               |
| category                     | URL or wildfire verdict                      | computer-and-internet-info    |
| chunks                       |                                              |                               |
| chunks_received              |                                              |                               |
| chunks_sent                  |                                              |                               |
| dst_category                 |                                              |                               |
| dst_host                     |                                              |                               |
| dst_mac                      |                                              |                               |
| dst_model                    |                                              |                               |
| dst_osfamily                 |                                              |                               |
| dst_osversion                |                                              |                               |
| dst_profile                  |                                              |                               |
| dst_vendor                   |                                              |                               |
| dynusergroup_name            |                                              |                               |
| elapsed                      |                                              |                               |
| flow_type                    |                                              |                               |
| hostid                       |                                              |                               |
| http2_connection             | HTTP/2 session ID                            |                               |
| http2_connection_64          |                                              |                               |
| link_change_count            |                                              |                               |
| link_switches                |                                              |                               |
| monitortag                   |                                              |                               |
| ndpmatches                   |                                              |                               |
| nftrans                      |                                              |                               |
| nssai_sd                     |                                              |                               |
| nssai_sst                    |                                              |                               |
| nthreats                     |                                              |                               |
| nurlcount                    |                                              |                               |
| offloaded                    |                                              |                               |
| packets                      |                                              |                               |
| parent_session_id            | ID of the session in which this is tunnelled |                               |
| parent_session_id_64         |                                              |                               |
| parent_start_time            | Time parent tunnel session began             |                               |
| pkts_received                |                                              |                               |
| pkts_sent                    |                                              |                               |
| policy_id                    |                                              |                               |
| sdwan_cluster                |                                              |                               |
| sdwan_cluster_type           |                                              |                               |
| sdwan_device_type            |                                              |                               |
| sdwan_ec_applied             |                                              |                               |
| sdwan_ec_session             |                                              |                               |
| sdwan_fec_data               |                                              |                               |
| sdwan_fec_ratio              |                                              |                               |
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
| serialnumber                 |                            |                               |
| session_end_reason           |                            |                               |
| session_owner                |                            |                               |
| src_category                 |                            |                               |
| src_host                     |                            |                               |
| src_mac                      |                            |                               |
| src_model                    |                            |                               |
| src_osfamily                 |                            |                               |
| src_osversion                |                            |                               |
| src_profile                  |                            |                               |
| src_vendor                   |                            |                               |
| start                        |                            |                               |
| tcp_retransit_cnt_c2s        |                            |                               |
| tcp_retransit_cnt_s2c        |                            |                               |
| tcp_rtt_c2s                  |                            |                               |
| tcp_rtt_s2c                  |                            |                               |
| tcp_zero_window_cnt_c2s      |                            |                               |
| tcp_zero_window_cnt_s2c      |                            |                               |
| total_n_ooseq_c2s            |                            |                               |
| total_n_ooseq_s2c            |                            |                               |
| traffic_flags                |                            |                               |
| tunnelid                     |                            |                               |
| xff_ip                       | X-Forwarded-For header     |                               |



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

| Variable                | Description                                  | Example Value              |
|-------------------------|----------------------------------------------|----------------------------|
| action_source           |                                              |                            |
| bytes                   |                                              |                            |
| bytes_received          |                                              |                            |
| bytes_sent              |                                              |                            |
| category                | URL or wildfire verdict                      | computer-and-internet-info |
| dynusergroup_name       |                                              |               |
| elapsed                 |                                              |               |
| max_encap               |                                              |               |
| monitortag              |                                              |               |
| nssai_sd                |                                              |               |
| nssai_sst               |                                              |               |
| packets                 |                                              |               |
| parent_session_id       | ID of the session in which this is tunnelled |               |
| parent_session_id_64    |                                              |               |
| parent_start_time       | Time parent tunnel session began             |               |
| pcap                    |                                              |               |
| pcap_id                 | ID of the PCAP file                          |               |
| pdu_session_id          |                                              |               |
| pkts_received           |                                              |               |
| pkts_sent               |                                              |               |
| session_end_reason      |                                              |               |
| sessions_closed         |                                              |               |
| sessions_created        |                                              |               |
| start                   |                                              |               |
| strict_check            |                                              |               |
| subcategory_of_app      |                                              |               |
| traffic_flags           |                                              |               |
| tunnel_fragment         |                                              |               |
| tunnel_insp_rule        |                                              |               |
| tunnelid                |                                              |               |
| unknown_proto           |                                              |               |

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

| Variable                | Description            | Example Value |
|-------------------------|------------------------|---------------|
| cert_flags              |                        |               |
| cert_serial             |                        |               |
| cert_size               |                        |               |
| cert_ver                |                        |               |
| chain_status            |                        |               |
| cn                      |                        |               |
| cn_len                  |                        |               |
| contentver              | App and Threats verion |               |
| dst_category            |                        |               |
| dst_host                |             |               |
| dst_mac                 |             |               |
| dst_model               |             |               |
| dst_osfamily            |             |               |
| dst_osversion           |             |               |
| dst_profile             |             |               |
| dst_vendor              |             |               |
| ec_curve                |             |               |
| err_index               |             |               |
| error                   |             |               |
| fingerprint             |             |               |
| hs_stage_c2f            |             |               |
| hs_stage_f2s            |             |               |
| issuer_cn               |             |               |
| issuer_len              |             |               |
| notafter                |             |               |
| notbefore               |             |               |
| policy_name             |             |               |
| proxy_type              |             |               |
| root_cn                 |             |               |
| root_status             |             |               |
| rootcn_len              |             |               |
| sni                     |             |               |
| sni_len                 |             |               |
| src_category            |             |               |
| src_host                |             |               |
| src_mac                 |             |               |
| src_model               |             |               |
| src_osfamily            |             |               |
| src_osversion           |             |               |
| src_profile             |             |               |
| src_vendor              |             |               |
| time_generated          |             |               |
| tls_auth                |             |               |
| tls_enc                 |             |               |
| tls_keyxchg             |             |               |
| tls_version             |             |               |

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


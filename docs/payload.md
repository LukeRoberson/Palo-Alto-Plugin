# Payload Fields

On the Palo Alto, the webhook message is customizable. The **payload** section of each log type has various variables that can be used.

Variables are referenced by a leading dollar-sign. They can be included in the message body, headers, or parameters.

When sending these in a JSON body, the variable still needs to be inside double-quotes. For example:

```json
{
    "admin": "$admin"
}
```
</br></br>


## Common Fields

These fields are available to all log types:

| Variable                     | Description                | Example Value                 |
| ---------------------------- | -------------------------- | ----------------------------- |
| actionflags                  |                            | 0x8000000000                  |
| cef-formatted-receive_time   | Timestamp in CEF format    | Jun 20 2025 05:22:38 GMT      |
| cef-formatted-time_generated | Timestamp in CEF format    | Jun 20 2025 05:22:37 GMT      |
| device_name                  | The name of the firewall   | PM-8-0-VM                     |
| dg_hier_level_1              |                            |                               |
| dg_hier_level_2              |                            |                               |
| dg_hier_level_3              |                            |                               |
| dg_hier_level_4              |                            |                               |
| high_res_timestamp           | Timestamp in milliseconds  | 1970-01-01T10:00:00.000+10:00 |
| receive_time                 | Simple timestamp           | 2025/06/20 15:22:38           |
| sender_sw_version            | PANOS version              | 11.2.5                        |
| seqno                        |                            |                               |
| serial                       | Hardware serial number     | 7200002624                    |
| subtype                      |                            |                               |
| time_generated               | Simple timestamp           | 2025/06/20 15:22:37           |
| type                         |                            | CONFIG                        |
| vsys                         |                            |                               |
| vsys_id                      | ID of the Virtual System   |                               |
| vsys_name                    | Name of the Virtual System |                               |
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


| Variable                     | Description                | Example Value                 |
| ---------------------------- | -------------------------- | ----------------------------- |
| admin                        | Admin user name            | test                          |
| after-change-detail          |                            |                               |
| before-change-detail         |                            |                               |
| client                       |                            |                               |
| cmd                          |                            |                               |
| comment                      | Commit comment             | test comment                  |
| dg_id                        |                            |                               |
| full-path                    |                            |                               |
| host                         |                            |                               |
| path                         |                            |                               |
| result                       | Result of commit           | Succeeded                     |
| tpl_id                       |                            |                               |
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

----
## System

| Variable                     | Description                | Example Value                 |
| ---------------------------- | -------------------------- | ----------------------------- |
| cef-number-of-severity       |                            |                               |
| device_type                  |                            |                               |
| dg_id                        |                            |                               |
| eventid                      |                            |                               |
| module                       |                            |                               |
| number-of-severity           |                            |                               |
| object                       |                            |                               |
| opaque                       |                            |                               |
| sdwan_cluster                |                            |                               |
| sdwan_site                   |                            |                               |
| severity                     |                            |                               |
| tpl_id                       |                            |                               |
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


----
## Threat

| Variable                 | Description | Example Value |
|--------------------------|-------------|---------------|
| action                   |             |               |
| additional_headers       |             |               |
| app                      |             |               |
| assoc_id                 |             |               |
| category                 |             |               |
| category_of_app          |             |               |
| cef-number-of-severity   |             |               |
| characteristic_of_app    |             |               |
| cloud                    |             |               |
| cloud_reportid           |             |               |
| cluster_name             |             |               |
| container_id             |             |               |
| container_of_app         |             |               |
| contenttype              |             |               |
| contentver               |             |               |
| direction                |             |               |
| domain_edl               |             |               |
| dport                    |             |               |
| dst                      |             |               |
| dst_category             |             |               |
| dst_dag                  |             |               |
| dst_edl                  |             |               |
| dst_host                 |             |               |
| dst_mac                  |             |               |
| dst_model                |             |               |
| dst_osfamily             |             |               |
| dst_osversion            |             |               |
| dst_profile              |             |               |
| dst_uuid                 |             |               |
| dst_vendor               |             |               |
| dstloc                   |             |               |
| dstuser                  |             |               |
| dynusergroup_name        |             |               |
| endpoint_id              |             |               |
| file_url                 |             |               |
| filedigest               |             |               |
| filetype                 |             |               |
| flags                    |             |               |
| flow_type                |             |               |
| from                     |             |               |
| hostid                   |             |               |
| http2_connection         |             |               |
| http2_connection_64      |             |               |
| http_headers             |             |               |
| http_method              |             |               |
| inbound_if               |             |               |
| is_saas_of_app           |             |               |
| justification            |             |               |
| k8s_cluster_id           |             |               |
| local_deep_learning      |             |               |
| logset                   |             |               |
| misc                     |             |               |
| monitortag               |             |               |
| natdport                 |             |               |
| natdst                   |             |               |
| natsport                 |             |               |
| natsrc                   |             |               |
| nssai_sst                |             |               |
| number-of-severity       |             |               |
| outbound_if              |             |               |
| parent_session_id        |             |               |
| parent_session_id_64     |             |               |
| parent_start_time        |             |               |
| partial_hash             |             |               |
| pcap_id                  |             |               |
| pod_name                 |             |               |
| pod_namespace            |             |               |
| ppid                     |             |               |
| proto                    |             |               |
| reason                   |             |               |
| recipient                |             |               |
| referer                  |             |               |
| repeatcnt                |             |               |
| reportid                 |             |               |
| risk_of_app              |             |               |
| rule                     |             |               |
| rule_uuid                |             |               |
| s_decrypted              |             |               |
| s_encrypted              |             |               |
| saas_sid                 |             |               |
| saas_sidx                |             |               |
| saas_tenant              |             |               |
| saas_type                |             |               |
| saas_user                |             |               |
| sanctioned_state_of_app  |             |               |
| security_key             |             |               |
| sender                   |             |               |
| serialnumber             |             |               |
| sessionid                |             |               |
| sessionid_64             |             |               |
| severity                 |             |               |
| sig_flags                |             |               |
| sport                    |             |               |
| src                      |             |               |
| src_category             |             |               |
| src_dag                  |             |               |
| src_edl                  |             |               |
| src_host                 |             |               |
| src_mac                  |             |               |
| src_model                |             |               |
| src_osfamily             |             |               |
| src_osversion            |             |               |
| src_profile              |             |               |
| src_uuid                 |             |               |
| src_vendor               |             |               |
| srcloc                   |             |               |
| srcuser                  |             |               |
| subcategory_of_app       |             |               |
| subject                  |             |               |
| technology_of_app        |             |               |
| thr_category             |             |               |
| threat_name              |             |               |
| threatid                 |             |               |
| time_received            |             |               |
| to                       |             |               |
| tunnel                   |             |               |
| tunneled_app             |             |               |
| tunnelid                 |             |               |
| url_category_list        |             |               |
| url_idx                  |             |               |
| user_agent               |             |               |
| vpc_id                   |             |               |
| xff                      |             |               |
| xff_ip                   |             |               |

</br></br>

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
    "number-of-severity": "$number-of-severity"
}

{
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
    "url_category_list": "$url_category_list"
}

{
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
| dport                        |                            |                               |
| dst                          |                            |                               |
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
| dstloc                       |                            |                               |
| dstuser                      |                            |                               |
| dynusergroup_name            |                            |                               |
| elapsed                      |                            |                               |
| endpoint_id                  |                            |                               |
| flags                        |                            |                               |
| flow_type                    |                            |                               |
| from                         |                            |                               |
| hostid                       |                            |                               |
| http2_connection             |                            |                               |
| http2_connection_64          |                            |                               |
| inbound_if                   |                            |                               |
| is_saas_of_app               |                            |                               |
| k8s_cluster_id               |                            |                               |
| link_change_count            |                            |                               |
| link_switches                |                            |                               |
| logset                       |                            |                               |
| monitortag                   |                            |                               |
| natdport                     |                            |                               |
| natdst                       |                            |                               |
| natsport                     |                            |                               |
| natsrc                       |                            |                               |
| ndpmatches                   |                            |                               |
| nftrans                      |                            |                               |
| nssai_sd                     |                            |                               |
| nssai_sst                    |                            |                               |
| nthreats                     |                            |                               |
| nurlcount                    |                            |                               |
| offloaded                    |                            |                               |
| outbound_if                  |                            |                               |
| packets                      |                            |                               |
| parent_session_id            |                            |                               |
| parent_session_id_64         |                            |                               |
| parent_start_time            |                            |                               |
| pkts_received                |                            |                               |
| pkts_sent                    |                            |                               |
| pod_name                     |                            |                               |
| pod_namespace                |                            |                               |
| policy_id                    |                            |                               |
| proto                        |                            |                               |
| repeatcnt                    |                            |                               |
| risk_of_app                  |                            |                               |
| rule                         |                            |                               |
| rule_uuid                    |                            |                               |
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
| sport                        |                            |                               |
| src                          |                            |                               |
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
| srcloc                       |                            |                               |
| srcuser                      |                            |                               |
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
| to                           |                            |                               |
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
    "offloaded": "$offloaded"
}

{
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
    "src_model": "$src_model"
}

{
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
| direction                    |                            |                               |
| domain_edl                   |                            |                               |
| dport                        |                            |                               |
| dst                          |                            |                               |
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
| dstloc                       |                            |                               |
| dstuser                      |                            |                               |
| dynusergroup_name            |                            |                               |
| endpoint_id                  |                            |                               |
| file_url                     |                            |                               |
| filedigest                   |                            |                               |
| filetype                     |                            |                               |
| flags                        |                            |                               |
| flow_type                    |                            |                               |
| from                         |                            |                               |
| hostid                       |                            |                               |
| http2_connection             |                            |                               |
| http2_connection_64          |                            |                               |
| http_headers                 |                            |                               |
| http_method                  |                            |                               |
| inbound_if                   |                            |                               |
| is_saas_of_app               |                            |                               |
| justification                |                            |                               |
| k8s_cluster_id               |                            |                               |
| local_deep_learning          |                            |                               |
| logset                       |                            |                               |
| misc                         |                            |                               |
| monitortag                   |                            |                               |
| natdport                     |                            |                               |
| natdst                       |                            |                               |
| natsport                     |                            |                               |
| natsrc                       |                            |                               |
| nssai_sst                    |                            |                               |
| number-of-severity           |                            |                               |
| outbound_if                  |                            |                               |
| parent_session_id            |                            |                               |
| parent_session_id_64         |                            |                               |
| parent_start_time            |                            |                               |
| partial_hash                 |                            |                               |
| pcap_id                      |                            |                               |
| pod_name                     |                            |                               |
| pod_namespace                |                            |                               |
| ppid                         |                            |                               |
| proto                        |                            |                               |
| reason                       |                            |                               |
| recipient                    |                            |                               |
| referer                      |                            |                               |
| repeatcnt                    |                            |                               |
| reportid                     |                            |                               |
| risk_of_app                  |                            |                               |
| rule                         |                            |                               |
| rule_uuid                    |                            |                               |
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
| sport                        |                            |                               |
| src                          |                            |                               |
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
| srcloc                       |                            |                               |
| srcuser                      |                            |                               |
| subcategory_of_app           |                            |                               |
| subject                      |                            |                               |
| technology_of_app            |                            |                               |
| thr_category                 |                            |                               |
| threat_name                  |                            |                               |
| threatid                     |                            |                               |
| time_received                |                            |                               |
| to                           |                            |                               |
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
    "number-of-severity": "$number-of-severity"
}

{
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
    "url_category_list": "$url_category_list"
}

{
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
| irection                   |             |               |
| domain_edl                 |             |               |
| dport                      |             |               |
| dst                        |             |               |
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
| dstloc                     |             |               |
| dstuser                    |             |               |
| dynusergroup_name          |             |               |
| endpoint_id                |             |               |
| file_url                   |             |               |
| filedigest                 |             |               |
| filetype                   |             |               |
| flags                      |             |               |
| flow_type                  |             |               |
| from                       |             |               |
| hostid                     |             |               |
| http2_connection           |             |               |
| http2_connection_64        |             |               |
| http_headers               |             |               |
| http_method                |             |               |
| inbound_if                 |             |               |
| is_saas_of_app             |             |               |
| justification              |             |               |
| k8s_cluster_id             |             |               |
| local_deep_learning        |             |               |
| logset                     |             |               |
| misc                       |             |               |
| monitortag                 |             |               |
| natdport                   |             |               |
| natdst                     |             |               |
| natsport                   |             |               |
| natsrc                     |             |               |
| nssai_sst                  |             |               |
| number-of-severity         |             |               |
| outbound_if                |             |               |
| parent_session_id          |             |               |
| parent_session_id_64       |             |               |
| parent_start_time          |             |               |
| partial_hash               |             |               |
| pcap_id                    |             |               |
| pod_name                   |             |               |
| pod_namespace              |             |               |
| ppid                       |             |               |
| proto                      |             |               |
| reason                     |             |               |
| recipient                  |             |               |
| referer                    |             |               |
| repeatcnt                  |             |               |
| reportid                   |             |               |
| risk_of_app                |             |               |
| rule                       |             |               |
| rule_uuid                  |             |               |
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
| sport                      |             |               |
| src                        |             |               |
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
| srcloc                     |             |               |
| srcuser                    |             |               |
| subcategory_of_app         |             |               |
| subject                    |             |               |
| technology_of_app          |             |               |
| thr_category               |             |               |
| threat_name                |             |               |
| threatid                   |             |               |
| time_received              |             |               |
| to                         |             |               |
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
    "number-of-severity": "$number-of-severity"
}

{
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
    "url_category_list": "$url_category_list"
}

{
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
| direction                  |             |               |
| domain_edl                 |             |               |
| dport                      |             |               |
| dst                        |             |               |
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
| dstloc                     |             |               |
| dstuser                    |             |               |
| dynusergroup_name          |             |               |
| endpoint_id                |             |               |
| file_url                   |             |               |
| filedigest                 |             |               |
| filetype                   |             |               |
| flags                      |             |               |
| flow_type                  |             |               |
| from                       |             |               |
| hostid                     |             |               |
| http2_connection           |             |               |
| http2_connection_64        |             |               |
| http_headers               |             |               |
| http_method                |             |               |
| inbound_if                 |             |               |
| is_saas_of_app             |             |               |
| justification              |             |               |
| k8s_cluster_id             |             |               |
| local_deep_learning        |             |               |
| logset                     |             |               |
| misc                       |             |               |
| monitortag                 |             |               |
| natdport                   |             |               |
| natdst                     |             |               |
| natsport                   |             |               |
| natsrc                     |             |               |
| nssai_sst                  |             |               |
| number-of-severity         |             |               |
| outbound_if                |             |               |
| parent_session_id          |             |               |
| parent_session_id_64       |             |               |
| parent_start_time          |             |               |
| partial_hash               |             |               |
| pcap_id                    |             |               |
| pod_name                   |             |               |
| pod_namespace              |             |               |
| ppid                       |             |               |
| proto                      |             |               |
| reason                     |             |               |
| recipient                  |             |               |
| referer                    |             |               |
| repeatcnt                  |             |               |
| reportid                   |             |               |
| risk_of_app                |             |               |
| rule                       |             |               |
| rule_uuid                  |             |               |
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
| sport                      |             |               |
| src                        |             |               |
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
| srcloc                     |             |               |
| srcuser                    |             |               |
| subcategory_of_app         |             |               |
| subject                    |             |               |
| technology_of_app          |             |               |
| thr_category               |             |               |
| threat_name                |             |               |
| threatid                   |             |               |
| time_received              |             |               |
| to                         |             |               |
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
    "number-of-severity": "$number-of-severity"
}

{
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
    "url_category_list": "$url_category_list"
}

{
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
| dport                   |             |               |
| dst                     |             |               |
| dst_dag                 |             |               |
| dst_edl                 |             |               |
| dst_uuid                |             |               |
| dstloc                  |             |               |
| dstuser                 |             |               |
| dynusergroup_name       |             |               |
| elapsed                 |             |               |
| endpoint_id             |             |               |
| flags                   |             |               |
| from                    |             |               |
| inbound_if              |             |               |
| is_saas_of_app          |             |               |
| k8s_cluster_id          |             |               |
| logset                  |             |               |
| max_encap               |             |               |
| monitortag              |             |               |
| natdport                |             |               |
| natdst                  |             |               |
| natsport                |             |               |
| natsrc                  |             |               |
| nssai_sd                |             |               |
| nssai_sst               |             |               |
| outbound_if             |             |               |
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
| proto                   |             |               |
| repeatcnt               |             |               |
| risk_of_app             |             |               |
| rule                    |             |               |
| rule_uuid               |             |               |
| s_decrypted             |             |               |
| s_encrypted             |             |               |
| sanctioned_state_of_app |             |               |
| security_key            |             |               |
| session_end_reason      |             |               |
| sessionid               |             |               |
| sessionid_64            |             |               |
| sessions_closed         |             |               |
| sessions_created        |             |               |
| sport                   |             |               |
| src                     |             |               |
| src_dag                 |             |               |
| src_edl                 |             |               |
| src_uuid                |             |               |
| srcloc                  |             |               |
| srcuser                 |             |               |
| start                   |             |               |
| strict_check            |             |               |
| subcategory_of_app      |             |               |
| technology_of_app       |             |               |
| time_received           |             |               |
| to                      |             |               |
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
    "sessionid": "$sessionid"
}

{
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
## Authentication

| Variable         | Description | Example Value |
|------------------|-------------|---------------|
| authid           |             |               |
| authpolicy       |             |               |
| authproto        |             |               |
| clienttype       |             |               |
| cluster_name     |             |               |
| desc             |             |               |
| event            |             |               |
| factorno         |             |               |
| ip               |             |               |
| logset           |             |               |
| normalize_user   |             |               |
| object           |             |               |
| region           |             |               |
| repeatcnt        |             |               |
| rule_uuid        |             |               |
| serverprofile    |             |               |
| sessionid        |             |               |
| src_category     |             |               |
| src_host         |             |               |
| src_mac          |             |               |
| src_model        |             |               |
| src_osfamily     |             |               |
| src_osversion    |             |               |
| src_profile      |             |               |
| src_vendor       |             |               |
| user             |             |               |
| user_agent       |             |               |
| vendor           |             |               |

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

| Variable             | Description | Example Value |
|----------------------|-------------|---------------|
| beginport            |             |               |
| cluster_name         |             |               |
| datasource           |             |               |
| datasourcename       |             |               |
| datasourcetype       |             |               |
| direction            |             |               |
| endport              |             |               |
| eventid              |             |               |
| factorcompletiontime |             |               |
| factorno             |             |               |
| factortype           |             |               |
| ip                   |             |               |
| origindatasource     |             |               |
| repeatcnt            |             |               |
| tag_name             |             |               |
| timeout              |             |               |
| ugflags              |             |               |
| user                 |             |               |
| userbysource         |             |               |

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

----
## HIP Match

| Variable     | Description | Example Value |
|--------------|-------------|---------------|
| cluster_name |             |               |
| hostid       |             |               |
| mac          |             |               |
| machinename  |             |               |
| matchname    |             |               |
| matchtype    |             |               |
| os           |             |               |
| reclassified |             |               |
| repeatcnt    |             |               |
| serialnumber |             |               |
| src          |             |               |
| srcipv6      |             |               |
| srcuser      |             |               |
| subtype      |             |               |

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
    "subtype": "$subtype"
}
```
</br></br>

----
## Globalprotect

| Variable           | Description | Example Value |
|--------------------|-------------|---------------|
| attempted_gateways |             |               |
| auth_method        |             |               |
| client_os          |             |               |
| client_os_ver      |             |               |
| client_ver         |             |               |
| cluster_name       |             |               |
| connect_method     |             |               |
| error              |             |               |
| error_code         |             |               |
| eventid            |             |               |
| gateway            |             |               |
| hostid             |             |               |
| location           |             |               |
| login_duration     |             |               |
| machinename        |             |               |
| opaque             |             |               |
| portal             |             |               |
| priority           |             |               |
| private_ip         |             |               |
| private_ipv6       |             |               |
| project_name       |             |               |
| public_ip          |             |               |
| public_ipv6        |             |               |
| reason             |             |               |
| repeatcnt          |             |               |
| response_time      |             |               |
| selection_type     |             |               |
| serialnumber       |             |               |
| srcregion          |             |               |
| srcuser            |             |               |
| stage              |             |               |
| status             |             |               |
| tunnel_type        |             |               |

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

----
## Iptag

| Variable           | Description | Example Value |
|--------------------|-------------|---------------|
| cluster_name       |             |               |
| datasource_subtype |             |               |
| datasource_type    |             |               |
| datasourcename     |             |               |
| event_id           |             |               |
| ip                 |             |               |
| ip_subnet_range    |             |               |
| repeatcnt          |             |               |
| tag_name           |             |               |
| timeout            |             |               |

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
| dport                   |             |               |
| dst                     |             |               |
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
| dstloc                  |             |               |
| dstuser                 |             |               |
| ec_curve                |             |               |
| endpoint_id             |             |               |
| err_index               |             |               |
| error                   |             |               |
| fingerprint             |             |               |
| flags                   |             |               |
| from                    |             |               |
| hs_stage_c2f            |             |               |
| hs_stage_f2s            |             |               |
| inbound_if              |             |               |
| is_saas_of_app          |             |               |
| issuer_cn               |             |               |
| issuer_len              |             |               |
| k8s_cluster_id          |             |               |
| logset                  |             |               |
| natdport                |             |               |
| natdst                  |             |               |
| natsport                |             |               |
| natsrc                  |             |               |
| notafter                |             |               |
| notbefore               |             |               |
| outbound_if             |             |               |
| pod_name                |             |               |
| pod_namespace           |             |               |
| policy_name             |             |               |
| proto                   |             |               |
| proxy_type              |             |               |
| repeatcnt               |             |               |
| risk_of_app             |             |               |
| root_cn                 |             |               |
| root_status             |             |               |
| rootcn_len              |             |               |
| rule                    |             |               |
| rule_uuid               |             |               |
| s_decrypted             |             |               |
| s_encrypted             |             |               |
| sanctioned_state_of_app |             |               |
| security_key            |             |               |
| sessionid               |             |               |
| sessionid_64            |             |               |
| sni                     |             |               |
| sni_len                 |             |               |
| sport                   |             |               |
| src                     |             |               |
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
| srcloc                  |             |               |
| srcuser                 |             |               |
| subcategory_of_app      |             |               |
| technology_of_app       |             |               |
| time_generated          |             |               |
| time_received           |             |               |
| tls_auth                |             |               |
| tls_enc                 |             |               |
| tls_keyxchg             |             |               |
| tls_version             |             |               |
| to                      |             |               |
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
    "rule_uuid": "$rule_uuid"
}

{
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


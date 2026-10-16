---
description: A monitoring collector, store or view is chosen for the cluster.
dependencies: []
---

## Monitoring systems

A monitoring system has a collector on each host, a store, and a view with alerts; Prometheus-format parts can be swapped one for another. Measured on Ouranos, one host, about 1,280 series: Beszel agent 16 MB, node_exporter 18 MB, Zabbix agent 2 21 MB, Beszel hub 32 MB, VictoriaMetrics 50 to 67 MB, Prometheus 90 to 96 MB, Telegraf above 166 MB. Netdata states 100 to 350 MB per host and needs root. Prometheus and node_exporter belong to the CNCF under Apache 2.0; VictoriaMetrics to a self-funded company under Apache 2.0; Beszel to one author under MIT, before 1.0; Grafana and Zabbix moved to AGPL; Netdata's newer dashboard is proprietary.

Attribution: Core supplied these measurements and findings; this module does not claim an independent reproduction or measurements on other hosts.

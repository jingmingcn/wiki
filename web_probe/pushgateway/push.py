from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()

g_probe_network_up = Gauge('probe_network_up', 'Network Connection Status, 1 as ok, 0 as failed', registry=registry)
g_probe_network_up.set(1)

g_probe_dns_resolve_seconds = Gauge('probe_dns_resolve_seconds', 'DNS Resolve Time Cost', registry=registry)
g_probe_dns_resolve_seconds.set(0.001)

g_probe_queueing_seconds = Gauge('probe_queueing_seconds', 'Queueing Time Cost', registry=registry)
g_probe_queueing_seconds.set(0.001)

g_probe_waiting_seconds = Gauge('probe_waiting_seconds','Wating Time Cost', registry=registry)
g_probe_waiting_seconds.set(0.0001)

g_probe_network_transmit_speed_bytes = Gauge('probe_network_transmit_speed_bytes', 'Network Transmit Speed', registry=registry)
g_probe_network_transmit_speed_bytes.set(1000000)

push_to_gateway('10.1.2.32:9091', job='web_probe', grouping_key={"instance":"www.163.com:80"},registry=registry)
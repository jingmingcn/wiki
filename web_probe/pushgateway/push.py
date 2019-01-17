from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
g = Gauge('web_probe_network_traffic_speed_down', 'Network Tracffic Speed Download', registry=registry)
g.set(3290)
push_to_gateway('10.1.2.32:9091', job='web_probe', grouping_key={"instance":"some_instance"},registry=registry)

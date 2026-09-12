# grafana-dashboards

Grafana dashboards as JSON, exported from Grafana 5/6 era and still importable
today.

| Dashboard | Needs |
|---|---|
| alertmanager.json | Prometheus + Alertmanager metrics |
| blackbox-ping.json | Prometheus + blackbox exporter |
| cadvisor.json | Prometheus + cAdvisor |
| elasticsearch_wms.json | Prometheus + Elasticsearch exporter |
| grafana-server.json | Prometheus + Grafana metrics |
| infiniband.json | Prometheus + node exporter (InfiniBand collector) |
| node-metrics.json | Prometheus + node exporter |
| usgs-earthquakes_rev2.json | [grafana-worldmap-panel](https://grafana.com/grafana/plugins/grafana-worldmap-panel/) plugin |

## Import

Via the UI (Dashboards > New > Import) or the API:

```bash
curl -u admin:admin -X POST http://localhost:3000/api/dashboards/db \
  -H 'Content-Type: application/json' \
  -d "{\"dashboard\": $(cat alertmanager.json), \"overwrite\": true}"
```

## Notes

- `schemaVersion` is kept as exported so Grafana runs its own on-load migrations
  (for example `singlestat` panels become `stat` when the dashboard is opened and
  saved in the UI). Do not bump it by hand.

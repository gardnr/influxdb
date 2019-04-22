InfluxDB exporter

[Documentation](https://influxdb-python.readthedocs.io/en/latest/)

```
python3 -m pip install -r requirements.txt

gardnr add driver influxdb influxdb.driver:InfluxDB \
    -c host=localhost \
    -c port=8086 \
    -c username=root \
    -c password=root \
    -c database=metrics
```

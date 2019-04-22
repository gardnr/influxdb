from influxdb import InfluxDBClient

from gardnr import constants, drivers


class InfluxDB(drivers.Exporter):
    blacklist = [constants.Metrics.IMAGE]

    def setup(self):
        self.client = InfluxDBClient(self.host,
                                     self.port,
                                     self.username,
                                     self.password,
                                     self.database)

    def export(self, logs):
        json_body = []

        for log in logs:
            json_body.append({
                'measurement': log.metric.name,
                'time': log.timestamp.isoformat(),
                'fields': {
                    'value': log.value
                }
            })

        self.client.write_points(json_body)

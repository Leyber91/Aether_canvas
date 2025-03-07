import time

class Metrics:
    def __init__(self):
        self.metrics_data = {}

    def record_metric(self, name, value):
        self.metrics_data.setdefault(name, []).append(value)

    def start_timer(self, name):
        self.metrics_data[name] = time.time()

    def end_timer(self, name):
        if name in self.metrics_data:
            elapsed_time = time.time() - self.metrics_data.pop(name)
            self.record_metric(name, elapsed)

    def increment_counter(self, name, increment=1):
        current = self.metrics_data.get(name, 0)
        self.metrics_data[name] = current + increment

    def get_metrics_report(self):
        return self.metrics_data

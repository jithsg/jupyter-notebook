import mlflow
from mlflow import log_metric
from random import choice
mlflow.set_tracking_uri("http://127.0.0.1:5000")
metric_names = ["cpu", "memory", "disk"]
percentages = [i for i in range(0, 100)]

if __name__ == "__main__":
    with mlflow.start_run():
        for i in range(40):
            log_metric(choice(metric_names), choice(percentages)) 
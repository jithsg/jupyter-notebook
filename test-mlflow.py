import mlflow
import os
mlflow.set_tracking_uri("http://127.0.0.1:5000")

if __name__ == "__main__":
    # Start a new MLflow run
    with mlflow.start_run():
        mlflow.log_param("threshold", 5)
        mlflow.log_metric("timestamp", 0.001) 

        # Ensure the artifact file exists before logging
        file_path = "nba.csv"
        if os.path.exists(file_path):
            mlflow.log_artifact(file_path)
        else:
            print(f"File {file_path} does not exist. Unable to log artifact.")

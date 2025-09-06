from mlops.pipelines.training.stub_training import stub_training_pipeline

if __name__ == "__main__":
    p = stub_training_pipeline()
    print("Stub training pipeline completed. Check ./mlruns for MLflow logs!")
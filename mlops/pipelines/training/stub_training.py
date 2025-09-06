from zenml import pipeline, step
import mlflow

@step
def ingest_data_step() -> dict:
    return {"n_samples": 42}

@step
def validate_data_step(ingested: dict) -> dict:
    #pretend DeepChecks passed
    return {"validated": True, **ingested}

@step
def train_step(validated: dict) -> dict:
    #log dummy metric/artifact to mlFlow
    mlflow.set_experiment("real-or-fake")
    with mlflow.start_run(run_name="dummy_run"):
        mlflow.log_param("model_name", "stub")
        mlflow.log_metric("val_accuracy", 0.50)
        mlflow.log_text("hello world", "notes.txt")
        mlflow.set_tag("candidate", "false")
    return {"model_uri": "stub://model", **validated}

@step 
def evaluate_step(trained: dict) -> dict:
    return {"auc": 0.75, "precision": 0.70, "recall": 0.65, **trained}

@step
def register_step(evaluated: dict) -> str:
    #no real registry yet, return pretend version
    return "stub-v0"

@pipeline
def stub_training_pipeline():
    i = ingest_data_step()
    v = validate_data_step(i)
    t = train_step(v)
    e = evaluate_step(t)
    register_step(e)

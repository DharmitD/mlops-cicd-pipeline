import kfp
import argparse
import json


def run_pipeline(pipeline_path, endpoint, branch):
    client = kfp.Client(host=endpoint)
    experiment = client.create_experiment(name="MLOps Experiment")

    run = client.run_pipeline(
        experiment_id=experiment.id,
        job_name=f"mlops-run-{branch}",
        pipeline_package_path=pipeline_path
    )

    print(f"✅ Pipeline run started: {run.id}")

    # Wait for completion & fetch metrics
    run_detail = client.wait_for_run_completion(run.id, timeout=600)
    metrics = json.dumps(run_detail.run.metrics, indent=2)
    print(f"📊 Metrics: {metrics}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", required=True, help="Path to KFP YAML file")
    parser.add_argument("--endpoint", required=True, help="Kubeflow Pipelines Endpoint")
    parser.add_argument("--branch", required=True, help="Git branch name for tracking")
    args = parser.parse_args()

    run_pipeline(args.pipeline, args.endpoint, args.branch)

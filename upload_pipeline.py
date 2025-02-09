import kfp
import argparse

def upload_pipeline(pipeline_path, endpoint):
    client = kfp.Client(host=endpoint)
    pipeline_name = "MLOps-CI-Pipeline"
    client.upload_pipeline(pipeline_path, pipeline_name=pipeline_name)
    print(f"✅ Uploaded {pipeline_name} to {endpoint}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pipeline", required=True, help="Path to KFP YAML file")
    parser.add_argument("--endpoint", required=True, help="Kubeflow Pipelines Endpoint")
    args = parser.parse_args()

    upload_pipeline(args.pipeline, args.endpoint)

from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-0817205254",
}

dag = DAG(
    "hello_world-0817205254",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_326350e8_1751_4ab2_a494_6183de3ad68f = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="ariflow",
    cos_directory="hello_world-0817205254",
    cos_dependencies_archive="hello-326350e8-1751-4ab2-a494-6183de3ad68f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="https://quay.io/repository/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_326350e8_1751_4ab2_a494_6183de3ad68f.image_pull_policy = "IfNotPresent"


notebook_op_226fbce5_1288_492a_abf8_a24d2a7668ae = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="ariflow",
    cos_directory="hello_world-0817205254",
    cos_dependencies_archive="world-226fbce5-1288-492a-abf8-a24d2a7668ae.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="https://quay.io/repository/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_226fbce5_1288_492a_abf8_a24d2a7668ae.image_pull_policy = "IfNotPresent"

(
    notebook_op_226fbce5_1288_492a_abf8_a24d2a7668ae
    << notebook_op_326350e8_1751_4ab2_a494_6183de3ad68f
)

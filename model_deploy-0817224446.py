from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-0817224446",
}

dag = DAG(
    "model_deploy-0817224446",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_e66c5e4e_5e26_4870_ade3_2be226c0631b = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="ariflow",
    cos_directory="model_deploy-0817224446",
    cos_dependencies_archive="build_push_image-e66c5e4e-5e26-4870-ade3-2be226c0631b.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "https://index.docker.io/v1/",
        "CONTAINER_REGISTRY_USER": "webmakaka",
        "CONTAINER_REGISTRY_PASSWORD": "Fgjrfkbgcbc11",
        "CONTAINER_DETAILS": "webmakaka/mlflowdemo:latest",
    },
    config_file="None",
    dag=dag,
)

notebook_op_e66c5e4e_5e26_4870_ade3_2be226c0631b.image_pull_policy = "IfNotPresent"


notebook_op_021933e9_680a_425d_930e_4954e33ead37 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="ariflow",
    cos_directory="model_deploy-0817224446",
    cos_dependencies_archive="deploy_model-021933e9-680a-425d-930e-4954e33ead37.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAILS": "webmakaka/mlflowdemo:latest",
        "CLUSTER_DOMAIN_NAME": "192.168.49.2.nip.io",
    },
    config_file="None",
    dag=dag,
)

notebook_op_021933e9_680a_425d_930e_4954e33ead37.image_pull_policy = "IfNotPresent"

(
    notebook_op_021933e9_680a_425d_930e_4954e33ead37
    << notebook_op_e66c5e4e_5e26_4870_ade3_2be226c0631b
)

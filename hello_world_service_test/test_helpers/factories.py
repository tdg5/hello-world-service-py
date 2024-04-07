from typing import Optional

from service_oriented import DeploymentEnvironment

from hello_world_api_py.app.config import Config
from hello_world_api_py_test.test_helpers.fixtures import TEST_DEPLOYMENT_ENVIRONMENT


def make_config(
    deployment_environment: Optional[DeploymentEnvironment] = None,
    entry_point: Optional[str] = None,
) -> Config:
    _deployment_environment = deployment_environment or TEST_DEPLOYMENT_ENVIRONMENT
    _entry_point = entry_point or "test"

    return Config(
        deployment_environment=_deployment_environment,
        entry_point=_entry_point,
    )

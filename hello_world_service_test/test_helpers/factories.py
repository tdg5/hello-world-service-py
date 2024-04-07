from typing import Optional

from service_oriented import DeploymentEnvironment

from hello_world_service.app.config import Config
from hello_world_service_test.test_helpers.fixtures import (
    TEST_DEPLOYMENT_ENVIRONMENT,
    fixture_path,
)


def config(
    deployment_environment: Optional[DeploymentEnvironment] = None,
    entry_point: Optional[str] = None,
    logging_config_yaml_path: Optional[str] = None,
) -> Config:
    _deployment_environment = deployment_environment or TEST_DEPLOYMENT_ENVIRONMENT
    _entry_point = entry_point or "test"
    _logging_config_yaml_path = logging_config_yaml_path or fixture_path(
        "logging_config.yaml"
    )

    return Config(
        deployment_environment=_deployment_environment,
        entry_point=_entry_point,
        logging_config_yaml_path=_logging_config_yaml_path,
    )

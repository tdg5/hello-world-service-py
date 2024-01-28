import os
from typing import cast

from hello_world_api_py.app.application import Application
from hello_world_api_py.app.config import Config
from hello_world_api_py.main import Main
from hello_world_api_py_test.test_helpers import TEST_DEPLOYMENT_ENVIRONMENT
from hello_world_api_py_test.test_helpers.factories import make_config


def test_init_can_take_a_config_instance() -> None:
    config = make_config()
    subject = Main(config=config)
    assert config == subject.application.config


def test_build_application_builds_an_application_with_the_given_config() -> None:
    config = make_config()
    subject = Main(config=config)
    assert isinstance(subject.application, Application)
    assert config == subject.application.config


def test_build_config_builds_an_unparameterized_config_instance() -> None:
    deployment_environment_env_key = "HELLO_WORLD_API_PY_DEPLOYMENT_ENVIRONMENT"
    original_deployment_environment = os.environ.get(deployment_environment_env_key)
    entry_point_env_key = "HELLO_WORLD_API_PY_ENTRY_POINT"
    original_entry_point = os.environ.get(entry_point_env_key)
    deployment_environment = TEST_DEPLOYMENT_ENVIRONMENT.stub
    entry_point = "test"
    try:
        os.environ[deployment_environment_env_key] = deployment_environment
        os.environ[entry_point_env_key] = entry_point
        subject = Main()
        assert subject.config is not None
        assert TEST_DEPLOYMENT_ENVIRONMENT == subject.config.deployment_environment
        assert entry_point == subject.config.entry_point
    finally:
        if original_deployment_environment:
            os.environ[deployment_environment_env_key] = original_deployment_environment
        else:
            del os.environ[deployment_environment_env_key]

        if original_entry_point:
            os.environ[entry_point_env_key] = original_entry_point
        else:
            del os.environ[entry_point_env_key]


class DummyApplication(Application):
    def __init__(self, config: Config):
        super().__init__(config=config)
        self.run_called = False

    def run(self) -> None:
        self.run_called = True


class MainWithDummyApp(Main):
    def _build_application(self, config: Config) -> Application:
        return DummyApplication(config=config)

    def _build_config(self) -> Config:
        return make_config()


def test_init_builds_config_if_not_given_config() -> None:
    subject = MainWithDummyApp()
    assert subject.application.config is not None


def test_run_runs_the_application() -> None:
    config = make_config()
    subject = MainWithDummyApp(config=config)
    subject.run()
    assert cast(DummyApplication, subject.application).run_called

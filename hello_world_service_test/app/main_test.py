from hello_world_service.app.application import Application
from hello_world_service.app.config import Config
from hello_world_service.main import Main


def test_application_class_is_application() -> None:
    assert Application == Main.application_class()


def test_config_class_is_config() -> None:
    assert Config == Main.config_class()

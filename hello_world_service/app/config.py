from service_oriented.application.config import BaseConfig


class Config(
    BaseConfig,
    env_nested_delimiter="__",
    env_prefix="HELLO_WORLD_SERVICE_",
):
    logging_config_yaml_path: str

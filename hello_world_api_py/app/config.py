from service_oriented.application.config import BaseConfig


class Config(
    BaseConfig,
    env_nested_delimiter="__",
    env_prefix="HELLO_WORLD_API_PY_",
):
    pass

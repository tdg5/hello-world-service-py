from service_oriented.initializers.logging_initializer import LoggingInitializer

from hello_world_api_py.app.config import Config


class Container:
    def __init__(self, config: Config) -> None:
        self.config = config

    def initialize(self) -> None:
        self._initialize_logging()

    def _initialize_logging(self) -> None:
        LoggingInitializer(yaml_path=self.config.logging_config_yaml_path).initialize()

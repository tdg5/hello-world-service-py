from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Dependency, Resource
from service_oriented.containers import LoggingConfigResource

from hello_world_api_py.app.config import Config


class RootContainer(DeclarativeContainer):
    config: Dependency[Config] = Dependency()

    logging: Resource[LoggingConfigResource] = Resource(
        LoggingConfigResource,
        config.provided.logging_config_yaml_path,
    )

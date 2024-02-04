import logging

from hello_world_api_py.app.config import Config
from hello_world_api_py.app.containers import RootContainer


logger = logging.getLogger(__name__)


class ApiEntryPoint:
    def __init__(self, config: Config):
        self.config = config

    def run(self) -> None:
        container = RootContainer(config=self.config)
        container.init_resources()
        logger.info("Hello, world!")

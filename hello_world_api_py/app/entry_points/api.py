import logging

from hello_world_api_py.app.config import Config
from hello_world_api_py.app.container import Container


logger = logging.getLogger(__name__)


class ApiEntryPoint:
    def __init__(self, config: Config):
        self.config = config

    def run(self) -> None:
        container = Container(config=self.config)
        container.initialize()
        logger.info("Hello, world!")

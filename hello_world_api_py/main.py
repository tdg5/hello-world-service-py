from typing import Optional

from hello_world_api_py.app.application import Application
from hello_world_api_py.app.config import Config


class Main:
    def __init__(self, config: Optional[Config] = None):
        self.config = config or self._build_config()
        self.application = self._build_application(self.config)

    def _build_application(self, config: Config) -> Application:
        return Application(config=config)

    def _build_config(self) -> Config:
        return Config()

    def run(self) -> None:
        self.application.run()


if __name__ == "__main__":
    Main().run()  # pragma: no cover

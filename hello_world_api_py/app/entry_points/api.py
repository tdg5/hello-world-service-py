from hello_world_api_py.app.config import Config


class ApiEntryPoint:
    def __init__(self, config: Config):
        self.config = config

    def run(self) -> None:
        print("Hello, world!")

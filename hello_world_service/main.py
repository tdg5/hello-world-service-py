from service_oriented.application import GenericMain

from hello_world_service.app.application import Application
from hello_world_service.app.config import Config


class Main(GenericMain[Config, Application]):
    pass


if __name__ == "__main__":
    Main().run()  # pragma: no cover

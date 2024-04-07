from service_oriented.application import BaseApplication, EntryPointSpec

from hello_world_api_py.app.entry_points.api import ApiEntryPoint


class Application(
    BaseApplication,
    entry_points={
        "api": EntryPointSpec(ApiEntryPoint),
    },
):
    pass

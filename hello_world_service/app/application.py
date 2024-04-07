from service_oriented.application import BaseApplication, EntryPointSpec

from hello_world_service.app.entry_points.api_entry_point import ApiEntryPoint


class Application(
    BaseApplication,
    entry_points={
        "api": EntryPointSpec(ApiEntryPoint),
    },
):
    pass

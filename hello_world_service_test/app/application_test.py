from hello_world_service.app.application import Application


def test_api_endpoint_is_defined() -> None:
    assert "api" in Application.default_entry_points

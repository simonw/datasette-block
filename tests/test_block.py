from asgi_lifespan import LifespanManager
from datasette.app import Datasette
import httpx
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "prefixes,path,expected_status_code",
    (([], "/all/hello", 404), (["/all/"], "/all/hello", 403)),
)
async def test_block(prefixes, path, expected_status_code):
    datasette = Datasette(
        [], metadata={"plugins": {"datasette-block": {"prefixes": prefixes}}}
    )
    app = datasette.app()
    async with LifespanManager(app):
        async with httpx.AsyncClient(app=app) as client:
            response = await client.get("http://localhost" + path)
            assert response.status_code == expected_status_code

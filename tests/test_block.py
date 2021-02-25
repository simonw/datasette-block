from datasette.app import Datasette
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
    response = await datasette.client.get(path)
    assert response.status_code == expected_status_code

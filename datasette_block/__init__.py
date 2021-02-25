from datasette import hookimpl
from functools import wraps


@hookimpl
def asgi_wrapper(datasette):
    config = datasette.plugin_config("datasette-block") or {}
    prefixes = config.get("prefixes") or []

    def wrap_with_block(app):
        @wraps(app)
        async def block_prefixes(scope, recieve, send):
            for prefix in prefixes:
                if scope["path"].startswith(prefix):
                    await send_403(send)
                    return
            await app(scope, recieve, send)

        return block_prefixes

    return wrap_with_block


async def send_403(send):
    await send(
        {
            "type": "http.response.start",
            "status": 403,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"403 denied",
        }
    )

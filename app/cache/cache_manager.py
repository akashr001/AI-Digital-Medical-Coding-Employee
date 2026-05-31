from app.cache.redis_client import (
    redis_client
)

CACHE_TTL = 3600


def get_cache(key):

    return redis_client.get(
        key
    )


def set_cache(
    key,
    value
):

    redis_client.set(
        key,
        value,
        ex=CACHE_TTL
    )
from django.core.cache import InvalidCacheBackendError
from django.core.cache import cache as default_cache
from django.core.cache import caches

try:
    cache = caches["misago"]
except InvalidCacheBackendError:
    cache = default_cache

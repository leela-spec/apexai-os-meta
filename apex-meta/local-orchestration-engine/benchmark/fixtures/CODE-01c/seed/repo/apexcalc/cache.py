import json
from pathlib import Path


class StaleCacheError(Exception):
    pass


def load_index(cache_dir):
    path = Path(cache_dir) / "index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != 2:
        raise StaleCacheError(
            f"apexcalc.cache: stale index at {cache_dir}/index.json "
            f"(schema {data.get('schema')}, expected 2)"
        )
    return data

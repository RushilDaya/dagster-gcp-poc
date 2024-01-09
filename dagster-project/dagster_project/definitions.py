from dagster import Definitions, load_assets_from_modules, asset


@asset
def rushil_asset():
    return [1, 2, 3]


defs = Definitions(
    assets=[rushil_asset],
)
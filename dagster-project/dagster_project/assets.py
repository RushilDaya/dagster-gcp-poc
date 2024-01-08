from dagster import asset


@asset
def rushil_asset():
    return [1, 2, 3]

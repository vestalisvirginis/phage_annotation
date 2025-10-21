from dagster_docker import PipesDockerClient

import dagster as dg

from . import assets

defs = dg.Definitions(
    assets=dg.load_assets_from_modules([assets]),
    resources={"docker_client": PipesDockerClient()},
)
from typing import Iterator, List, Tuple
from dagster_docker import PipesDockerClient


import dagster as dg


@dg.asset(
    # check_specs=[
    #     dg.AssetCheckSpec(
    #         name="full_sequence",
    #         description="Reports created for all sequences",
    #         asset="fastqc_runner",
    #         blocking=False,
    #     )
    # ],
    kinds={"python"},
)
def fastqc_runner(
    context: dg.AssetExecutionContext,
) -> dg.Output[str]:
    """Extraction of phage sequences based on given att sites"""

    

@dg.asset(
    # check_specs=[
    #     dg.AssetCheckSpec(
    #         name="full_sequence",
    #         description="Reports created for all sequences",
    #         asset="fastqc_runner",
    #         blocking=False,
    #     )
    # ],
    kinds={"docker"},
)
def fastqc_runner(
    context: dg.AssetExecutionContext,
    docker_client: PipesDockerClient,
) -> Iterator[dg.Output[str]]:
    """Docker execution of pharokka tool"""
    result = docker_client.run(
        image="pharokka",
        command=["python", "/scripts/pharokka.py"],
        context=context,
        container_kwargs={
            "auto_remove": True,
            "volumes": {
                str(Path(os.getenv("ANNOTATION_HOME")) / "scripts"): {
                    "bind": "/scripts",
                    "mode": "ro",
                },
                str(
                    Path(os.getenv("ANNOTATION_HOME"))
                    / "databases"
                ): {
                    "bind": "/databases",
                    "mode": "ro",
                },
                str(
                    Path(os.getenv("ANNOTATION_HOME"))
                    / "data"
                    / "input"
                    / "fasta"
                ): {
                    "bind": "/inputs",
                    "mode": "ro",
                },
                str(
                    Path(os.getenv("ANNOTATION_HOME"))
                    / "data"
                    / "output"
                    / "pharokka"
                ): {
                    "bind": "/outputs",
                    "mode": "rw",
                },
            },
        },
    )

    # files_io = os.listdir(
    #     str(Path(os.getenv("ANNOTATION_HOME")) / "data" / "outputs" / "pre_fastqc")
    # )
    # _, files_spec = md5_validate

    # _stems = compose(first, mc("split", "-"), at("stem"), Path)
    # _f_stems = list(map(_stems, files_spec))
    # _f_outs = list(map(_stems, files_io))
    # complete = set(_f_stems).issubset(set(_f_outs))

    # yield dg.AssetCheckResult(passed=complete, check_name="full_sequence")

    yield dg.Output(value=str(result.get_results()))
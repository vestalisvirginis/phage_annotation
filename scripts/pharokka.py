import subprocess

from dagster_pipes import open_dagster_pipes

with open_dagster_pipes() as context:
    result = subprocess.run(["pharokka", "--version"], capture_output=True, text=True)
    version = result.stdout.strip()
    context.log.info(str(version))

    context.report_asset_materialization(metadata={"pharokka_version": version})

    context.log.info("Pharokka: Started")

    "pharokka.py -i /inputs/9_polished.fasta -o /outputs/phage_9_pha -d /databases/ -t 12 -p phage_9_pha -g phanotate --dnaapler"
    "pharokka.py -i /inputs/9_polished.fasta -o /outputs/phage_9_gv -d /databases/ -t 12 -p phage_9_gv -g prodigal-gv --dnaapler"

    context.log.info("Pharokka: Completed")

    8;160.65;125.49;reoriented
    3;124.74;119.75;no-reoriented
    9;124.56;120.42; no-reoriented
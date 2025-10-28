import subprocess

from dagster_pipes import open_dagster_pipes

with open_dagster_pipes() as context:
    result = subprocess.run(["pharokka", "--version"], capture_output=True, text=True)
    version = result.stdout.strip()
    context.log.info(str(version))

    context.report_asset_materialization(metadata={"pharokka_version": version})

    context.log.info("Pharokka: Started")

 #   "pharokka.py -i /inputs/22_polished.fasta -o /outputs/phage_22_pha -d /databases/ -t 12 -p phage_22_pha -g phanotate --dnaapler"
#   "pharokka.py -i /inputs/22_polished.fasta -o /outputs/phage_22_gv -d /databases/ -t 12 -p phage_22_gv -g prodigal-gv --dnaapler"

    context.log.info("Pharokka: Completed")


# sample;time_phanotate;time_prodigal-gv;re-orientation
#    3;124.74;119.75;no-reoriented
#    6;155.2;126.22;reoriented
#    7;156.94;126.04;reoriented
#    8;160.65;125.49;reoriented
#    9;124.56;120.42; no-reoriented
#    11;155.89;124.64;reoriented
#    12;156.1;124.8;reoriented
#    22;156.91;125.64;reoriented

#"pharokka_plotter.py -i /inputs/3_polished.fasta -n phage_3_plot -o /outputs/plots/phage_3_gv --gff /outputs/phage_3_gv/phage_3_gv.gff -p phage_3_gv --interval 8000 --annotations 0.5 --dpi 900 --plot_title '${Bacillus}$ Phage Phage_3_gv'"
pharokka_plotter.py -i /inputs/22_polished.fasta -o /outputs/phage_22_gv -n phage_22_gv_plot -p phage_22_gv --interval 5000 --annotations 1 --dpi 900 --plot_title '${Bacillus}$ Phage Phage_phage_22_gv'
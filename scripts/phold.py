phold run -i /inputs/phage_9_gv/phage_3_gv.gbk -o /outputs/phage_3_gv/  -t 16 -p phage_3_gv -d /databases/gpu_computing/ --finetune --keep_tmp_files --foldseek_gpu

phold install -d /databases/standard --extended_db -t 16

phold install -d /databases/gpu_computing --foldseek_gpu --extended_db -t 16 


sudo docker run -it --rm --name pholdtest -v /mnt/data/projects/4_annotations/phold_databases:/databases -v /mnt/data/projects/4_annotations/data/output/pharokka:/inputs -v /mnt/data/projects/4_annotations/data/output/phold:/outputs phold bash




phold run -i /inputs/phage_6_gv/phage_6_gv.gbk -o /outputs/phage_6_gv/  -t 16 -p phage_6_gv -d /databases/gpu_computing/ --finetune --keep_tmp_files --foldseek_gpu



phold run -i /inputs/phage_3_pha/phage_3_pha.gbk -o /outputs/phage_3_pha/  -t 16 -p phage_3_pha -d /databases/gpu_computing/ --finetune --keep_tmp_files --cpu

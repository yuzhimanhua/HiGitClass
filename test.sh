dataset=ai
sup_source=keywords
embedding=esim

python main.py --dataset ${dataset} --sup_source ${sup_source} --block_level 2 --embedding ${embedding}

python eval.py --dataset ${dataset}

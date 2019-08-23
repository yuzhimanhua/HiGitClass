dataset=bio
sup_source=keywords
embedding=esim

export CUDA_VISIBLE_DEVICES=0

python main.py --dataset ${dataset} --sup_source ${sup_source} --block_level 2 --embedding ${embedding}

python eval.py --dataset ${dataset}

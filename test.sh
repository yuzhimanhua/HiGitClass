dataset=bio
embedding=esim

python main.py --dataset ${dataset} --embedding ${embedding}

python eval.py --dataset ${dataset}

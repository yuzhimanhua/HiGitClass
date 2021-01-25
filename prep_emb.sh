dataset=ai
json_name=AI_Hier.json

python preprocess.py --dataset ${dataset} --json_name ${json_name}

cd ESim/

python construct.py --dataset ${dataset} --json_name ${json_name}

./run.sh

python postprocess.py --dataset ${dataset}

cd ../

dataset=bio
json_name=Bio_Hier.json

echo Data Preprocessing ...
python preprocess.py --dataset ${dataset} --json_name ${json_name}

cd ESim/

echo Embedding Preprocessing ...
python construct.py --dataset ${dataset} --json_name ${json_name}

echo Embedding Learning ...
./run.sh

echo Embedding Postprocessing ...
python postprocess.py --dataset ${dataset}

cd ../

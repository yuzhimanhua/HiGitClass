#!/bin/bash

dataset="ai"
json_name="AI_Hier.json"
python constructHIN.py --dataset ${dataset} --json_name ${json_name}

node_file="node.dat"
link_file="link.dat"
path_file="path.dat"
output_file="vec.dat"

make

size=100 # embedding dimension
negative=5 # number of negative samples
samples=1 # number of edges (Million) for training at each iteration
iters=500 # number of iterations
threads=20 # number of threads for training

./bin/esim -model 2 -alpha 0.025 -node ${node_file} -link ${link_file}  -path ${path_file} -output ${output_file} -binary 0 -size ${size} -negative ${negative} -samples ${samples} -iters ${iters} -threads ${threads}

python extractEmbedding.py --dataset ${dataset}

import json
import argparse

parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataset', default='ai', choices=['ai', 'bio'])
parser.add_argument('--json_name', default='AI_Hier.json')

args = parser.parse_args()
dataset = args.dataset
json_name = args.json_name

with open(dataset+'/'+json_name) as fin, open(dataset+'/dataset.txt', 'w') as fou1, open(dataset+'/labels.txt', 'w') as fou2:
	for line in fin:
		js = json.loads(line)
		fou1.write(js['text'] + ' ' + js['user'] + ' ' + ' '.join(js['tags']) + ' ' + ' '.join(js['name']) + '\n')
		fou2.write(js['labels'][-1] + '\n')

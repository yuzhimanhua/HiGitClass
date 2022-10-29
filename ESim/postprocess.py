import string
import argparse

parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataset', default='ai', choices=['ai', 'bio'])

args = parser.parse_args()
dataset = args.dataset

print('### Extract Embedding ###')

tot = 0
with open('vec.dat') as fin:
	for line in fin:
		data = line.strip().split()
		if data[0].startswith('$') or len(data) != 101:
			continue
		tot += 1

with open('vec.dat') as fin, open(f'../{dataset}/embedding_esim', 'w') as fout:
	fout.write(str(tot)+'\t100\n')
	for line in fin:
		data = line.strip().split()
		if data[0].startswith('$') or len(data) != 101:
			continue
		fout.write(line)
import string
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataset', default='ai', choices=['ai', 'bio'])
parser.add_argument('--json_name', default='AI_Hier.json')

args = parser.parse_args()
dataset = args.dataset
json_name = args.json_name

print('### Constructing HIN ###')

cnt = dict()
repo = set()
user = set()
tag = set()
name = set()
max_len = 1500
with open(f'../{dataset}/{json_name}') as fin:
	for idx, line in enumerate(tqdm(fin)):
		data = json.loads(line.strip())

		repo.add('$REPO'+str(idx))
		user.add('$USER'+data['user'])

		for T in data['tags']:
			tag.add('$TAG'+T.lower())

		for N in data['name']:
			name.add('$NAME'+N.lower())

		W = data['text'].lower().split()
		for token in W[:max_len]:
			if token not in cnt:
				cnt[token] = 0
			cnt[token] += 1

label = set()
parent_label = dict()
with open(f'../{dataset}/label_hier.txt') as fin:
	for line in fin:
		data = line.strip().split()
		for L in data[1:]:
			label.add('$LABEL'+L)
			parent_label[L] = data[0]

with open('node.dat', 'w') as fout:
	for R in repo:
		fout.write(R+' r\n')

	for U in user:
		fout.write(U+' u\n')

	for L in label:
		fout.write(L+' l\n')

	for T in tag:
		fout.write(T+' t\n')

	for N in name:
		fout.write(N+' n\n')

	for W in cnt:
		if cnt[W] >= 5:
			fout.write(W+' w\n')

with open(f'../{dataset}/{json_name}') as fin1, open(f'../{dataset}/keywords.txt') as fin2, open('link.dat', 'w') as fout:
	for idx, line in enumerate(tqdm(fin1)):	
		data = json.loads(line)

		R = '$REPO'+str(idx)
		U = '$USER'+data['user']
		Ts = ['$TAG'+x.lower() for x in data['tags']]
		Ns = ['$NAME'+x.lower() for x in data['name']]

		W = data['text'].lower().split()

		sent = []
		for token in W[:max_len]:
			if cnt[token] >= 5:
				sent.append(token)

		for i in range(len(sent)):
			fout.write(sent[i]+' '+R+'\n')
			fout.write(R+' '+sent[i]+'\n')
			
			fout.write(sent[i]+' '+U+'\n')
			fout.write(U+' '+sent[i]+'\n')
			
			for T in Ts:
				fout.write(sent[i]+' '+T+'\n')
				fout.write(T+' '+sent[i]+'\n')

			for N in Ns:
				fout.write(sent[i]+' '+N+'\n')
				fout.write(N+' '+sent[i]+'\n')

	for line in fin2:
		data = line.strip().split()
		Ls = []
		L = data[0]
		while L != 'ROOT':
			Ls.append('$LABEL'+L)
			L = parent_label[L]

		for keyword in data[1:]:
			if keyword in cnt and cnt[keyword] >= 5:
				for L in Ls:
					fout.write(keyword+' '+L+'\n')
					fout.write(L+' '+keyword+'\n')

with open('path.dat', 'w') as fout:
	fout.write('wrw 0.2\n')
	fout.write('wlw 0.2\n')
	fout.write('wuw 0.2\n')
	fout.write('wtw 0.2\n')
	fout.write('wnw 0.2\n')
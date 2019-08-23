import string
import json

import argparse
parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--dataset', default='ai', choices=['ai', 'bio'])
parser.add_argument('--json_name', default='AI_Hier.json')
args = parser.parse_args()
dataset = args.dataset
json_name = args.json_name

print('### Constructing HIN ###')


cnt = dict()
parent_label = dict()

repo = set()
label = set()
user = set()
tag = set()
name = set()

with open('../'+dataset+'/'+json_name) as fin:
	for idx, line in enumerate(fin):
		
		js = json.loads(line.strip())

		repo.add('$REPO'+str(idx))
		user.add('$USER'+js['user'])

		if js['sub_label'] not in parent_label:
			parent_label[js['sub_label']] = js['super_label']

		label.add('$LABEL'+js['sub_label'])
		label.add('$LABEL'+js['super_label'])

		for T in js['tags']:
			tag.add('$TAG'+T.lower())

		for N in js['repo_name_seg'].split():
			name.add('$NAME'+N.lower())

		W = js['text'].lower().split()
		for token in W[:1500]:
			if token not in cnt or len(token) >= 50:
				cnt[token] = 0
			cnt[token] += 1

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
		if cnt[W] < 5:
			continue
		fout.write(W+' w\n')

win = 5

with open('../'+dataset+'/'+json_name) as fin1, open('../'+dataset+'/keywords.txt') as fin2, open('link.dat', 'w') as fout:
	for idx, line in enumerate(fin1):
		
		js = json.loads(line)

		R = '$REPO'+str(idx)
		U = '$USER'+js['user']
		Ts = ['$TAG'+x.lower() for x in js['tags']]
		Ns = ['$NAME'+x.lower() for x in js['repo_name_seg'].split()]

		W = js['text'].lower().split()

		sent = []
		for token in W[:1500]:
			if cnt[token] < 5:
				continue
			sent.append(token)

		for i in range(len(sent)):
			for j in range(i+1, i+win+1):
				if j >= len(sent):
					continue
				fout.write(sent[i]+' '+sent[j]+'\n')
				fout.write(sent[j]+' '+sent[i]+'\n')

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
		tmp = line.strip().split()
		L1 = '$LABEL'+tmp[0]
		L2 = '$LABEL'+parent_label[tmp[0]]

		for keyword in tmp[1]:
			if keyword in cnt and cnt[keyword] >= 5:
				fout.write(keyword+' '+L1+'\n')
				fout.write(keyword+' '+L2+'\n')
				fout.write(L1+' '+keyword+'\n')
				fout.write(L2+' '+keyword+'\n')

with open('path.dat', 'w') as fout:
	fout.write('wrw 0.2\n')
	fout.write('wlw 0.2\n')
	fout.write('wuw 0.2\n')
	fout.write('wtw 0.2\n')
	fout.write('wnw 0.2\n')
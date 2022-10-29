import string
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
import argparse

parser = argparse.ArgumentParser(description='main', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataset', default='ai', choices=['ai', 'bio'])

args = parser.parse_args()
dataset = args.dataset

print('\n### Testing ###')

p = dict()
with open(f'{dataset}/label_hier.txt') as fin:
	for line in fin:
		data = line.strip().split()
		for label in data[1:]:
			p[label.lower()] = data[0].lower()

y_u = []
y_d = []
with open(f'{dataset}/labels.txt') as fin:
	for line in fin:
		dl = line.strip().lower()
		y_u.append(p[dl])
		y_d.append(dl)

y_u_pred = []
y_d_pred = []
with open(f'{dataset}/out.txt') as fin:
	for line in fin:
		data = line.strip().split()
		y_u_pred.append(data[0].lower())
		y_d_pred.append(data[1].lower())

print('Upper Micro F1 score:', f1_score(y_u, y_u_pred, average='micro'))
print('Upper Macro F1 score:', f1_score(y_u, y_u_pred, average='macro'))
print('Upper-level Confusion Matrix:')
print(confusion_matrix(y_u, y_u_pred))

print('Lower Micro F1 score:', f1_score(y_d, y_d_pred, average='micro'))
print('Lower Macro F1 score:', f1_score(y_d, y_d_pred, average='macro'))
print('Lower-level Confusion Matrix:')
print(confusion_matrix(y_d, y_d_pred))

print('Overall Micro F1 score:', f1_score(y_u+y_d, y_u_pred+y_d_pred, average='micro'))
print('Overall Macro F1 score:', f1_score(y_u+y_d, y_u_pred+y_d_pred, average='macro'))
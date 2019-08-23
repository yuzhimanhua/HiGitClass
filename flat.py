import string
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

dataset = 'bio'

p = dict()
with open(dataset+'/label_hier_hier.txt') as fin:
	for line in fin:
		tmp = line.strip().split()
		for label in tmp[1:]:
			p[label.lower()] = tmp[0].lower()

y_u = []
y_d = []
with open(dataset+'/labels.txt') as fin:
	for line in fin:
		dl = line.strip().lower()
		y_u.append(p[dl])
		y_d.append(dl)

y_u_pred = []
y_d_pred = []
with open(dataset+'/out.txt') as fin:
	for line in fin:
		tmp = line.strip().split()
		y_u_pred.append(p[tmp[0].lower()])
		y_d_pred.append(tmp[0].lower())

print('Upper Micro/Macro:')
print(f1_score(y_u, y_u_pred, average='micro'))
print(f1_score(y_u, y_u_pred, average='macro'))

print('Lower Micro/Macro:')
print(f1_score(y_d, y_d_pred, average='micro'))
print(f1_score(y_d, y_d_pred, average='macro'))
print(confusion_matrix(y_d, y_d_pred))

print('Overall Micro/Macro:')
print(f1_score(y_u+y_d, y_u_pred+y_d_pred, average='micro'))
print(f1_score(y_u+y_d, y_u_pred+y_d_pred, average='macro'))
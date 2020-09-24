import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
import numpy as np
from math import sqrt


'''
Retorna o item que mais se repete em uma lista
'''
def most_common(lst):
    return max(set(lst), key=lst.count)

def main():
	

	data = pd.read_csv('wine.data',names=['class','atr1','atr2','atr3','atr4','atr5','atr6','atr7','atr8','atr9','atr10','atr11','atr12','atr13'])

	x_train, x_test = train_test_split(data, test_size=0.2, random_state=42, shuffle=True)
		


	'''
	Separa e exclui os labels do dataset
	'''
	y_train = list(x_train['class'])
	del x_train['class']

	y_test = list(x_test['class'])
	del x_test['class']

	x_train = normalize(x_train, axis=0)
	x_test = normalize(x_test, axis=0)

	#LET'S

	k = 3
	acc = 0

	#CODE HERE

	print('Acc:',acc,'Total:',np.shape(x_test)[0],"Rate:",acc/np.shape(x_test)[0])


	
if __name__ == '__main__':
	main()
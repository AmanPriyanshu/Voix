from GloVe_helper import GloVeLoader
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
import pickle

if __name__ == '__main__':
	gl = GloVeLoader()
	df = pd.read_csv('IMDB_Dataset.csv')
	df = df.values

	x, y = df.T[0], df.T[1]
	y = np.array([0 if i=='negative' else 1 for i in y])

	x = np.array([gl.pull_glove_embed(i) for i in x])
	print("starting training")
	clf = MLPClassifier(random_state=1, max_iter=500, verbose=True).fit(x, y)
	clf.score(x, y)
	pickle.dump(clf, open('sentiment_model.sav', 'wb'))
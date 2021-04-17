import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def generate_trends(n=1, epsilon=0.925, processing_limit=100):
	df = pd.read_csv('posts.csv')
	df = df.values
	df = df.T[2:].T
	df = df[-processing_limit:]

	df += np.mean(np.random.laplace(loc=0.0, scale=1/epsilon, size=df.shape))

	kmeans = KMeans(n_clusters=n, random_state=0).fit(df)
	results = kmeans.cluster_centers_
	indexes = []
	for result in results:
		indexes.append(np.argmin(np.abs(result - df)))
	trending = pd.DataFrame({'trending_posts': indexes})
	trending.to_csv('trending.csv', index=False)

if __name__ == '__main__':
	generate_trends()
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import string

class GloVeLoader:
	def __init__(self, word_limit=10, glove_path='./GloVe/glove.15d.txt', dims=15):
		self.glove_path = glove_path
		self.word_limit = word_limit
		self.embeddings_dict = {}
		self.glove_loader()
		self.wordnet_lemmatizer = WordNetLemmatizer()
		self.punctuation = string.punctuation
		self.dims = dims

	def glove_loader(self):
		with open(self.glove_path, 'r', encoding="utf-8") as f:
			for line in f:
				values = line.split()
				word = values[0]
				vector = np.asarray(values[1:], "float32")
				self.embeddings_dict[word.lower()] = vector

	def pull_glove_embed(self, sentence):
		vec = []
		for w in nltk.word_tokenize(sentence)[:self.word_limit]:
			try:
				vec.append(self.embeddings_dict[w.lower()])
			except:
				try:
					vec.append(self.embeddings_dict[self.wordnet_lemmatizer.lemmatize(w.lower())])
				except:
					vec.append(np.zeros(self.dims))
		vec += [np.zeros(self.dims) for _ in range(self.word_limit - len(vec))]
		vec = np.stack(vec)
		vec = vec.flatten()
		return vec

def get_embed(sentence):
	gl = GloVeLoader()
	return gl.pull_glove_embed(sentence)

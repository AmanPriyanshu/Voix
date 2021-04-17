from flask import Flask, request, jsonify
from GloVe_helper import get_embed
import pandas as pd
import os
from find_trends import generate_trends
import numpy as np
import pickle

WORD_LIMIT = 10

app = Flask(__name__)

def get_post_details(index):
	if not os.path.isfile('./posts/post_'+str(index)+'.csv'):
		return {}
	else:
		df = pd.read_csv('./posts/post_'+str(index)+'.csv')
		df = df.values
		df = df.T[0]
		return {i: df[i] for i in range(len(df))}

@app.route('/', methods=['GET', 'POST'])
def index():
	return "Hello World"

@app.route('/get_trends', methods=['GET'])
def get_trends():
	df = pd.read_csv('trending.csv')
	df = df.values
	indexes = df.T[0]
	df = pd.read_csv('posts.csv', usecols=['post_content'])
	df = df.values
	df = df.T[0]
	df = df[indexes]
	return jsonify({i:df[i] for i in range(len(df))})

@app.route('/get_post', methods=['POST'])
def get_post():
	data = request.get_json()
	df = pd.read_csv('posts.csv', usecols=['author', 'post_content'])
	df = df.values
	index = np.where(df.T[1]==data['post_content'])[0][0]
	return jsonify(get_post_details(index))

@app.route('/make_comment', methods=['POST'])
def make_comment():
	data = request.get_json()
	embed = get_embed(data['comment'])
	clf = pickle.load(open('sentiment_model.sav', 'rb'))
	embed = np.array([embed])
	df = pd.DataFrame({'comments': [data['comment']], 'sentiment': clf.predict(embed)[0]})
	if not os.path.isfile('./posts/post_'+str(data['index'])+'.csv'):
		df.to_csv('./posts/post_'+str(data['index'])+'.csv', index=False, header=True, mode='w')
	else:
		df.to_csv('./posts/post_'+str(data['index'])+'.csv', index=False, header=False, mode='a')
	return jsonify(get_post_details(data['index']))

@app.route('/make_post', methods=['POST'])
def save_data():
	data = request.get_json()
	embed = get_embed(data['post_content'])
	data.update({"embedding"+str(idx):embed[idx] for idx in range(len(embed))})
	data = {key: [value] for key, value in data.items()}
	df = pd.DataFrame(data)
	if os.path.isfile('posts.csv'):
		df.to_csv('posts.csv', index=False, mode='a', header=False)
	else:
		df.to_csv('posts.csv', index=False, mode='a', header=True)
	generate_trends()
	return jsonify({})

if __name__ == '__main__':
	app.run(debug=True)
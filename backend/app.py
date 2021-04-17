from flask import Flask, request, jsonify
from GloVe_helper import get_embed
import pandas as pd
import os
from find_trends import generate_trends

WORD_LIMIT = 10

app = Flask(__name__)

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
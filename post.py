import streamlit as st
import requests
import os

NAME = 'Voix'
URL = "http://shutdown20011.pythonanywhere.com/"
data = None
n = None

def set_up(data_i, n_i):
	global data, n
	data = data_i
	n = n_i

def app():
	global data, n
	st.title('Post')
	st.markdown('## '+data[n])
	post_ref = {
		"post_content": data[n]
	}
	r = requests.post(url=URL+"get_post", json=post_ref)
	r = r.json()
	r = list(r.values())
	if len(r)>0:
		[st.write(i) for i in r]

	st.markdown("### Make a Comment:")
	author = st.text_input('Author:')
	comment = st.text_area('What are you thinking?', height=10, max_chars=300)

	if(author!="" and comment!="" and st.button('Comment!')):
		post_ref = {
			"index": n,
			"author": author,
			"comment": comment
		}
		r = requests.post(url=URL+"make_comment", json=post_ref)
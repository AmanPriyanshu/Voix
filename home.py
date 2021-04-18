import streamlit as st
import requests

NAME = 'Voix'
URL = "http://shutdown20011.pythonanywhere.com/"

def app():
	st.title('Home')
	st.write('Welcome to '+NAME)
	st.write('Utilizing the power of Social Media to Promote Civic Participation and Amplifying the Voice of the People.')
	st.subheader('Make a New Post')
	author = st.text_input('Author:')
	post = st.text_area('What are you thinking?', height=10, max_chars=300)

	if(author!="" and post!="" and st.button('POST')):
		post_ref = {
		"author": author,
		"post_content": post
		}

		r = requests.post(url=URL+"make_post", json=post_ref)
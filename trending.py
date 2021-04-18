import streamlit as st
import requests
from post import set_up

NAME = 'Voix'
URL = "http://shutdown20011.pythonanywhere.com/"

posts = []

def app():
	global posts
	st.title('Trending')
	st.write('Welcome to the Trending, herein we present the most live and topical subjects.')

	st.markdown("## POSTS")
	if st.button('Refresh'):
		r = requests.get(url=URL+'get_trends')
		data = r.json()
		
		for key, value in data.items():
			st.markdown(str(int(key)+1)+'. `'+value+'`')
			posts.append(value)
	n = st.text_input("Enter post number")
	if(n!="" and st.button("Submit")):
		try:
			set_up(posts[-10:], int(n)-1)
		except:
			set_up(posts[-10:], 0)
import home
import post
import trending
import streamlit as st
from multiapp import MultiApp

app = MultiApp()
app.add_app("Home", home.app)
app.add_app("Trending", trending.app)
app.add_app("Post", post.app)
app.run()
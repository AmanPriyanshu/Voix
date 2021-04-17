import home
import trending
import streamlit as st
from multiapp import MultiApp

app = MultiApp()
app.add_app("Home", home.app)
app.add_app("Trending", trending.app)
app.run()
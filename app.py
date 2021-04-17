import home
import trending
import streamlit as st
PAGES = {
    "Home": home,
    "Trending": trending
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
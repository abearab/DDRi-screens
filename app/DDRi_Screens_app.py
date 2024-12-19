import streamlit as st

st.set_page_config(
    page_title='DDRi Screens App',
)

st.title('DDRi Screens App')
st.markdown(
    'This app is a collection of volcano plots for various DDRi screens.'
)



st.sidebar.tabs = ['Home', 'Screens']
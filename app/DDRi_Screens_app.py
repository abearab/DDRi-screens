import streamlit as st

st.set_page_config(
    page_title='DDRi Screens App',
)

st.title('DDRi Screens App')
st.markdown(
    """
    This is a data exploration app for the DDRi Screens dataset.
    """
)

# Show the link to the pages
st.page_link('pages/1_🧬_CRISPRi_mono_therapy_💊.py', 
             label='CRISPRi mono therapy screens 💊')
st.page_link('pages/2_🧬_CRISPRi_combination_therapy_💊💊.py', 
             label='CRISPRi combination therapy screens 💊💊')

from glob import glob
import streamlit as st

st.title('DDRi Screens App')
st.markdown('This app is a collection of volcano plots for various DDRi screens.')

### Interactive Plots

# # List of inhibitors and their corresponding names
# screens_path_list = glob('app/_html/*')
# for path in screens_path_list:
#     screens_id = path.split('/')[-1].split('.')[0]

screens_id = 'A549_CRISPRi_v2_screens'

st.markdown(f'## {screens_id.replace("_v2_", " (V2) ").replace("_", " ")}')

# List all volcano plots for each screen
for file_path in glob(f'app/_html/{screens_id}/*.html'):
    drug_name = file_path.split('/')[-1].replace('_volcano.html', '')

    st.subheader(f'{drug_name} Volcano Plot')
    # st.markdown(f'[View detailed plot]({file_path})')
    st.components.v1.html(open(file_path).read(), height=600, scrolling=True)

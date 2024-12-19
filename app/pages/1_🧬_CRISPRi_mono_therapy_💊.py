import os
import pandas as pd
import streamlit as st

def highlight_rho_label(row):
    if row['rho_label'] == 'resistance_hit':
        color = 'color: #de2d26; alpha: 0.1' 
    elif row['rho_label'] == 'sensitivity_hit':
        color = 'color: #3182bd; alpha: 0.1'
    else:
        color = ''
    return [color] * len(row)

screens_id = 'A549_CRISPRi_v2_screens'
treatments = [
    'PARPi',
    'ATMi',
    'ATRi',
    'DNAPKi',
    'WEE1i',
]

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)

selected_treatment = st.selectbox('Select a treatment', treatments)

if selected_treatment:
    drug_name = selected_treatment
    file_path = f'{parent_dir}/data/{screens_id}/{drug_name}_volcano.html'

    st.subheader(f'{drug_name} Volcano Plot')
    # st.markdown(f'[View detailed plot]({file_path})')
    st.components.v1.html(open(file_path).read(), height=400, scrolling=False)

    st.divider()

    st.subheader(f'{drug_name} Scatter Plot')
    st.components.v1.html(open(file_path.replace('volcano', 'scatter')).read(), height=400, scrolling=False)

    st.divider()
    
    st.subheader(f'{drug_name} Table of Hits')
    df = pd.read_csv(file_path.replace('.html', '.csv'))
    df.drop(columns=[col for col in df.columns if '-log10' in col], inplace=True)
    # df.drop(columns=[col for col in df.columns if 'gamma' in col], inplace=True)

    st.dataframe(df.style.apply(highlight_rho_label, axis=1), height=500, hide_index=True)
    
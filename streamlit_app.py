import streamlit as st
import pandas as pd

st.title('💩ZoIR first app')

st.write('Hakim vret!')

with st.expander('Initial data'):
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  st.wirte('**x**')
  X_raw = df.drop('species', axis = 1 )
  X_raw

  st.wirte('**y**')
  y_raw = df.species
  y_raw

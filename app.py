# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QY65NWorfR_r7PqAFuTAsXqZ_FxC8cTg
"""

import streamlit as st
import random

st.title('Test Streamlit')
st.write('Hello World!')

if st.button('Generate Random Number'):
    random_number = random.randint(1, 100)
    st.write(f'Random Number: {random_number}')

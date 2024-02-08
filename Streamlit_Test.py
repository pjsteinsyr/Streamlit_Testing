import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Peter's Test Site")
st.header("**This site is a test for IST 300**")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.image("SyracuseUniversity.jpg")
st.radio('Pick your gender',['Male','Female'])
df= pd.DataFrame(np.random.randn(10, 2),
                 columns=['x', 'y'])
st.line_chart(df)

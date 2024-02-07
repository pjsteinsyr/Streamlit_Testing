import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand=np.random.normal(1, 2, size=20)fig, ax = plt.subplots()ax.hist(rand, bins=15)st.pyplot(fig)
st.title("Peter's Test Site")
st.header("**This site is a test for IST 300**")
st.image("SyracuseUniversity.jpg")
st.radio('Pick your gender',['Male','Female'])



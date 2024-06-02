import streamlit as st
import numpy as np
import plotly.express as pe
st.title("Mehak Boutique")
st.header("Welcome to Mehak Boutique")
st.subheader("Alteration, Western Dress")
st.write("It established in 2000.")
x=st.number_input("Add number of stich dresses",value=0,format="%d")
price=x*250
st.write("Price:"+str(price))
y=np.linspace(-10,10,200)
z=y**2
fig=pe.line(x=y,y=z,title="Square")
st.plotly_chart(fig)

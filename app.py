import streamlit as st
import pandas as pd

view = [100,150,30]
st.write("# Youtube View")
st.write("## raw")
st.write("## Bar Chart")
st.bar_chart(view)
sview = pd.Series(view)
sview
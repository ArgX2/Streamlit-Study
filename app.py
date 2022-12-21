import streamlit as st
import pandas as pd
from PIL import Image
image = Image.open('alpago.jpg')

st.title("Henlo")
view = [100,150,30]
st.write("## Bar Chart")
st.bar_chart(view)
sview = pd.Series(view)
sview
st.image(image, caption="사진 테스트.")
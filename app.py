import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open('alpago.jpg')

st.title("Henlo")
st.image(image, caption="사진 테스트.")

Num = st.slider('인원 입력 후 버튼 클릭.', 0, 50, 25)
st.write("현재 설정 된 인원 수:",Num)

Line = list(range(Num))
sview = pd.DataFrame(
   columns=('%d' % i for i in range(Num)))

st.dataframe(sview)

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
image = Image.open('alpago.jpg')

st.title("Henlo")
st.image(image, caption="사진 테스트.")

Num = st.slider('인원 입력 후 버튼 클릭.', 0, 50, 25)
st.write("현재 설정 된 인원 수:",Num)
NumList = list(range(Num))
NameList = list(range(Num))

st.write('')

Name = st.text_input('여기에 이름 입력')
st.write(Name)

Stack = 0
for i in range(Num):
    if st.button('확인',i):
        NameList[Stack] = Name
        Stack+=1
    else:
        st.write('입력 후 클릭')
    
if st.button('초기화'):
    Stack=0
    NumList = [0 for i in range(Num)]
    NameList = ['-' for i in range(Num)]
else:
    st.write('초기화')

st.write('')

option = st.selectbox(
    '위치 선택 후 변경',
    ('Email', 'Home phone', 'Mobile phone')
)
st.write('You selected:', option)

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

st.write("")

key = st.checkbox("이름 수정하기")



if key:
    
    Stack = 0

    Name = st.text_input('여기에 이름 입력',Stack)
    st.write("이전에 입력된 값:", Name)

    if st.button('확인'):
        NameList[Stack] = Name
        Stack+=1

        
    if st.button('초기화'):
        Stack=0
        NumList = [0 for i in range(Num)]
        NameList = ['-' for i in range(Num)]


    st.write('')

    option = st.selectbox(
        '위치 선택 후 변경',
        ('Email', 'Home phone', 'Mobile phone')
    )

st.write('You selected:', option)

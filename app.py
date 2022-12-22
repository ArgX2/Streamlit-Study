import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image
image = Image.open('alpago.jpg')

st.title("Henlo")
st.image(image, caption="사진 테스트.")

Num = st.slider('인원 입력 후 버튼 클릭.', 2, 50, 25)
st.write("현재 설정 된 인원 수:",Num)
NumList = [0 for i in range(Num)]
NameList = list(range(Num))
NumList2 = []

st.write("")

key = st.checkbox("이름 수정하기")


if key:
    
    Stack = 0

    Name = st.text_input('여기에 이름 입력',Stack)
    st.write("이전에 입력된 값:", Name)

    if Stack <= 0:
        if st.button('이전'):
            NameList[Stack] = Name
            Stack-=1

    elif Stack >= Num-1:        
        if st.button('다음'):
            NameList[Stack] = Name
            Stack+=1

        
    if st.button('초기화'):
        Stack=0
        NumList = [0 for i in range(Num)]
        NameList = ['-' for i in range(Num)]

    st.write('')
else:
    NameList = [(i+1) for i in range(Num)]

def Mix():
    NumList2 = []
    for i in range(Num):
        Sv = random.randrange(0,len(NumList))
        NumList2[i] = NumList[Sv]
        del NumList[Sv]

if st.button('MIX'):
    Mix()   


option = st.selectbox(
        '위치 선택 후 변경',
        (NameList)
    )

Mix()
st.write('선택된 값의 수:', NumList2[NameList.index(option)])

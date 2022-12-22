import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image
img = Image.open('alpago.jpg')

def Mix(L1, NL2, N):
    L1 = [i for i in range(N)]
    L2 = []
    for i in range(N):
        Sv = random.randrange(0,len(L1))
        L2.append(L1[Sv])
        del L1[Sv]
    return L2


st.title("사다리타기")
st.image(img)

Num = st.slider('인원 입력 후 버튼 클릭.', 2, 50, 10)
st.write("현재 설정 된 인원 수:",Num)
NumList = [i for i in range(Num)]
NameList = list(range(Num))
NumList2 = list()

st.write("")

key = st.checkbox("이름 수정하기")

if key:
    
    Stack = 0

    Name = st.text_input('여기에 이름 입력',Stack)
    st.write("이전에 입력된 값:", Name)

    if Stack > 0:
        if st.button('이전'):
            NameList[Stack] = Name
            Stack-=1

    elif Stack <= Num-1:        
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



if st.button('MIX'): 
    NumList2 = Mix(NumList, NumList2, Num)

    col1, col2, col3 = st.columns(3)
    Split = Num//3
    with col1:
        for i in range(0,Split):
            NameList[i] = st.checkbox(NameList[i])
            if NameList[i]:
                st.write(NumList2[NameList.index(option)])

    with col2:
        for i in range(Split-1,Split*2):
            NameList[i] = st.checkbox(NameList[i])
            if NameList[i]:
                st.write(NumList2[NameList.index(option)])    

    with col3:
        for i in range(Split*2-1,Num-1):
            NameList[i] = st.checkbox(NameList[i])
            if NameList[i]:
                st.write(NumList2[NameList.index(option)])                     



st.write("")
option = st.multiselect(
        '대상 선택',
        (NameList)
    )
st.write('선택된 대상에게 배정된 값:', NumList2[NameList.index(option)])


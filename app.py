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

    Name = st.text_input('여기에 이름 입력')

    st.write("현재 대상 - ", Stack+1, "번째")

    if Stack > 0:
        if st.button('이전'):  
            Stack-=1

    elif Stack <= Num-1:        
        if st.button('다음'):
            Stack+=1

    if st.button('확인'):
        NameList[Stack] = Name

        st.write(NameList)

        
    if st.button('초기화'):
        Stack=0
        NumList = [0 for i in range(Num)]
        #NameList = ['-' for i in range(Num)]

    st.write('')
else:
    NameList = [str(i+1)+"번" for i in range(Num)]

Open = 0    
    
Select = st.multiselect("알고싶은 대상 선택", NameList)

if st.button('MIX'): 
    NumList2 = Mix(NumList, NumList2, Num)
    Open = 1

if Open:
    for i in range(len(Select)):
        st.write(Select[i],"의 값 - ",NumList2[NameList.index(Select[i])])

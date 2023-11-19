!pip install streamlit

import streamlit as st

# CSS를 통한 스타일링
st.markdown("""
    <style>
    .main {
        font-family: 'Helvetica Neue', sans-serif;
        color: #333;
        background-color: #f4f4f9;
    }
    .stTextInput>div>div>input {
        color: #4f8bf9;
    }
    .stButton>button {
        background-color: #4f8bf9;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 제목 및 서브타이틀
st.title("간단한 앱")
st.subheader("TOSS 앱 스타일")

# 사용자 입력 폼
with st.form(key='my_form'):
    name = st.text_input(label="이름을 입력하세요")
    submit_button = st.form_submit_button(label='제출')

# 제출 버튼이 눌렸을 때의 처리
if submit_button:
    st.write(f"안녕하세요, {name}님!")

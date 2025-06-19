import streamlit as st
import pandas as pd

# 제목
st.title("🥗 도시락 선택 데이터 분석 앱")

# CSV 파일 불러오기
data = pd.read_csv("lunchdata.csv", encoding='cp949')

# 날짜 형식 변환 (선택)
data["날짜"] = pd.to_datetime(data["날짜"])

# 메뉴 필터 만들기
menu_options = data["메뉴"].unique()
selected_menu = st.selectbox("메뉴를 선택하세요:", menu_options)

# 선택한 메뉴 데이터만 보기
filtered = data[data["메뉴"] == selected_menu]
st.subheader(f"'{selected_menu}' 선택 현황")
st.dataframe(filtered)

# 요일별 도시락 수량 합계
st.subheader("요일별 선택 수량")
sum_by_day = data.groupby("요일")["수량"].sum().sort_index()
st.bar_chart(sum_by_day)

# 학년별 인기 메뉴 보기
st.subheader("학년별 인기 메뉴")
popular_by_grade = data.groupby(["학년", "메뉴"])["수량"].sum().unstack()
st.bar_chart(popular_by_grade)

# 총 수량 확인
total = data["수량"].sum()
st.markdown(f"👉 **전체 도시락 선택 수량: {total}개**")

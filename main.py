import streamlit as st
import pandas as pd

st.title("🥗 도시락 선택 데이터 분석 앱")

# 데이터 불러오기
data = None  # 기본값 설정
raw = pd.read_csv("lunchdata.csv", encoding='cp949', header=None)
st.write(raw.head())


try:
    data = pd.read_csv("lunchdata.csv", encoding='cp949', sep=",")
    data.columns = data.columns.str.strip().str.replace('\ufeff', '')  # 열 이름 정리
    st.write("📋 데이터 미리보기", data.head())
    st.write("🧾 열 이름:", data.columns.tolist())
except FileNotFoundError:
    st.error("❌ 파일이 없습니다. 'lunchdata.csv' 파일을 같은 폴더에 넣어주세요.")
except Exception as e:
    st.error(f"❌ 오류 발생: {e}")

# 데이터가 성공적으로 불러졌을 때만 실행
if data is not None:

    # 날짜 형식 변환
    if "날짜" in data.columns:
        try:
            data["날짜"] = pd.to_datetime(data["날짜"])
        except:
            st.warning("📆 날짜 형식 변환 실패. 날짜 열이 올바른 형식인지 확인하세요.")
    else:
        st.warning("⚠️ '날짜' 열이 존재하지 않습니다.")
        st.write("🧾 열 이름 목록:", data.columns.tolist())

    # 메뉴 선택 필터
    if "메뉴" in data.columns:
        menu_options = data["메뉴"].unique()
        selected_menu = st.selectbox("메뉴를 선택하세요:", menu_options)

        filtered = data[data["메뉴"] == selected_menu]
        st.subheader(f"'{selected_menu}' 선택 현황")
        st.dataframe(filtered)
    else:
        st.error("⚠️ '메뉴' 열이 누락되었습니다.")
        st.stop()

    # 요일별 도시락 수량 합계 시각화
    if "요일" in data.columns and "수량" in data.columns:
        st.subheader("요일별 선택 수량")
        sum_by_day = data.groupby("요일")["수량"].sum().sort_index()
        st.bar_chart(sum_by_day)
    else:
        st.warning("⚠️ '요일' 또는 '수량' 열이 누락되었습니다.")

    # 학년별 인기 메뉴
    if "학년" in data.columns and "수량" in data.columns:
        st.subheader("학년별 인기 메뉴")
        popular_by_grade = data.groupby(["학년", "메뉴"])["수량"].sum().unstack()
        st.bar_chart(popular_by_grade)
    else:
        st.warning("⚠️ '학년' 또는 '수량' 열이 누락되었습니다.")

    # 전체 수량
    if "수량" in data.columns:
        total = data["수량"].sum()
        st.markdown(f"👉 **전체 도시락 선택 수량: {total}개**")


import streamlit as st
import matplotlib.pyplot as plt

st.title("🎉 간단 데이터 분석 & 시각화 앱")

# 한글 폰트 수동 지정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
plt.rcParams['axes.unicode_minus'] = False


# 샘플 데이터 만들기
data = {
    "이름": ["철수", "영희", "민수", "지현", "수민", "준호"],
    "국어": [85, 90, 78, 92, 88, 76],
    "수학": [80, 95, 70, 85, 90, 79],
    "영어": [88, 86, 75, 90, 92, 81]
}
df = pd.DataFrame(data)

st.write("### 학생 성적 데이터")
st.dataframe(df)

# 과목 선택 (국어, 수학, 영어 중 하나)
subject = st.selectbox("분석할 과목을 선택하세요", ["국어", "수학", "영어"])

# 선택한 과목 점수 분포 히스토그램
st.write(f"### {subject} 점수 분포")

fig, ax = plt.subplots()
ax.hist(df[subject], bins=5, color='skyblue', edgecolor='black')
ax.set_xlabel("점수")
ax.set_ylabel("학생 수")
ax.set_title(f"{subject} 점수 분포 히스토그램")

st.pyplot(fig)

# 기본 통계 정보 출력
st.write(f"### {subject} 기본 통계")
st.write(df[subject].describe())

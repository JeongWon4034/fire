import streamlit as st

# 페이지 설정
st.set_page_config(page_title="AI 지하수 오염 분석 시스템", layout="wide", page_icon="💧")

# 헤더
st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h1 style="font-size: 2.8rem;">💧 AI 지하수 오염 분석 시스템</h1>
        <p style="font-size: 1.2rem; color: gray;">프리미엄 지표 요약</p>
    </div>
""", unsafe_allow_html=True)

# 더미 값 (나중에 실제 값으로 교체)
num_sources = 128
num_detections = 64
num_types = 5
success_rate = 87.5

# 메트릭 박스 UI
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🏭 분석된 오염원", f"{num_sources}개소")

with col2:
    st.metric("⚠️ 오염 감지 지점", f"{num_detections}건")

with col3:
    st.metric("📊 오염원 유형", f"{num_types}종")

with col4:
    st.metric("📈 분석 성공률", f"{success_rate:.1f}%")

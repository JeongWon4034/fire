import streamlit as st

# 페이지 설정
st.set_page_config(page_title="AI 지하수 오염 분석 시스템", layout="wide", page_icon="💧")

# 프리미엄 스타일 정의
st.markdown("""
<style>
    .metric-container {
        display: flex;
        justify-content: space-around;
        margin-top: 2rem;
    }

    .metric-box {
        flex: 1;
        margin: 0 1rem;
        padding: 2rem;
        background: #f4f6fa;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        text-align: center;
        transition: transform 0.3s ease;
    }

    .metric-box:hover {
        transform: translateY(-5px);
    }

    .metric-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }

    .metric-value {
        font-size: 2.8rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# 상단 제목
st.markdown("""
<div style="text-align: center; padding-top: 2rem;">
    <h1 style="font-size: 2.8rem;">💧 AI 지하수 오염 분석 시스템</h1>
    <p style="font-size: 1.2rem; color: gray;">프리미엄 핵심 지표</p>
</div>
""", unsafe_allow_html=True)

# 더미 값
num_sources = 128
num_detections = 64
num_types = 5
success_rate = 87.5

# 네모 박스 4개 출력
st.markdown(f"""
<div class="metric-container">
    <div class="metric-box">
        <div class="metric-title">🏭 분석된 오염원</div>
        <div class="metric-value">{num_sources}개소</div>
    </div>
    <div class="metric-box">
        <div class="metric-title">⚠️ 오염 감지 지점</div>
        <div class="metric-value">{num_detections}건</div>
    </div>
    <div class="metric-box">
        <div class="metric-title">📊 오염원 유형</div>
        <div class="metric-value">{num_types}종</div>
    </div>
    <div class="metric-box">
        <div class="metric-title">📈 분석 성공률</div>
        <div class="metric-value">{success_rate:.1f}%</div>
    </div>
</div>
""", unsafe_allow_html=True)

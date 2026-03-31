import streamlit as st
from ai_engine import generate_ddr

st.set_page_config(
    page_title="DDR Generator",
    page_icon="🏗️",
    layout="wide"
)

st.markdown("""
<style>
.main { padding: 2rem; }
.block-container { padding-top: 2rem; }
.section-card {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
.title { font-size: 32px; font-weight: 700; }
.subtitle { color: #6c757d; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🏗️ DDR Report Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload any inspection & thermal files to generate DDR report</div>', unsafe_allow_html=True)


def read_file(file):
    if file is None:
        return ""
    raw_bytes = file.read()
    try:
        return raw_bytes.decode("utf-8")
    except:
        return str(raw_bytes)


col1, col2 = st.columns(2)

with col1:
    inspection_file = st.file_uploader("Upload inspection file", key="inspection")

with col2:
    thermal_file = st.file_uploader("Upload thermal file", key="thermal")

inspection_text = read_file(inspection_file)
thermal_text = read_file(thermal_file)

st.markdown("---")

center_col = st.columns([1, 2, 1])
with center_col[1]:
    generate = st.button("🚀 Generate DDR Report", use_container_width=True)

if generate:
    if not inspection_text and not thermal_text:
        st.warning("⚠️ Please upload at least one file")
    else:
        with st.spinner("Generating DDR report..."):
            ddr = generate_ddr(inspection_text, thermal_text)

            st.markdown("## 📄 Generated DDR Report")

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.text(ddr)
            st.markdown('</div>', unsafe_allow_html=True)

            st.download_button(
                "📥 Download Report",
                ddr,
                file_name="ddr_report.txt",
                mime="text/plain"
            )
import streamlit as st
from ai_engine import generate_ddr

st.set_page_config(
    page_title="DDR Report Generator",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding: 2rem;
}
.block-container {
    padding-top: 2rem;
}
.section-card {
    background-color: #f5f7fa;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    border: 1px solid #e0e0e0;
}
.title {
    font-size: 30px;
    font-weight: 700;
    color: #222;
}
.subtitle {
    color: #666;
    margin-bottom: 20px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">DDR Report Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload inspection and thermal reports to generate structured DDR output</div>', unsafe_allow_html=True)


def read_file(file):
    if file is None:
        return ""

    try:
        return file.read().decode("utf-8")
    except:
        return str(file.read())


col1, col2 = st.columns(2)

with col1:
    inspection_file = st.file_uploader("Upload Inspection Report", key="inspection")

with col2:
    thermal_file = st.file_uploader("Upload Thermal Report", key="thermal")


inspection_text = read_file(inspection_file)
thermal_text = read_file(thermal_file)

st.markdown("---")

center_col = st.columns([1, 2, 1])
with center_col[1]:
    generate = st.button("Generate DDR Report", use_container_width=True)

if generate:
    if not inspection_text and not thermal_text:
        st.warning("Please upload at least one file to continue")
    else:
        with st.spinner("Processing reports and generating DDR output..."):
            ddr = generate_ddr(inspection_text, thermal_text)

            st.markdown("### Generated DDR Report")

            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.text(ddr)
            st.markdown('</div>', unsafe_allow_html=True)

            st.download_button(
                label="Download Report",
                data=ddr,
                file_name="ddr_report.txt",
                mime="text/plain"
            )
import streamlit as st
from PIL import Image
import os
import sys

sys.path.append(os.path.abspath("."))
from src.vision import detect_ppe
from src.agent import audit_ppe_compliance, answer_safety_query

st.set_page_config(
    page_title="MineGuard AI | Statutory Safety Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Vibrant Glassmorphic & 3D CSS Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    /* Make the top Streamlit header completely transparent */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }

    /* Global canvas & vibrant mesh background */
    .stApp {
        background: radial-gradient(circle at 15% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
                    radial-gradient(circle at 85% 15%, rgba(168, 85, 247, 0.14) 0%, transparent 45%),
                    radial-gradient(circle at 50% 80%, rgba(14, 165, 233, 0.10) 0%, transparent 50%),
                    linear-gradient(135deg, #090d16 0%, #0c1220 50%, #080c14 100%);
        background-attachment: fixed;
        color: #f1f5f9;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3.5rem;
        max-width: 1220px;
    }

    /* Vibrant Gradient Header */
    .brand-title {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(120deg, #38bdf8 0%, #818cf8 40%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        text-shadow: 0 8px 30px rgba(56, 189, 248, 0.25);
    }
    .brand-caption {
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }

    /* Glassmorphism Cards & Containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(18, 26, 45, 0.55) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 255, 255, 0.10) !important;
        border-radius: 16px !important;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.6),
                    inset 0 1px 1px 0 rgba(255, 255, 255, 0.12) !important;
        padding: 1.4rem !important;
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(56, 189, 248, 0.35) !important;
        box-shadow: 0 16px 36px -10px rgba(14, 165, 233, 0.25),
                    inset 0 1px 1px 0 rgba(255, 255, 255, 0.2) !important;
    }

    /* 3D Glass Action Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.85) 0%, rgba(99, 102, 241, 0.90) 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.03em !important;
        border-radius: 10px !important;
        padding: 0.65rem 1.6rem !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        box-shadow: 0 4px 14px 0 rgba(14, 165, 233, 0.4),
                    0 4px 0 0 #3730a3,
                    inset 0 1px 1px 0 rgba(255, 255, 255, 0.4) !important;
        transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 22px 0 rgba(99, 102, 241, 0.55),
                    0 6px 0 0 #3730a3,
                    inset 0 1px 1px 0 rgba(255, 255, 255, 0.5) !important;
        filter: brightness(1.1);
    }
    div.stButton > button:active {
        transform: translateY(3px) !important;
        box-shadow: 0 2px 6px 0 rgba(14, 165, 233, 0.3),
                    0 1px 0 0 #3730a3,
                    inset 0 1px 1px 0 rgba(0, 0, 0, 0.2) !important;
    }

    /* 3D Modern Glass Tabs */
    [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(15, 23, 42, 0.6) !important;
        padding: 6px 8px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        margin-bottom: 1.5rem;
    }
    [data-baseweb="tab"] {
        border-radius: 8px !important;
        padding: 8px 18px !important;
        color: #94a3b8 !important;
        font-weight: 600 !important;
        background: transparent !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }
    [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(51, 65, 85, 0.7) 100%) !important;
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.35) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.35),
                    inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
    }
    [data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }

    /* Camera Module Constraints */
    [data-testid="stCameraInput"] {
        max-width: 440px;
        margin: 0 auto;
    }
    [data-testid="stCameraInput"] video {
        border-radius: 12px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    /* Typography & Visual Accents */
    h4, h5 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    code {
        font-family: 'JetBrains Mono', monospace !important;
        color: #38bdf8 !important;
        background: rgba(14, 165, 233, 0.12) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 4px;
        padding: 2px 6px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="brand-title">MineGuard AI</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-caption">Autonomous Computer Vision & DGMS Statutory Safety Platform</div>', unsafe_allow_html=True)

def run_pipeline(image: Image.Image):
    # Top Box: Vision Inference
    with st.container(border=True):
        st.markdown("#### Vision Inference (YOLOv8)")
        with st.spinner("Processing frame..."):
            annotated_img, detections = detect_ppe(image)
        
        # Constrain image width so it doesn't stretch massively on wide screens
        col_img, col_spacer = st.columns([1, 1])
        with col_img:
            st.image(annotated_img, caption="Object Detection Output", use_container_width=True)
        
        entities = ", ".join(list(set(detections))) if detections else "None Detected"
        st.markdown(f"**Identified Entities:** `{entities}`")
        
    # Bottom Box: Statutory Safety Audit (Full Width)
    with st.container(border=True):
        st.markdown("#### Statutory Safety Audit")
        with st.spinner("Evaluating compliance against DGMS & Mines Act provisions..."):
            audit_report = audit_ppe_compliance(detections)
        st.markdown(audit_report)
        
# Navigation Tabs
tab_demo, tab_upload, tab_camera = st.tabs(["Live Demo", "Upload Frame", "Live Camera Capture"])

# Tab 1: Live Demo Benchmarks
with tab_demo:
    with st.container(border=True):
        st.markdown("##### Standard Benchmark Cases")
        demo_choice = st.radio(
            "Select Field Test Scenario:",
            ["Scenario A: Non-Compliant Worker (No Hard Hat)", "Scenario B: Compliant Pit Operative"],
            horizontal=True
        )
        
        sample_file = "non_compliant.jpg" if "Non-Compliant" in demo_choice else "compliant_worker.jpg"
        sample_path = os.path.join("data", "samples", sample_file)
        
        col_prev, col_btn = st.columns([1, 2])
        if os.path.exists(sample_path):
            with col_prev:
                st.image(sample_path, width=220, caption="Scenario Preview")
            with col_btn:
                st.write("")
                st.write("")
                if st.button("Run Compliance Analysis"):
                    run_pipeline(Image.open(sample_path))
        else:
            st.info("Place benchmark images in `data/samples/` to enable 1-click execution.")

# Tab 2: Upload Frame
with tab_upload:
    with st.container(border=True):
        uploaded_file = st.file_uploader("Select high-resolution inspection image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            run_pipeline(Image.open(uploaded_file))

# Tab 3: Constrained Live Camera
with tab_camera:
    with st.container(border=True):
        st.markdown("##### Video Capture Station")
        col_spacer_l, col_cam, col_spacer_r = st.columns([1, 2, 1])
        with col_cam:
            camera_image = st.camera_input("Capture inspection frame")
        
        if camera_image:
            run_pipeline(Image.open(camera_image))

# Copilot Section
st.write("")
st.markdown("### Statutory Safety Copilot")
st.caption("Direct query engine for DGMS Circulars, Metalliferous Mines Regulations (MMR), Coal Mines Regulations (CMR), and Section 72C penalties.")

user_query = st.text_input("Enter regulatory query:", placeholder="e.g. What are the mandatory penal actions under Section 72C?")

if user_query:
    with st.container(border=True):
        with st.spinner("Searching regulatory index..."):
            answer = answer_safety_query(user_query)
        st.markdown(answer)
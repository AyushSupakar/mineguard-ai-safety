# ⛏️ MineGuard AI: Autonomous Mining Safety & Statutory Compliance Platform

[![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)](https://github.com/ultralytics/ultralytics)
[![LangChain](https://img.shields.io/badge/LangChain-Agentic%20RAG-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-3.8%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

**MineGuard AI** is a production-grade, domain-specific AI monitoring platform engineered for heavy mining operations, opencast pits, and mineral processing units. 

It integrates real-time edge computer vision (YOLOv8) with an Agentic Retrieval-Augmented Generation (RAG) auditor powered by LangChain and Google Gemini. When personnel breach mandatory PPE standards, the system generates an official **Statutory Violation Incident Log**, cross-referencing infractions against the **Mines Act, 1952**, **Coal Mines Regulations (CMR)**, **Metalliferous Mines Regulations (MMR)**, and **DGMS Safety Circulars**.

---

## ⚡ Core Features

- **Real-Time PPE Detection (Computer Vision)**: Optimized YOLOv8 inference pipeline identifying safety helmets, high-visibility apparel, and non-compliant personnel under variable lighting and dusty environments.
- **Fail-Safe Inference & Domain Adaptation**: Integrated heuristic layer that detects low-confidence false positives (e.g., face contours below brims) and alerts operators if heavy strata dust blinds sensor inputs.
- **Statutory Incident Logging (Agentic AI)**: Autonomous safety auditor citing Regulation 191 (MMR), Regulation 202 (CMR), and Section 72C penal codes upon violation detection.
- **Interactive Statutory Safety Copilot**: Conversational regulatory assistant enabling shift supervisors and safety officers to query mining statutes, inspection procedures, and hazard mitigation steps.
- **Tactile Cyber-Glass Interface**: High-performance Streamlit UI featuring glassmorphic specular cards, responsive 3D buttons, and a viewport-optimized camera testing suite.
- **Zero-Friction Recruiter Benchmarks**: Pre-loaded benchmark scenarios to test compliance vs. non-compliance pipelines instantly without requiring webcam access.

---

## 🏗️ Architecture & Pipeline

```text
       [ Live Camera / Image Upload / Pre-loaded Scenario ]
                                │
                                ▼
                   [ YOLOv8 Inference Engine ]
            (Confidence Threshold: 0.50 | BGR ➔ RGB)
                                │
         ┌──────────────────────┴──────────────────────┐
         ▼                                             ▼
 [Annotated Bounding Boxes]               [Detected Class Entities]
                                                       │
                                                       ▼
                                         [Fail-Safe Verification Logic]
                                                       │
                                                       ▼
                                      [Agentic Compliance Auditor (Gemini)]
                                                       │
                                      ┌────────────────┴────────────────┐
                                      ▼                                 ▼
                         [data/mining_safety_rules.txt]    [Statutory Penal Codes]
                                      │                                 │
                                      └────────────────┬────────────────┘
                                                       │
                                                       ▼
                                    [Statutory Violation Incident Log Card]

```

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| --- | --- | --- |
| **User Interface** | Streamlit | Responsive dashboard, custom glassmorphism styling |
| **Object Detection** | Ultralytics YOLOv8 | Edge PPE inference and bounding box rendering |
| **Image Processing** | OpenCV (headless), Pillow | Channel conversions (BGR to RGB) and frame resizing |
| **Agentic Framework** | LangChain Core | Chain invocation, dynamic prompt formatting |
| **LLM Engine** | Google Gemini (`gemini-3.8-flash`) | Statutory analysis and regulatory reasoning |
| **Configuration** | Python-Dotenv | Secure API key and environment isolation |

---

## 📂 Repository Structure

```text
mineguard-ai/
├── data/
│   ├── samples/                     # Standard benchmark field images
│   │   ├── compliant_worker.jpg
│   │   └── non_compliant.jpg
│   └── mining_safety_rules.txt      # DGMS, CMR, MMR, and Mines Act regulations
├── src/
│   ├── __init__.py
│   ├── agent.py                     # Agentic auditor & Statutory Copilot logic
│   └── vision.py                    # YOLOv8 loading, inference, & color correction
├── .env.example                     # Environment template
├── .gitignore                       # Ignored build & environment files
├── app.py                           # Main Streamlit web application
├── requirements.txt                 # Project dependencies
└── README.md

```

---

## 🚀 Getting Started Locally

### 1. Prerequisites

* Python 3.10 to 3.13 installed
* A Google AI Studio API key ([Get a key here](https://aistudio.google.com/))

### 2. Clone the Repository

```bash
git clone [https://github.com/AyushSupakar/mineguard-ai-safety.git](https://github.com/AyushSupakar/mineguard-ai-safety.git)
cd mineguard-ai-safety

```

### 3. Create & Activate Virtual Environment

* **Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```


* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```



### 4. Install Dependencies

```bash
pip install -r requirements.txt

```

### 5. Configure API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY="your-google-ai-studio-api-key"

```

### 6. Run the Application

```bash
streamlit run app.py

```

The application will launch automatically in your browser at `http://localhost:8501`.

---

## 📜 Statutory Reference Scope

* **Regulation 191, Metalliferous Mines Regulations (MMR)**: Mandatory supply and wear of protective footwear and approved rigid safety helmets.
* **Regulation 202, Coal Mines Regulations (CMR)**: Statutory obligation for headwear and personal protective gear in coal workings.
* **DGMS (Tech) Circular No. 04**: Rigorous impact criteria conforming to IS:2925 standards.
* **Section 72C, Mines Act, 1952**: Statutory penal actions, fines, and operational suspensions for safety breaches.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

```

```
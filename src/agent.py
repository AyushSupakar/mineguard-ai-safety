import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def audit_ppe_compliance(detections: list) -> str:
    # Filter for non-compliance classes
    violations = [d for d in detections if "no-" in d.lower() or "without" in d.lower()]
    
    if not violations:
        return "✅ **Statutory Compliance Verified**: All detected personnel adhere to mandatory PPE protocols."

    # Load local statutory text
    rules_path = os.path.join("data", "mining_safety_rules.txt")
    if os.path.exists(rules_path):
        with open(rules_path, "r", encoding="utf-8") as f:
            regulations = f.read()
    else:
        regulations = "General Mines Safety Regulations apply."

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return f"⚠️ **Alert**: Infraction detected ({', '.join(violations)}), but `GEMINI_API_KEY` is not set in `.env`."

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0.2
    )

    prompt = PromptTemplate(
        input_variables=["violations", "regulations"],
        template="""
You are an autonomous AI Mine Safety Auditor operating under statutory Mining Acts and DGMS circulars.

Detected Site Violations: {violations}
Statutory Regulations:
{regulations}

Generate a concise, professional "Statutory Violation Incident Log":
1. **Infraction Summary**: State what safety breach was visually flagged.
2. **Statutory Reference**: Cite the exact relevant Regulation/Rule from the context.
3. **Hazard Risk Level**: High / Critical / Moderate with engineering reason.
4. **Immediate Corrective Action**: Concrete instruction for the Shift In-Charge / Mining Sirdar.

Keep the response structured, authoritative, and direct.
"""
    )

    chain = prompt | llm
    response = chain.invoke({"violations": ", ".join(violations), "regulations": regulations})
    
    # Clean extraction: handles both string responses and SDK chunk lists
    raw_content = response.content
    if isinstance(raw_content, str):
        return raw_content
    elif isinstance(raw_content, list):
        text_blocks = [
            chunk["text"] if isinstance(chunk, dict) and "text" in chunk else str(chunk)
            for chunk in raw_content
        ]
        return "\n".join(text_blocks)
        
    return str(raw_content)

def answer_safety_query(query: str, chat_history: list = None) -> str:
    rules_path = os.path.join("data", "mining_safety_rules.txt")
    if os.path.exists(rules_path):
        with open(rules_path, "r", encoding="utf-8") as f:
            regulations = f.read()
    else:
        regulations = "General Mines Safety Regulations apply."

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "⚠️ `GEMINI_API_KEY` is missing."

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",  # Update this line
        google_api_key=api_key,
        temperature=0.2
    )

    prompt = PromptTemplate(
        input_variables=["regulations", "query"],
        template="""
You are an expert DGMS Mine Safety Regulatory Officer. Answer the user's question accurately using the statutory context provided below.

Statutory Context:
{regulations}

Question: {query}

Provide a direct, authoritative, and concise answer citing relevant rules where applicable.
"""
    )

    chain = prompt | llm
    response = chain.invoke({"regulations": regulations, "query": query})

    raw_content = response.content
    if isinstance(raw_content, str):
        return raw_content
    elif isinstance(raw_content, list):
        return "\n".join([c["text"] if isinstance(c, dict) and "text" in c else str(c) for c in raw_content])
    return str(raw_content)
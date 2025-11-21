# 🏥 Dia-Agent: Privacy-First Clinical Support System

<img width="2816" height="1536" alt="Gemini_Generated_Image_7stsv37stsv37sts" src="https://github.com/user-attachments/assets/ffcd88de-01a8-449e-9d0e-bb40372f45ce" />


![Dia-Agent Banner](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Track](https://img.shields.io/badge/Track-Agents_for_Good-blue?style=for-the-badge)

**Dia-Agent** is a specialized multi-agent system designed to assist medical professionals in diagnosing and managing diabetes risks. Unlike standard chatbots, it implements strict **Clinical Safety Protocols**, including **Human-in-the-Loop (HITL)** verification for critical alerts and **Long-term Memory** for personalized patient care.

🩺 **Use Case**: Clinical decision support, patient lifestyle coaching, and chronic disease management.

🧠 **Technologies**:
![Google ADK](https://img.shields.io/badge/Google_ADK-0.1.x-4285F4?logo=google)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-8E75B2?logo=google)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas)

---

## 🦄 _**Code Requirements**_
- Python 3.10 or later
- A Google Cloud Project with **Generative Language API** enabled
- A valid **Google API Key**
- Required libraries: `google-adk`, `google-genai`, `python-dotenv`, `pandas`

---

## 🔍 _**Problem Statement**_

Diabetes affects millions worldwide, but personalized care is resource-intensive. While AI can analyze data faster than humans, **"hallucinations" in medical advice can be fatal**.

Standard LLMs lack:
1.  **Deterministic Safety:** They might miss a critical high-risk indicators.
2.  **Contextual Continuity:** They forget patient history (allergies, preferences) between sessions.
3.  **Accountability:** They cannot be "paused" for doctor review before sending critical alerts.

**Dia-Agent solves this** by combining deterministic clinical rules with generative empathy, enforced by a strict human-in-the-loop architecture.

---

## 🎯 _**Key Features**_

- 🤝 **Sequential Multi-Agent Architecture**: Separates clinical analysis (hard logic) from lifestyle coaching (soft skills).
- 🛑 **Human-in-the-Loop Safety**: The system **automatically PAUSES** execution when High Risk is detected, waiting for a doctor's digital signature/approval before proceeding.
- 🧠 **Long-Term Memory**: Remembers patient specifics (e.g., "Vegan", "Swimmer") across sessions to tailor advice.
- 📊 **Data-Driven Logic**: Risk calculation rules are derived from Random Forest analysis on 10,000+ patient records.
- 🔒 **Privacy-First**: Designed to run locally (VS Code) to ensure patient data handling control.

---

## 🧠 **Machine Learning Foundation**
Unlike standard chatbots that "guess," Dia-Agent's risk assessment logic is grounded in rigorous data science.
* **Model:** A Stacking Ensemble Classifier (LightGBM, XGBoost, CatBoost) trained on patient health data.
* **Validation:** Validated using Stratified K-Fold Cross-Validation (10 folds) to ensure clinical reliability.
* **Key Predictors:** Uses SMOTE to identify critical risk factors: Fasting Glucose, BMI, and Hypertension.
* **Safety:** The agent uses these data-derived thresholds to trigger the "Human-in-the-Loop" safety pause.
---

## 🛠️ _**Tech Stack**_
- **Google Agent Development Kit (ADK)**: For agent orchestration and state management.
- **Gemini 2.0 Flash**: The reasoning engine for the agents.
- **InMemorySessionService**: For managing active conversation context.
- **InMemoryMemoryService**: For storing long-term patient history.
- **ADK Logging Plugin**: For full observability and tracing of agent thoughts.

---

## 📌 _**Architecture & How It Works**_

The system utilizes a **Sequential Agent Pipeline** (`SequentialAgent`) to ensure tasks are performed in a specific order.

### **The Workflow**

1.  **Data Ingestion**: Patient vitals (Glucose, BMI, Age) are fed into the system.
2.  **Agent 1: Clinical Analyst**:
    * Uses a deterministic tool `calculate_clinical_risk` (Python logic, not LLM guess) to score the patient.
    * If **High Risk** is detected, it calls `notify_doctor_critical`.
    * **🛑 SYSTEM PAUSE**: The ADK `Resumability` feature halts the agent. The system waits for a human signal.
3.  **Human-in-the-Loop**: A doctor reviews the data and clicks "Approve".
4.  **Agent 2: Lifestyle Coach**:
    * Resumes execution.
    * Queries **Long-term Memory** to find patient preferences (e.g., "Vegan").
    * Generates a diet/exercise plan that combines the **Clinical Risk** with **Personal Preferences**.

```plaintext
                    +---------------------------+
                    |   Patient Clinical Data   |
                    |  (Glucose, BMI, Age...)   |
                    +-------------+-------------+
                                  |
                                  v
                   +-----------------------------+
                   |  Agent 1: Clinical Analyst  |
                   | (Deterministic Logic Tool)  |
                   +--------------+--------------+
                                  |
                                  v
                       +----------------------+
                       |   Risk Calculation   |
                       +----------+-----------+
                                  |
                  +---------------+---------------+
                  |                               |
            [High Risk]                      [Low Risk]
                  |                               |
                  v                               |
     +-------------------------+                  |
     | 🛑 SYSTEM PAUSE (ADK)   |                  |
     | Notify Doctor Tool      |                  |
     +------------+------------+                  |
                  |                               |
                  v                               |
     +-------------------------+                  |
     | 👨‍⚕️ Doctor Approval     |                  |
     | (Human-in-the-Loop)     |                  |
     +------------+------------+                  |
                  |                               |
                  v                               v
      +-----------------------------------------------+
      |         Agent 2: Lifestyle Coach              |
      |       (Empathetic Generative AI)              |
      +-----------------------+-----------------------+
                              |
                              v
              +-------------------------------+
              |   🧠 Long-Term Memory Check   |
              | (Retrieves: "Vegan", "Swim")  |
              +---------------+---------------+
                              |
                              v
              +-------------------------------+
              |   ✅ Final Personalized Plan  |
              |  (Medical + Lifestyle Advice) |
              +-------------------------------+
```

---

## 👨‍🔬 _Clinical Logic_

The agent does not "guess" diabetes risk. It uses strict clinical thresholds derived from data analysis:

* **High Glucose:** > 125 mg/dL (+3 points)
* **Elevated Glucose:** > 100 mg/dL (+1 point)
* **Obesity:** BMI > 30 (+2 points)
* **Hypertension:** Yes (+1 point)
* **Age:** > 45 (+1 point)

**Risk Classification:**

* **HIGH (Score ≥ 3):** Immediate Doctor Notification Required.
* **MODERATE (Score ≥ 1):** Lifestyle modification.
* **LOW:** Routine checkup.

---

## 🐉 _Execution Steps_

### **1. Clone & Install**
```bash
git clone [https://github.com/Preethi-K-N/Dia-Agent-Diabetes-Capstone.git](https://github.com/Preethi-K-N/Dia-Agent-Diabetes-Capstone.git)
cd Dia-Agent-Diabetes-Capstone
pip install -r requirements.txt
```
### **2. Configure Security**
Create a `.env` file in the root directory and add your Google API Key:

```ini
GOOGLE_API_KEY=your_actual_api_key_here
```
### **3. Run the Simulation**
Run the main agent script. This will simulate a full patient interaction, including the pause for doctor approval.
```bash
python Dia_Agent_Capstone.py
```

---

## 🗂 _**Folder Structure**_
```
Dia-Agent-Diabetes-Capstone
│
├── diabetes_tools.py        # Custom Clinical Tools (The Logic Layer)
├── Dia_Agent_Capstone.py    # Agent Orchestration & Runner (The Application Layer)
├── requirements.txt         # Project Dependencies
├── .env                     # API Keys (Not uploaded to GitHub)
├── README.md                # Project Documentation
│
└── research_and_analysis/   # Data Science Background
    ├── ML_code.ipynb        # Original ML Model Training
    └── dataset.csv          # Dataset used for logic derivation
```

---

## 📌 _Citation & References_
* **Google ADK Documentation:** https://google.github.io/adk-docs/
* **Gemini Models:** https://ai.google.dev/models
* **Dataset:** Synthetic Healthcare Data (Analysis provided in `research_and_analysis` folder).

---

## ⚖️ _Disclaimer_
*This is a prototype for the Kaggle AI Agents competition. While based on real clinical metrics, it should not be used for actual medical diagnosis without further clinical validation.*

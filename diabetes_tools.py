from google.adk.tools.tool_context import ToolContext

def calculate_clinical_risk(glucose: float, bmi: float, age: int, hypertension: int) -> dict:
    """
    Analyzes patient metrics to determine Diabetes Risk Level.
    Derived from Random Forest analysis of clinical data.
    """
    risk_score = 0
    risk_factors = []

    # Clinical Rules
    if glucose > 125:
        risk_score += 3
        risk_factors.append("High Glucose (>125 mg/dL)")
    elif glucose > 100:
        risk_score += 1
        risk_factors.append("Elevated Glucose")

    if bmi > 30:
        risk_score += 2
        risk_factors.append("Obesity (BMI > 30)")

    if hypertension == 1:
        risk_score += 1
        risk_factors.append("Hypertension")

    if age > 45:
        risk_score += 1

    # Risk Classification
    if risk_score >= 3:
        return {
            "risk_level": "HIGH", 
            "score": risk_score, 
            "factors": risk_factors, 
            "advice": "Immediate medical consultation required."
        }
    elif risk_score >= 1:
        return {
            "risk_level": "MODERATE", 
            "score": risk_score, 
            "factors": risk_factors, 
            "advice": "Lifestyle modification recommended."
        }
    else:
        return {
            "risk_level": "LOW", 
            "score": risk_score, 
            "factors": risk_factors, 
            "advice": "Routine checkup schedule."
        }

def notify_doctor_critical(risk_level: str, patient_id: str, tool_context: ToolContext) -> dict:
    """
    Safety Protocol: Pauses execution if Risk is HIGH to get Human Doctor Approval.
    """
    # 1. Auto-approve low/moderate risk
    if risk_level != "HIGH":
        return {"status": "logged", "message": f"Risk is {risk_level}. Logged to internal system."}

    # 2. First Call: Trigger Pause
    if not tool_context.tool_confirmation:
        print(f"\n[SYSTEM ALERT] 🛑 HIGH RISK DETECTED for {patient_id}. Pausing for Doctor Approval...")

        tool_context.request_confirmation(
            hint=f"Approve Critical Alert for {patient_id}?",
            payload={"patient_id": patient_id, "risk": risk_level}
        )
        return {"status": "pending", "message": "Waiting for human doctor approval."}

    # 3. Resumed Call: Process Decision
    if tool_context.tool_confirmation.confirmed:
        return {"status": "sent", "message": f"✅ ALERT SENT to Dr. Smith for {patient_id}."}
    else:
        return {"status": "rejected", "message": "❌ Alert cancelled by supervisor."}

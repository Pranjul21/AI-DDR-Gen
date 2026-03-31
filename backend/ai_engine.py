def generate_ddr(inspection_text: str, thermal_text: str) -> str:
    text = (inspection_text + " " + thermal_text).lower()

    issues = set()

    if "crack" in text:
        issues.add("Structural Damage")

    if any(word in text for word in ["leak", "damp", "moisture"]):
        issues.add("Water Leakage")

    if any(word in text for word in ["temperature", "heat"]):
        issues.add("Thermal Irregularity")

    if "corrosion" in text:
        issues.add("Material Degradation")

    if "mold" in text:
        issues.add("Mold Growth")

    issues = list(issues)

    severity_map = {
        "Structural Damage": "High",
        "Water Leakage": "Medium",
        "Thermal Irregularity": "Medium",
        "Material Degradation": "Medium",
        "Mold Growth": "High"
    }

    summary = ", ".join(issues) if issues else "No major issues detected"

    observations = "\n".join([f"- {i}" for i in issues]) if issues else "- Not Available"

    severity = "\n".join([
        f"- {i}: {severity_map.get(i, 'Low')}" for i in issues
    ]) if issues else "- Not Available"

    recommendations_map = {
        "Structural Damage": "Repair structural cracks immediately",
        "Water Leakage": "Fix leakage and improve waterproofing",
        "Thermal Irregularity": "Inspect insulation and heat sources",
        "Material Degradation": "Replace or treat affected materials",
        "Mold Growth": "Remove mold and improve ventilation"
    }

    recommendations = [
        recommendations_map[i] for i in issues if i in recommendations_map
    ]

    recommendations_text = "\n".join([f"- {r}" for r in recommendations]) if recommendations else "- General inspection recommended"

    ddr = f"""
1. Property Issue Summary
{summary}

2. Area-wise Observations
{observations}

3. Probable Root Cause
- Issues likely caused by environmental exposure, poor maintenance, or construction defects

4. Severity Assessment
{severity}

5. Recommended Actions
{recommendations_text}

6. Additional Notes
- This report is generated using rule-based analysis without external AI services

7. Missing or Unclear Information
- Not Available
"""

    return ddr
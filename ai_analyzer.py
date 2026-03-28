# -*- coding: utf-8 -*-
import json
import os
from groq import Groq


def analyze_email_for_phishing(subject: str, sender: str, body: str) -> dict:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""You are a cybersecurity expert specializing in phishing email detection.
Analyze the following email and determine if it is a phishing attempt.

EMAIL DETAILS:
--------------
From: {sender}
Subject: {subject}

Body:
{body}

--------------
Provide your analysis in the following JSON format ONLY (no extra text, no markdown):
{{
  "is_phishing": true or false,
  "score": <integer from 0 to 100>,
  "verdict": "<one of: SAFE, SUSPICIOUS, PHISHING>",
  "confidence": "<one of: LOW, MEDIUM, HIGH>",
  "reasons": ["<reason 1>", "<reason 2>", "<reason 3>"],
  "red_flags": ["<red flag if any>"],
  "recommendation": "<short advice>"
}}

Scoring guide:
- 0-25: Likely safe
- 26-50: Suspicious, proceed with caution
- 51-75: Likely phishing
- 76-100: Definitely phishing"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Free open source model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.1
    )

    response_text = response.choices[0].message.content.strip()

    # Clean markdown if present
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        response_text = "\n".join(lines[1:-1])

    result = json.loads(response_text)
    return result


def format_analysis_report(email_data: dict, analysis: dict) -> str:
    score = analysis.get("score", 0)
    verdict = analysis.get("verdict", "UNKNOWN")
    is_phishing = analysis.get("is_phishing", False)
    confidence = analysis.get("confidence", "LOW")
    reasons = analysis.get("reasons", [])
    red_flags = analysis.get("red_flags", [])
    recommendation = analysis.get("recommendation", "")

    filled = int(score / 5)
    bar = "#" * filled + "-" * (20 - filled)

    if verdict == "SAFE":
        verdict_icon = "[SAFE]"
    elif verdict == "SUSPICIOUS":
        verdict_icon = "[SUSPICIOUS]"
    else:
        verdict_icon = "[PHISHING]"

    report = f"""
{'='*60}
EMAIL ANALYSIS REPORT
{'='*60}
From    : {email_data['sender']}
Subject : {email_data['subject']}
{'='*60}

{verdict_icon}
VERDICT        : {verdict}
PHISHING SCORE : [{bar}] {score}/100
IS PHISHING    : {"YES - DANGER" if is_phishing else "NO - SAFE"}
CONFIDENCE     : {confidence}

REASONS:
"""
    for i, reason in enumerate(reasons, 1):
        report += f"  {i}. {reason}\n"

    if red_flags:
        report += "\nRED FLAGS:\n"
        for flag in red_flags:
            report += f"  - {flag}\n"

    report += f"\nRECOMMENDATION:\n  {recommendation}\n"
    report += "=" * 60 + "\n"

    return report
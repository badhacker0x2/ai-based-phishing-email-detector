[README.md](https://github.com/user-attachments/files/26320628/README.md)
# 🛡️ AI-Based Phishing Email Detector

> AI-POWERED PHISHING EMAIL DETECTOR

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Model](https://img.shields.io/badge/Model-Groq%20LLaMA%203.3-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red?style=flat-square&logo=linux)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9C%93-brightgreen?style=flat-square)

Reads your emails, passes them to an open-source AI, and determines whether they are phishing attempts — with a detailed risk score and full analysis report.

---

## 📚 Table of Contents

- [Authors](#-authors)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Scoring Guide](#-scoring-guide)
- [Sample Output](#-sample-output)
- [Error Handling](#-error-handling)
- [Security](#-security-best-practices)

---

## 👨‍💻 Authors

| Role | Name |
|------|------|
| 🧠 Project Lead & Core Development | **Md. Munkasiur Haque** |
| 🔧 Error Handling & Debugging | **Rahat Sahriar Rafi** |

---

## ✨ Features

- 📬 Reads emails via IMAP — supports Gmail, Outlook, and more
- 🤖 Powered by LLaMA 3.3 70B via Groq — free & open source
- 📊 Phishing risk score from 0 to 100 with detailed breakdown
- 🚦 Verdict: `SAFE`, `SUSPICIOUS`, or `PHISHING` with confidence level
- 🚩 Lists specific red flags and reasons for every verdict
- 🧪 Demo mode — test without any email credentials
- 🐧 Fully ASCII-compatible — works perfectly on Kali Linux
- 🔑 No credit card required — 100% free API via Groq

---

## 📁 Project Structure

```
ai-based-phishing-email-detector/
├── main.py           # Entry point, user interaction & report output
├── email_reader.py   # Connects to email via IMAP, fetches messages
├── ai_analyzer.py    # Sends email to AI, parses phishing analysis
├── requirements.txt  # Python dependencies
├── .env              # API key storage (NEVER commit this)
├── .gitignore        # Excludes .env and venv from GitHub
└── README.md         # This file
```

---

## ⚙️ Requirements

| Requirement | Details |
|-------------|---------|
| **Python** | 3.10 or higher |
| **Groq API Key** | Free — no credit card required |
| **Internet** | Required for AI analysis and IMAP |
| **Gmail (optional)** | IMAP enabled + App Password for real email mode |

---

## 🚀 Installation

**Step 1 — Clone the repository**

```bash
git clone https://github.com/your-username/ai-based-phishing-email-detector.git
cd ai-based-phishing-email-detector
```

**Step 2 — Create virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
# Terminal will show (.venv) prefix when active
```

**Step 3 — Install dependencies**

```bash
pip install groq
```

---

## 🔧 Configuration

Get your free Groq API key from **https://console.groq.com** — sign up with Google or GitHub, no credit card needed.

**Option A — Temporary (current session)**

```bash
export GROQ_API_KEY="gsk_your_key_here"
```

**Option B — Permanent (recommended for Kali Linux)**

```bash
echo 'export GROQ_API_KEY="gsk_your_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**Option C — .env file**

```bash
echo 'GROQ_API_KEY="gsk_your_key_here"' > .env
```

> ⚠️ **Security Warning:** Never share your API key publicly or commit it to GitHub. If your key is accidentally exposed, regenerate it immediately at [console.groq.com/keys](https://console.groq.com/keys).

---

## ▶️ Usage

```bash
# Activate venv first
source .venv/bin/activate

# Run
python main.py
```

You will see an interactive prompt:

```
============================================================
  [AI-Based Phishing Email Detector] AI-POWERED PHISHING EMAIL DETECTOR
============================================================
Choose mode:
  [1] Analyze real emails (requires credentials)
  [2] Demo mode (sample emails)
Enter choice (1 or 2): _
```

- **Demo Mode** — runs 3 built-in sample emails (phishing + safe) with no credentials needed. Great for testing and GitHub demos.
- **Real Email Mode** — connects to your inbox via IMAP and analyzes your latest emails using AI.

---

## 🔍 How It Works

```
1. User Input
   └── Choose demo mode or enter email credentials (IMAP)

2. email_reader.py
   └── Connects via IMAP, fetches email subject and body

3. ai_analyzer.py
   └── Sends email content to Groq (LLaMA 3.3 70B) with cybersecurity prompt

4. AI Response (JSON)
   └── Returns score, verdict, confidence, reasons, red flags

5. main.py
   └── Formats and prints the full analysis report to terminal
```

---

## 📊 Scoring Guide

| Score Range | Verdict | Meaning |
|-------------|---------|---------|
| 0 — 25 | ✅ `SAFE` | No phishing indicators detected |
| 26 — 50 | ⚠️ `SUSPICIOUS` | Some suspicious elements, proceed with caution |
| 51 — 75 | 🟠 `SUSPICIOUS` | Multiple phishing indicators present |
| 76 — 100 | 🔴 `PHISHING` | Classic phishing attack, very high confidence |

---

## 🖥️ Sample Output

```
============================================================
EMAIL ANALYSIS REPORT
============================================================
From    : security@paypa1-alert.com
Subject : URGENT: Your account has been suspended!
============================================================

[PHISHING]
VERDICT        : PHISHING
PHISHING SCORE : [####################] 97/100
IS PHISHING    : YES - DANGER
CONFIDENCE     : HIGH

REASONS:
  1. Sender domain mimics PayPal with character substitution
  2. Creates urgency with account deletion threats
  3. Requests highly sensitive personal and financial data

RED FLAGS:
  - Domain spoofing: paypa1 instead of paypal
  - Requests SSN, credit card, and password together
  - 24-hour deadline pressure tactic

RECOMMENDATION:
  Delete immediately. Never provide financial data via email links.
============================================================

SUMMARY
============================================================
  Total Emails Analyzed : 3
  Phishing Detected     : 2
  Safe Emails           : 1
  Average Risk Score    : 68.3/100

  [WARNING] 2 phishing email(s) detected!
```

---

## 🐛 Error Handling

All error handling and debugging was completed by **Rahat Sahriar Rafi**.

---

**`ModuleNotFoundError: No module named 'groq'`**

Virtual environment is not activated or `groq` is not installed inside it.

```bash
source .venv/bin/activate
pip install groq
```

---

**`GroqError: api_key must be set`**

The `GROQ_API_KEY` environment variable was not set before running the script.

```bash
export GROQ_API_KEY="gsk_your_key_here"
```

---

**`SyntaxError: invalid character (emoji/unicode)`**

Kali Linux terminals may not support Unicode block characters or emoji in source files. All emoji and special characters have been replaced with ASCII equivalents throughout the codebase.

---

**`externally-managed-environment` (pip on Kali)**

Kali Linux prevents system-wide pip installs. Always use a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install groq
```

---

**`IMAP Authentication Error`**

Make sure IMAP is enabled in Gmail settings and you are using an **App Password**, not your regular Gmail password.

---

## 🔒 Security Best Practices

| Practice | Action |
|----------|--------|
| API Key Storage | Use `.env` file or environment variable — never hardcode |
| GitHub Safety | Add `.env` and `.venv/` to `.gitignore` before pushing |
| Key Exposure | Regenerate immediately at [console.groq.com/keys](https://console.groq.com/keys) |
| Gmail Password | Use App Passwords, not your main Gmail password |

**Recommended `.gitignore`:**

```
.env
.venv/
venv/
__pycache__/
*.pyc
*.pyo
```

---

## 📄 License

MIT License — AI-Based Phishing Email Detector © 2025

Built with **Python** + **Groq LLaMA 3.3 70B** — free, open source, and fast.

> Core Development: **Md. Munkasiur Haque** | Error Handling: **Rahat Sahriar Rafi**

# 🔐 Privacy-First Password Strength Analyzer

A real-time, browser-isolated password security analyzer built with **Python & Streamlit**.

Unlike conventional password analyzers that send inputs to a backend server, this application performs **100% of its evaluation client-side inside a sandboxed browser environment**. Your passwords are never transmitted over the network, saved to a database, or logged anywhere.

---

## 🛡️ Privacy & Security Architecture

Traditional web tools pose privacy risks when evaluating passwords. This application solves this with a **Zero-Knowledge Client-Side Sandbox**:

```text
┌─────────────────────────────────────────────────────────────┐
│                    USER BROWSER                             │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ Embedded Sandboxed Web Component                      │  │
│  │                                                       │  │
│  │  1. User types password                               │  │
│  │  2. JavaScript evaluates metrics in volatile memory    │  │
│  │  3. Instant UI updates (Score, Meter, Badges)         │  │
│  │                                                       │  │
│  │  🚫 NO fetch() / XMLHttpRequest                       │  │
│  │  🚫 NO LocalStorage / Cookies                         │  │
│  │  🚫 NO Third-Party Scripts                            │  │
│  └───────────────────────────────────────────────────────┘  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                      ❌ ZERO TRANSMISSION
                               │
┌──────────────────────────────▼──────────────────────────────┐
│                  STREAMLIT PYTHON SERVER                    │
│                                                             │
│  • Serves UI template only                                  │
│  • Never receives keystrokes or password strings            │
│  • Zero-log environment                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

* **⚡ Real-Time Evaluation:** Dynamic visual feedback as you type.
* **🌓 Adaptive Light & Dark Mode:** Automatically syncs with Streamlit and OS theme preferences with WCAG-compliant contrast.
* **🔤 Multi-Factor Character Analysis:** Inspects lowercase, uppercase, numeric, symbol coverage, and unique character ratios.
* **🔍 Weakness & Pattern Detection:** Flags repeated characters, character sequences, and common weak passwords (`123456`, `qwerty`, `admin`, etc.).
* **👁️ Mask / Unmask Toggle:** Convenient visibility control for long passphrases.
* **📱 Fully Responsive:** Clean layout across mobile, tablet, and desktop viewports.

---

## 📁 Repository Structure

Password-Strength-Analyzer/
│
├── .gitignore              ✅ PUSH (Protects repo from junk files)
├── app.py                  ✅ PUSH (Your main Streamlit code)
├── README.md               ✅ PUSH (Project documentation)
└── requirements.txt        ✅ PUSH (Package dependencies)

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/password-analyzer-streamlit.git
cd password-analyzer-streamlit
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run streamlit_app.py
```

Your browser will automatically open:
```text
http://localhost:8501
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Fork or push this repository to your **GitHub** account.
2. Visit **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub.
3. Click **"New app"**.
4. Select your repository: `password-analyzer-streamlit`.
5. Set **Main file path** to: `streamlit_app.py`.
6. Click **"Deploy!"** 🚀

---

## 🧪 Evaluation & Scoring Breakdown

| Metric | Condition | Points Awarded |
| :--- | :--- | :--- |
| **Length** | $\ge 8$ characters | $+1$ pt |
| | $\ge 12$ characters | $+2$ pts |
| | $\ge 16$ characters | $+1$ pt (Bonus) |
| **Character Diversity** | Lowercase (`a-z`) | $+1$ pt |
| | Uppercase (`A-Z`) | $+1$ pt |
| | Numbers (`0-9`) | $+1$ pt |
| | Special Symbols (`!@#$%^&*`) | $+1$ pt |
| **Entropy Bonus** | $\ge 8$ unique characters | $+1$ pt |
| **Pattern Penalties** | 3+ repeating characters (`aaa`) | $-1$ pt |
| **Blacklist** | Common breach passwords | Score capped to $0$ |

### Strength Levels

* **`0 – 2 pts`**: 🔴 **Very Weak** — Can be brute-forced almost instantly.
* **`3 – 4 pts`**: 🟠 **Weak** — Vulnerable to simple dictionary attacks.
* **`5 – 6 pts`**: 🟡 **Moderate** — Acceptable for low-risk accounts.
* **`7 pts`**: 🟢 **Strong** — High complexity; resistant to offline cracking.
* **`8 pts`**: 🔵 **Very Strong** — Multi-word passphrases / high-entropy keys.

---

## 🔒 Security Principles

1. **Client Isolation:** All evaluations run strictly inside an inline `<iframe>` sandbox.
2. **No Data Retention:** No database connections, local storage, or session storage.
3. **No External Dependencies:** Zero CDN links or unvetted JavaScript libraries.
4. **Input Constraints:** Analysis payload bounded to a maximum of 1,000 characters to prevent DOM freezing.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ⚠️ Disclaimer

*This tool is intended for educational purposes and password hygiene awareness. For production environments, always enforce multi-factor authentication (MFA) and generate complex passphrases using a trusted password manager.*
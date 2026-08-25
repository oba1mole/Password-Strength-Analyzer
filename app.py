import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Password Analyzer",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# PAGE STYLING (STREAMLIT NATIVE ADAPTIVE CSS)
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        .block-container {
            max-width: 800px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .security-note {
            padding: 0.9rem 1.1rem;
            border: 1px solid rgba(128, 128, 128, 0.25);
            background-color: rgba(128, 128, 128, 0.06);
            border-radius: 10px;
            margin-bottom: 1.25rem;
            font-size: 0.92rem;
            line-height: 1.5;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🔐 Live Password Analyzer")

st.caption(
    "AI Security & Machine Learning Project — "
    "Build by `DAVID IMOLEAYO BAMIDELE`."
)

st.caption(
    "Client-side password analysis — "
    "the password is never submitted to the Streamlit server."
)

st.markdown(
    """
    <div class="security-note">
        🛡️ <strong>Privacy Design:</strong>
        The password field and analysis logic run completely inside the client-side browser component.
        This application does not store data, does not transmit inputs over the network,
        and does not load external third-party scripts.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# CLIENT-SIDE PASSWORD ANALYZER (THEMED COMPONENT)
# ---------------------------------------------------------

html = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
    /* =====================================================
       THEME VARIABLES (AUTOMATIC LIGHT / DARK ADAPTATION)
       ===================================================== */
    :root {
        color-scheme: light dark;

        /* Light Mode Defaults */
        --bg-card: rgba(0, 0, 0, 0.02);
        --border-color: rgba(0, 0, 0, 0.12);
        --text-primary: #1f2937;
        --text-muted: #6b7280;
        --input-bg: #ffffff;
        --input-border: rgba(0, 0, 0, 0.18);
        --focus-ring: rgba(79, 143, 247, 0.4);
        --item-bg: rgba(0, 0, 0, 0.02);

        /* Status Colors */
        --color-ok: #15803d;
        --bg-ok: rgba(34, 197, 94, 0.12);
        --color-bad: #991b1b;
        --bg-bad: rgba(239, 68, 68, 0.08);

        /* Warning box */
        --bg-warning: rgba(234, 179, 8, 0.1);
        --border-warning: rgba(234, 179, 8, 0.35);
        --text-warning: #854d0e;

        /* Meter track */
        --meter-track: rgba(0, 0, 0, 0.08);
    }

    /* Dark Mode Overrides */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-card: rgba(255, 255, 255, 0.03);
            --border-color: rgba(255, 255, 255, 0.12);
            --text-primary: #f3f4f6;
            --text-muted: #9ca3af;
            --input-bg: rgba(255, 255, 255, 0.05);
            --input-border: rgba(255, 255, 255, 0.18);
            --focus-ring: rgba(79, 143, 247, 0.5);
            --item-bg: rgba(255, 255, 255, 0.03);

            --color-ok: #4ade80;
            --bg-ok: rgba(34, 197, 94, 0.16);
            --color-bad: #f87171;
            --bg-bad: rgba(239, 68, 68, 0.14);

            --bg-warning: rgba(234, 179, 8, 0.14);
            --border-warning: rgba(234, 179, 8, 0.4);
            --text-warning: #fde047;

            --meter-track: rgba(255, 255, 255, 0.1);
        }
    }

    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        background: transparent;
        color: var(--text-primary);
    }

    .card {
        border: 1px solid var(--border-color);
        background: var(--bg-card);
        border-radius: 12px;
        padding: 20px;
    }

    label {
        display: block;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 8px;
        color: var(--text-primary);
    }

    .row {
        display: flex;
        gap: 8px;
    }

    input[type="password"],
    input[type="text"] {
        width: 100%;
        padding: 11px 14px;
        border: 1px solid var(--input-border);
        border-radius: 8px;
        background: var(--input-bg);
        color: var(--text-primary);
        font-size: 15px;
        outline: none;
        transition: border-color 0.2s, box-shadow 0.2s;
    }

    input:focus {
        border-color: #4f8ff7;
        box-shadow: 0 0 0 3px var(--focus-ring);
    }

    button {
        border: 1px solid var(--input-border);
        border-radius: 8px;
        padding: 0 16px;
        background: var(--input-bg);
        color: var(--text-primary);
        cursor: pointer;
        font-weight: 600;
        font-size: 0.9rem;
        min-width: 80px;
        transition: background 0.2s, opacity 0.2s;
    }

    button:hover {
        opacity: 0.85;
    }

    .meter {
        height: 8px;
        border-radius: 99px;
        background: var(--meter-track);
        overflow: hidden;
        margin: 16px 0 12px;
    }

    .fill {
        height: 100%;
        width: 0%;
        transition: width 0.25s ease, background-color 0.25s ease;
        background: #ef4444;
    }

    .score {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 14px;
        color: var(--text-primary);
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 8px;
    }

    .item {
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 9px 12px;
        font-size: 0.88rem;
        background: var(--item-bg);
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: background 0.2s, border-color 0.2s;
    }

    .item.ok {
        background: var(--bg-ok);
        color: var(--color-ok);
        font-weight: 600;
        border-color: transparent;
    }

    .item.bad {
        background: var(--bg-bad);
        color: var(--color-bad);
        border-color: transparent;
    }

    .warning {
        margin-top: 14px;
        padding: 10px 14px;
        border: 1px solid var(--border-warning);
        background: var(--bg-warning);
        color: var(--text-warning);
        border-radius: 8px;
        font-size: 0.88rem;
        line-height: 1.4;
    }

    .hint {
        color: var(--text-muted);
        font-size: 0.82rem;
        margin-top: 14px;
        line-height: 1.45;
    }

    @media (max-width: 550px) {
        .grid {
            grid-template-columns: 1fr;
        }
    }
</style>
</head>

<body>

<div class="card">
    <label for="pw">Enter a password to analyze:</label>

    <div class="row">
        <input
            id="pw"
            type="password"
            autocomplete="new-password"
            spellcheck="false"
            maxlength="1000"
            placeholder="Type your password here..."
            aria-label="Password to analyze"
        >
        <button id="toggle" type="button">Show</button>
    </div>

    <div id="output" hidden>
        <div class="meter" aria-hidden="true">
            <div id="fill" class="fill"></div>
        </div>

        <div id="score" class="score">Strength: —</div>

        <div class="grid">
            <div class="item" id="length"><span>Length</span> <span>—</span></div>
            <div class="item" id="lower"><span>Lowercase</span> <span>—</span></div>
            <div class="item" id="upper"><span>Uppercase</span> <span>—</span></div>
            <div class="item" id="number"><span>Numbers</span> <span>—</span></div>
            <div class="item" id="symbol"><span>Symbols</span> <span>—</span></div>
            <div class="item" id="unique"><span>Unique chars</span> <span>—</span></div>
        </div>

        <div id="warning" class="warning"></div>

        <div class="hint">
            ✓ Evaluated entirely in this browser component. No password value is sent to a password-analysis API and the application does not store the password.
        </div>
    </div>
</div>

<script>
(function () {
    "use strict";

    const MAX_LENGTH = 1000;

    const pw = document.getElementById("pw");
    const toggle = document.getElementById("toggle");
    const output = document.getElementById("output");
    const fill = document.getElementById("fill");
    const score = document.getElementById("score");
    const warning = document.getElementById("warning");

    const fields = {
        length: document.getElementById("length"),
        lower: document.getElementById("lower"),
        upper: document.getElementById("upper"),
        number: document.getElementById("number"),
        symbol: document.getElementById("symbol"),
        unique: document.getElementById("unique")
    };

    function setResult(element, label, ok) {
        element.innerHTML = `<span>${label}</span> <span>${ok ? "✓" : "✗"}</span>`;
        element.className = "item " + (ok ? "ok" : "bad");
    }

    function analyze(value) {
        if (!value) {
            output.hidden = true;
            return;
        }

        output.hidden = false;

        const length = value.length;
        const lower = /[a-z]/.test(value);
        const upper = /[A-Z]/.test(value);
        const number = /[0-9]/.test(value);
        const symbol = /[^A-Za-z0-9]/.test(value);
        const unique = new Set(Array.from(value)).size;

        // Scoring rules
        let points = 0;
        if (length >= 12) points += 2;
        else if (length >= 8) points += 1;
        if (length >= 16) points += 1;

        if (lower) points += 1;
        if (upper) points += 1;
        if (number) points += 1;
        if (symbol) points += 1;

        if (unique >= 8) points += 1;
        if (/(.)\1{2,}/.test(value)) points -= 1; // Penalty for sequences like 'aaa'

        if (/^(password|qwerty|123456|12345678|admin|letmein)$/i.test(value)) {
            points = 0;
        }

        points = Math.max(0, Math.min(points, 8));

        // Strength label & color assignment
        let label = "Very weak";
        let barColor = "#ef4444"; // Red

        if (points <= 2) {
            label = "Very weak";
            barColor = "#ef4444";
        } else if (points <= 4) {
            label = "Weak";
            barColor = "#f97316"; // Orange
        } else if (points <= 6) {
            label = "Moderate";
            barColor = "#eab308"; // Amber / Gold
        } else if (points === 7) {
            label = "Strong";
            barColor = "#22c55e"; // Green
        } else {
            label = "Very strong";
            barColor = "#06b6d4"; // Cyan
        }

        // Render to UI
        fill.style.width = ((points / 8) * 100) + "%";
        fill.style.backgroundColor = barColor;

        score.textContent = "Strength: " + label;

        fields.length.innerHTML = `<span>Length</span> <span>${length}</span>`;
        fields.length.className = "item " + (length >= 12 ? "ok" : (length >= 8 ? "ok" : "bad"));

        setResult(fields.lower, "Lowercase", lower);
        setResult(fields.upper, "Uppercase", upper);
        setResult(fields.number, "Numbers", number);
        setResult(fields.symbol, "Symbols", symbol);

        fields.unique.innerHTML = `<span>Unique chars</span> <span>${unique}</span>`;
        fields.unique.className = "item " + (unique >= 8 ? "ok" : "bad");

        // Guidance warnings
        if (length > MAX_LENGTH) {
            warning.textContent = "⚠️ Input is too long. Analysis is limited to 1,000 characters.";
        } else if (length < 8) {
            warning.textContent = "⚠️ Passwords under 8 characters can be brute-forced very quickly and do not re-use on other services.";
        } else if (length < 12) {
            warning.textContent = "💡 Recommendation: Increase length to 12+ characters for strong protection.";
        } else {
            warning.textContent = "✅ Tip: Passphrases with multiple unrelated words are easiest to remember and hardest to crack.";
        }
    }

    pw.addEventListener("input", () => analyze(pw.value));

    toggle.addEventListener("click", () => {
        const isShowing = pw.type === "text";
        pw.type = isShowing ? "password" : "text";
        toggle.textContent = isShowing ? "Show" : "Hide";
    });
})();
</script>

</body>
</html>
"""

# ---------------------------------------------------------
# RENDER CLIENT-SIDE COMPONENT
# ---------------------------------------------------------

components.html(html, height=480, scrolling=False)

# ---------------------------------------------------------
# SECURITY INFORMATION
# ---------------------------------------------------------
st.divider()

st.subheader("🛡️ Security Design")

st.markdown(
    """
    - **Client-side analysis:** Password analysis is performed
      inside the browser component.
    - **No database:** Passwords are never stored.
    - **No password API:** There is no `/api/analyze` endpoint.
    - **No password logging:** The application does not print
      or log password values.
    - **No third-party JavaScript:** The analyzer does not load
      external scripts.
    - **No analytics/session replay:** Password input should not
      be exposed to analytics or session-recording tools.
    - **Input limit:** Analysis is limited to 1,000 characters.
    """
)

st.info(
    "This is a password-strength estimator, "
    "not a guarantee against password cracking."
)

st.caption(
    "Note: "
    "For real authentication systems, always use unique passwords "
    "and a reputable password manager."
)
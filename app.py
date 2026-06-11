import streamlit as st
from groq import Groq

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FinGuard AI",
    page_icon="💰",
    layout="wide"
)

# ---------------- GROQ API ----------------
client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

# ---------------- MEMORY ----------------
if "financial_history" not in st.session_state:
    st.session_state.financial_history = []

# ---------------- DARK THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.block-container {
    padding-top: 2rem;
}

[data-testid="stSidebar"] {
    background-color: #161B22;
}

div.stButton > button {
    background-color: #1F6FEB;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

div.stButton > button:hover {
    background-color: #388BFD;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("💰 FinGuard AI")
st.subheader("Your Intelligent Financial Coach")

st.write(
    "Analyze financial behavior using NLP, "
    "cognitive science, behavioral economics, "
    "and AI-powered financial coaching."
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 FinGuard Features")
if st.sidebar.button(
    "🔄 Reset Memory"
):
    st.session_state.financial_history = []

features = [
    "✅ Financial Intent Detection",
    "✅ Spending Risk Analysis",
    "✅ Cognitive Bias Detection",
    "✅ Financial Personality Engine",
    "✅ Financial Health Score",
    "✅ Behavioral Memory",
    "✅ AI Financial Coach"
]

for feature in features:
    st.sidebar.write(feature)

# ---------------- INPUT ----------------
user_input = st.text_area(
    "💭 Describe your financial thought:",
    height=120
)

if user_input:

    text = user_input.lower()

    # ---------------- KEYWORDS ----------------

    spending_words = [
        "buy", "purchase",
        "shopping", "spend",
        "expensive", "travel",
        "trip", "vacation",
        "shop", "iphone",
        "shoes", "airpods",
        "laptop", "car"
    ]

    saving_words = [
        "save", "saving",
        "invest", "future",
        "goal", "deposit"
    ]

    budget_words = [
        "budget", "expense",
        "limit", "manage",
        "control"
    ]

    impulsive_words = [
        "now", "today",
        "urgent", "sale",
        "discount", "limited",
        "offer", "need",
        "tonight", "expensive",
        "can't miss"
    ]

    emotional_words = [
        "sad", "stressed",
        "depressed", "bad day",
        "anxious", "hopeless",
        "overwhelmed"
    ]

    distress_words = [
        "broke",
        "debt",
        "drowning in debt",
        "bankrupt",
        "poor",
        "ruined",
        "can't afford",
        "no money",
        "financial stress",
        "loan"
    ]

    # ---------------- VARIABLES ----------------

    intent = "Unknown"
    impulsive_score = 0
    health_score = 100

    personality = "Balanced Financial Thinker"

    detected_signals = []
    cognitive_biases = []

    # ---------------- INTENT DETECTION ----------------

    for word in spending_words:
        if word in text:
            intent = "Spending 💸"

    for word in saving_words:
        if word in text:
            intent = "Saving 💰"

    for word in budget_words:
        if word in text:
            intent = "Budgeting 📊"

    # ---------------- IMPULSIVE DETECTION ----------------

    for word in impulsive_words:
        if word in text:
            impulsive_score += 1
            health_score -= 8

    # ---------------- SIGNALS ----------------

    if any(word in text for word in spending_words):
        detected_signals.append(
            "✔ Spending Intent"
        )

    if (
        ("need" in text or "want" in text)
        and any(word in text for word in spending_words)
    ):
        detected_signals.append(
            "✔ Emotional Spending Trigger"
        )

    if "expensive" in text:
        detected_signals.append(
            "✔ High Cost Purchase"
        )

    if any(
        word in text for word in
        ["now", "today", "urgent", "tonight"]
    ):
        detected_signals.append(
            "✔ Urgency Detected"
        )

    # ---------------- COGNITIVE SCIENCE ----------------

    if any(
        word in text for word in
        ["sale", "discount",
         "limited", "offer"]
    ):
        cognitive_biases.append(
            "🧠 FOMO Trigger"
        )
        health_score -= 10

    if any(
        word in text for word in
        ["deserve",
         "treat myself",
         "earned this"]
    ):
        cognitive_biases.append(
            "🧠 Reward-Seeking Behavior"
        )
        health_score -= 10

    if any(
        word in text for word in emotional_words
    ):
        cognitive_biases.append(
            "🧠 Emotional Spending Risk"
        )
        health_score -= 15

    if any(
        word in text for word in
        ["miss out", "can't miss"]
    ):
        cognitive_biases.append(
            "🧠 Loss Aversion Bias"
        )
        health_score -= 10

    # ---------------- DISTRESS ----------------

    if any(
        word in text for word in distress_words
    ):
        intent = "Financial Distress ⚠"

        cognitive_biases.append(
            "🧠 Financial Distress"
        )

        detected_signals.append(
            "✔ Financial Stress Signal"
        )

        health_score -= 60

    if "go broke" in text:
        cognitive_biases.append(
            "🧠 Self-Destructive Thinking"
        )

        detected_signals.append(
            "✔ High-Risk Financial Mindset"
        )

        health_score -= 40

    # ---------------- PERSONALITY ----------------

    if impulsive_score >= 3:
        personality = "💸 Impulsive Spender"

    if any(
        word in text for word in emotional_words
    ):
        personality = "🧠 Emotional Spender"

    if any(
        word in text for word in
        ["save", "future",
         "invest", "goal"]
    ):
        personality = "💰 Smart Saver"

    if any(
        word in text for word in
        ["budget", "expense",
         "manage"]
    ):
        personality = "📊 Budget Planner"

    if any(
        word in text for word in distress_words
    ):
        personality = (
            "⚠ Financially Distressed"
        )
    # ---------------- SCORE FIX ----------------

    health_score = max(
        0,
        min(100, health_score)
    )

    # ---------------- MEMORY ----------------

    st.session_state.financial_history.append(
        personality
    )

    recent_history = (
        st.session_state.financial_history[-5:]
    )

    memory_feedback = (
        "No strong long-term behavior detected."
    )

    impulsive_count = recent_history.count(
        "💸 Impulsive Spender"
    )

    emotional_count = recent_history.count(
        "🧠 Emotional Spender"
    )

    saver_count = recent_history.count(
        "💰 Smart Saver"
    )

    if impulsive_count >= 2:
        memory_feedback = (
            "⚠ Repeated impulsive spending "
            "patterns detected recently."
        )

    elif emotional_count >= 2:
        memory_feedback = (
            "🧠 Emotional spending "
            "appears frequently."
        )

    elif saver_count >= 2:
        memory_feedback = (
            "💰 Strong saving behavior "
            "observed recently."
        )

    # ---------------- DASHBOARD ----------------

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## 📊 Financial Intent")
        st.success(intent)

    with col2:
        st.markdown("## 🧬 Personality")
        st.success(personality)

    st.markdown("## 🧠 Behavioral Memory")
    st.info(memory_feedback)

    # ---------------- TREND GRAPH ----------------

    st.markdown("## 📈 Financial Behavior Trend")

    trend_map = {
        "💸 Impulsive Spender": 30,
        "🧠 Emotional Spender": 45,
        "💰 Smart Saver": 90,
        "📊 Budget Planner": 80,
        "⚠ Financially Distressed": 20,
        "Balanced Financial Thinker": 70
    }

    trend_scores = [
        trend_map.get(p, 50)
        for p in recent_history
    ]

    if trend_scores:
        st.line_chart(trend_scores)

    st.markdown("## 💯 Financial Health Score")
    st.progress(health_score / 100)
    st.write(f"### Score: {health_score}/100")

    st.markdown("## 🧠 FinGuard Reasoning")

    for signal in detected_signals:
        st.write(signal)

    st.markdown("## 🧬 Cognitive Bias Analysis")

    if cognitive_biases:
        for bias in cognitive_biases:
            st.write(bias)
    else:
        st.success(
            "No major cognitive biases detected."
        )

    # ---------------- AI COACH ----------------

    st.markdown("## 🤖 FinGuard AI Coach")

    if st.button(
        "Generate Smart Financial Advice"
    ):

        with st.spinner(
            "FinGuard is thinking..."
        ):

            try:

                prompt = f"""
You are FinGuard AI,
a smart, friendly, and emotionally aware
financial coach.

Be supportive and reassuring,
especially when the user is financially
stressed or emotionally vulnerable.

However, always remain practical,
financially intelligent, and specific.

Use behavioral finance concepts
when relevant (FOMO, impulsivity,
loss aversion, delayed gratification).

Give realistic and useful money advice.

Avoid sounding robotic,
but also avoid overly dramatic
therapy-like language.

Be warm, calm, and actionable.

User financial thought:
{user_input}

Intent:
{intent}

Personality:
{personality}

Health Score:
{health_score}/100

Behavior Signals:
{detected_signals}

Cognitive Biases:
{cognitive_biases}

Your task:
1. Analyze financial behavior.
2. Identify emotional/cognitive risks.
3. Mention behavioral finance concepts
such as FOMO, impulsivity,
delayed gratification, or loss aversion.
4. Give practical advice.
5. Be friendly but intelligent.
6. Avoid generic phrases.
7. Keep under 120 words.
"""

                response = (
                    client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )
                )

                ai_response = (
                    response
                    .choices[0]
                    .message
                    .content
                )

                st.info(ai_response)

            except Exception as e:
                st.error(
                    f"AI Error: {e}"
                )
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* ----------------------------------------------------- */
/* MAIN BACKGROUND */
/* ----------------------------------------------------- */

.stApp {
    background:
        radial-gradient(
            circle at 50% 20%,
            rgba(0, 180, 216, 0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 10% 90%,
            rgba(72, 149, 239, 0.08),
            transparent 25%
        ),
        #07111f;
}


/* Hide Streamlit Branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* Main Container */

.block-container {
    max-width: 1050px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}


/* ----------------------------------------------------- */
/* TITLE */
/* ----------------------------------------------------- */

.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: 800;
    color: white;
    margin-top: 70px;
    margin-bottom: 5px;
    letter-spacing: -2px;
}


.subtitle {
    text-align: center;
    font-size: 20px;
    color: #94a3b8;
    margin-bottom: 12px;
}


.tagline {
    text-align: center;
    color: #22d3ee;
    font-size: 15px;
    letter-spacing: 2px;
    margin-bottom: 45px;
}


/* ----------------------------------------------------- */
/* SHIELD */
/* ----------------------------------------------------- */

.shield {
    text-align: center;
    font-size: 75px;
    margin-bottom: 5px;
}


/* ----------------------------------------------------- */
/* WELCOME */
/* ----------------------------------------------------- */

.welcome-text {
    text-align: center;
    font-size: 30px;
    font-weight: 500;
    color: white;
    margin-top: 55px;
    margin-bottom: 30px;
}


/* ----------------------------------------------------- */
/* FEATURE CARDS */
/* ----------------------------------------------------- */

.feature-card {

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.06),
            rgba(255,255,255,0.02)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 20px;

    text-align: center;

    color: white;

    min-height: 130px;

    backdrop-filter: blur(12px);

    transition: 0.3s;
}


.feature-card:hover {

    border:
        1px solid rgba(34,211,238,0.5);

    transform: translateY(-5px);
}


.feature-icon {

    font-size: 30px;

    margin-bottom: 8px;
}


.feature-title {

    font-weight: 600;

    font-size: 15px;

    color: white;
}


.feature-description {

    font-size: 12px;

    color: #94a3b8;

    margin-top: 5px;
}


/* ----------------------------------------------------- */
/* API CARD */
/* ----------------------------------------------------- */

.api-box {

    background:
        linear-gradient(
            145deg,
            rgba(15, 32, 55, 0.95),
            rgba(10, 22, 38, 0.95)
        );

    border:
        1px solid rgba(34,211,238,0.18);

    border-radius: 22px;

    padding: 30px;

    margin-top: 20px;

    box-shadow:
        0px 20px 80px rgba(0,0,0,0.35);
}


/* ----------------------------------------------------- */
/* STREAMLIT INPUT */
/* ----------------------------------------------------- */

.stTextInput input {

    border-radius: 14px !important;

    border:
        1px solid rgba(34,211,238,0.35) !important;

    background-color:
        rgba(255,255,255,0.05) !important;

    color: white !important;

    padding: 15px !important;

    font-size: 16px !important;
}


/* ----------------------------------------------------- */
/* BUTTON */
/* ----------------------------------------------------- */

.stButton button {

    width: 100%;

    border-radius: 14px;

    padding: 13px;

    font-size: 16px;

    font-weight: 600;

    border: none;

    color: #04111f;

    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #3b82f6
        );
}


/* ----------------------------------------------------- */
/* CHAT INPUT */
/* ----------------------------------------------------- */

[data-testid="stChatInput"] {

    border-radius: 20px !important;

}


[data-testid="stChatInput"] textarea {

    background-color:
        rgba(255,255,255,0.06) !important;

    color: white !important;

    border-radius: 20px !important;
}


/* ----------------------------------------------------- */
/* CHAT MESSAGE */
/* ----------------------------------------------------- */

[data-testid="stChatMessage"] {

    background:
        rgba(255,255,255,0.03);

    border-radius: 16px;

    border:
        1px solid rgba(255,255,255,0.06);

    padding: 15px;
}


/* ----------------------------------------------------- */
/* STATUS BADGE */
/* ----------------------------------------------------- */

.status {

    text-align: center;

    color: #22c55e;

    font-size: 13px;

    margin-top: 25px;
}


</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "api_key" not in st.session_state:
    st.session_state.api_key = ""

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# SYSTEM PROMPT
# =========================================================

SYSTEM_PROMPT = """
You are CyberGuard AI, a specialized Cybersecurity
Intelligence Assistant.

Your expertise includes:

- Cybersecurity fundamentals
- Phishing awareness
- Social engineering
- Password security
- Multi-factor authentication
- Malware awareness
- Ransomware awareness
- Digital privacy
- Secure browsing
- Email security
- Account protection
- Network security fundamentals
- Web security concepts
- Security best practices
- Threat awareness
- Defensive risk assessment

STRICT DOMAIN POLICY:

You ONLY answer questions related to cybersecurity,
digital safety, online privacy, cyber threats, and
defensive security practices.

If the user asks about any unrelated topic, respond ONLY:

"🛡️ Please ask a question related to Cybersecurity.
CyberGuard AI is specialized in Cybersecurity and
Digital Safety."

For relevant cybersecurity questions:

- Explain clearly.
- Use headings.
- Give practical defensive advice.
- Mention LOW, MEDIUM, or HIGH risk when relevant.
- Keep the answer educational and professional.
- Promote ethical and authorized security practices.

Never assist with harmful, illegal, or unauthorized
cybersecurity activities.
"""


# =========================================================
# LOGIN / API SCREEN
# =========================================================

if not st.session_state.authenticated:

    # Shield

    st.markdown(
        "<div class='shield'>🛡️</div>",
        unsafe_allow_html=True
    )


    # Title

    st.markdown(
        "<div class='main-title'>CyberGuard AI</div>",
        unsafe_allow_html=True
    )


    # Subtitle

    st.markdown(
        """
        <div class='subtitle'>
        Cybersecurity Intelligence Assistant
        </div>
        """,
        unsafe_allow_html=True
    )


    # Tagline

    st.markdown(
        """
        <div class='tagline'>
        DETECT • UNDERSTAND • DEFEND
        </div>
        """,
        unsafe_allow_html=True
    )


    # Center Columns

    left, center, right = st.columns([1, 1.5, 1])


    with center:

        st.markdown(
            "<div class='api-box'>",
            unsafe_allow_html=True
        )


        st.markdown(
            """
            <h3 style='text-align:center;
                       color:white;
                       margin-bottom:5px;'>

            🔑 Connect Your AI

            </h3>

            <p style='text-align:center;
                      color:#94a3b8;'>

            Enter your OpenAI API Key to launch
            CyberGuard AI.

            </p>
            """,
            unsafe_allow_html=True
        )


        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Enter your API key..."
        )

if st.button("Launch CyberGuard AI →"):

    if not api_key.strip():

        st.warning(
            "⚠️ Please enter your OpenAI API Key first."
        )

    else:

        try:

            with st.spinner(
                "🔐 Verifying your API key..."
            ):

                # Test API Key with a very small request
                test_chat = ChatOpenAI(

                    model="gpt-5-nano",

                    temperature=0,

                    api_key=api_key.strip(),

                    max_tokens=5
                )


                # Small test request
                test_chat.invoke(
                    "Reply with: OK"
                )


            # If successful
            st.session_state.api_key = api_key.strip()

            st.session_state.authenticated = True

            st.success(
                "✅ API Key verified successfully!"
            )

            st.rerun()


        except Exception as error:

            error_message = str(error).lower()


            # Invalid API Key
            if (
                "api key" in error_message
                or "authentication" in error_message
                or "401" in error_message
            ):

                st.error(
                    "❌ Invalid API Key. Please enter a valid OpenAI API Key."
                )

            else:

                st.error(
                    f"❌ Unable to verify API Key: {str(error)}"
                )

        st.markdown(
            """
            <p style='text-align:center;
                      color:#64748b;
                      font-size:12px;
                      margin-top:15px;'>

            🔒 Your API key is only used for this session.

            </p>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # Footer

    st.markdown(
        """
        <div class='status'>
        ● CyberGuard AI • Specialized Cybersecurity Assistant
        </div>
        """,
        unsafe_allow_html=True
    )


    st.stop()


# =========================================================
# APP HEADER AFTER LOGIN
# =========================================================

top_left, top_center, top_right = st.columns(
    [1, 3, 1]
)


with top_left:

    st.markdown(
        "<h3 style='color:white;'>🛡️ CyberGuard</h3>",
        unsafe_allow_html=True
    )


with top_center:

    st.markdown(
        """
        <p style='text-align:center;
                  color:#22d3ee;
                  font-size:14px;
                  margin-top:18px;'>

        CYBERSECURITY INTELLIGENCE

        </p>
        """,
        unsafe_allow_html=True
    )


with top_right:

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# =========================================================
# EMPTY CHAT SCREEN
# =========================================================

if len(st.session_state.messages) == 0:

    st.markdown(
        "<div class='shield'>🛡️</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        "<div class='main-title'>CyberGuard AI</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class='subtitle'>
        Your AI Assistant for Cybersecurity,
        Threat Awareness & Digital Safety
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class='welcome-text'>
        Where should we begin?
        </div>
        """,
        unsafe_allow_html=True
    )


    # Feature Cards

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            """
            <div class='feature-card'>

            <div class='feature-icon'>🔍</div>

            <div class='feature-title'>
            Threat Analysis
            </div>

            <div class='feature-description'>
            Understand cyber threats
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            """
            <div class='feature-card'>

            <div class='feature-icon'>📧</div>

            <div class='feature-title'>
            Phishing Detection
            </div>

            <div class='feature-description'>
            Identify suspicious messages
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            """
            <div class='feature-card'>

            <div class='feature-icon'>🔐</div>

            <div class='feature-title'>
            Password Safety
            </div>

            <div class='feature-description'>
            Improve account security
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            """
            <div class='feature-card'>

            <div class='feature-icon'>🌐</div>

            <div class='feature-title'>
            Digital Privacy
            </div>

            <div class='feature-description'>
            Protect your online identity
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):

            st.markdown(message.content)


    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):

            st.markdown(message.content)


# =========================================================
# CHAT INPUT
# =========================================================

user_prompt = st.chat_input(
    "Ask anything about cybersecurity..."
)


# =========================================================
# AI RESPONSE
# =========================================================

if user_prompt:


    # Show User Message

    with st.chat_message("user"):

        st.markdown(user_prompt)


    # Save User Message

    st.session_state.messages.append(

        HumanMessage(
            content=user_prompt
        )

    )


    try:


        # Initialize Model

        chat = ChatOpenAI(
    model="gpt-5.6-luna",
    temperature=0.3,
    api_key=st.session_state.api_key
)


        # Complete Conversation

        conversation = [

            SystemMessage(
                content=SYSTEM_PROMPT
            )

        ] + st.session_state.messages


        # Generate Response

        with st.chat_message("assistant"):

            with st.spinner(
                "🛡️ CyberGuard is analyzing..."
            ):

                response = chat.invoke(
                    conversation
                )


            st.markdown(
                response.content
            )


        # Save Response

        st.session_state.messages.append(

            AIMessage(
                content=response.content
            )

        )


    except Exception as error:

        st.error(
            f"Connection Error: {error}"
        )

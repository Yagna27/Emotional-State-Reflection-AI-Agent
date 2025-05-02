import streamlit as st
from agent import analyze_emotion, reframe_emotion

st.set_page_config(page_title="EmoSynth Agent", layout="centered")

st.title("🧠 EmoSynth: Your Mindset Reframer")
st.markdown("Describe how you're feeling, and let EmoSynth reflect it back with wisdom.")

# User Input
user_input = st.text_area("What's on your mind?", height=150)

# Style Selector
style = st.selectbox("Choose a mindset style for reframing:", ["Stoic", "Therapist", "Coach", "Optimist", "Realist"])

# Button to trigger
if st.button("Analyze & Reframe"):
    with st.spinner("Analyzing your emotion..."):
        emotion_result = analyze_emotion(user_input)
    
    with st.spinner(f"Reframing your thoughts with {style} wisdom..."):
        reframed = reframe_emotion(user_input, style)

    st.subheader("🔍 Detected Emotion")
    st.success(emotion_result)

    st.subheader(f"🪞 {style} Reflection")
    st.info(reframed)

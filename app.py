import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv("D:\AI_Assistant\Data\quiz data1.csv")

# Set the app title
st.set_page_config(page_title="AI Quiz & Recommendation System", layout="centered")
st.title("📘 AI Quiz for Students")

# Page selector
page = st.sidebar.radio("Go to", ["Quiz", "Recommendations"])

# Store user answers in session
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Quiz page
if page == "Quiz":
    st.subheader("🧠 Take the Quiz")
    for idx, row in df.iterrows():
        st.markdown(f"**Q{idx + 1}. {row['question']}**")

        # Options
        options = {
            "A": row["option_a"],
            "B": row["option_b"],
            "C": row["option_c"],
            "D": row["option_d"]
        }

        # Show options as radio buttons
        selected = st.radio(
            label="Select an option",
            options=list(options.keys()),
            format_func=lambda x: f"{x}. {options[x]}",
            key=f"q_{idx}"
        )

        st.session_state.answers[idx] = selected

    if st.button("Submit Quiz"):
        score = 0
        wrong_questions = []

        for idx, row in df.iterrows():
            correct_option = row['correct_option'].strip().upper()
            user_ans = st.session_state.answers.get(idx)

            if user_ans == correct_option:
                score += 1
            else:
                wrong_questions.append((row['question'], correct_option, user_ans))

        st.success(f"✅ You scored {score} out of {len(df)}")

        if wrong_questions:
            st.warning("Here are the questions you got wrong:")
            for q, correct, your_ans in wrong_questions:
                st.markdown(f"- **{q}**")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;✅ Correct: {correct}, ❌ Your answer: {your_ans}")

        # Store wrong question indices
        st.session_state.wrong_q_indices = [df.iloc[idx]["topic"] for idx, row in enumerate(df.iterrows()) if st.session_state.answers.get(idx) != row[1]["correct_option"].strip().upper()]

# Recommendations page
elif page == "Recommendations":
    st.subheader("📚 Recommended Topics for You")
    if "wrong_q_indices" in st.session_state and st.session_state.wrong_q_indices:
        topics = st.session_state.wrong_q_indices
        recommended_topics = set(topics)
        for topic in recommended_topics:
            st.markdown(f"- 🔁 Revise: **{topic}**")
    else:
        st.info("✅ No topics to recommend. Great job on the quiz!")

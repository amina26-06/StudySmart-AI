import streamlit as st
import pandas as pd
import os
from datetime import datetime
st.set_page_config(
    page_title="StudySmart AI",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎓 StudySmart AI")
st.sidebar.write("Your Intelligent Learning Companion")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📚 Study Tracker",
        "📊 Analytics Dashboard",
        "🤖 AI Study Mentor",
        "🧠 Decision Assistant",
        "🔍 TrustCheck AI",
        "📝 Technology Quiz"
    ]
)

# HOME PAGE
if page == "🏠 Home":
    st.title("🎓 Welcome to StudySmart AI")
    st.subheader("An Intelligent Learning and Productivity Companion")

    st.write("""
    StudySmart AI helps students organize their learning journey,
    track study progress, analyze productivity, make better decisions,
    and improve technology knowledge.
    """)

    st.success("✨ Learn smarter. Track better. Grow stronger!")

# STUDY TRACKER PAGE
elif page == "📚 Study Tracker":
    st.title("📚 Study Tracker")
    st.write("Track your subjects, topics, study hours, and completed tasks.")

    # CSV file name
    file_name = "study_data.csv"

    # Create the CSV file if it doesn't exist
    if not os.path.exists(file_name):
        df = pd.DataFrame(
            columns=["Date", "Subject", "Topic", "Study Hours", "Status"]
        )
        df.to_csv(file_name, index=False)

    # Study session form
    with st.form("study_form", clear_on_submit=True):
        subject = st.text_input("📖 Subject")
        topic = st.text_input("📝 Topic")

        study_hours = st.number_input(
            "⏱️ Study Hours",
            min_value=0.0,
            max_value=24.0,
            step=0.5
        )

        status = st.selectbox(
            "✅ Task Status",
            ["Completed", "In Progress", "Not Started"]
        )

        submitted = st.form_submit_button("➕ Add Study Session")

    # Save data
    if submitted:
        if subject and topic:
            new_data = pd.DataFrame({
                "Date": [datetime.now().strftime("%Y-%m-%d")],
                "Subject": [subject],
                "Topic": [topic],
                "Study Hours": [study_hours],
                "Status": [status]
            })

            new_data.to_csv(
                file_name,
                mode="a",
                header=False,
                index=False
            )

            st.success("🎉 Study session saved successfully!")

        else:
            st.warning("⚠️ Please enter both Subject and Topic.")

    # Show saved data
    st.subheader("📋 Your Study History")

    study_data = pd.read_csv(file_name)

    if not study_data.empty:
        st.dataframe(study_data, use_container_width=True)
    else:
        st.info("No study sessions added yet.")
# ANALYTICS PAGE
elif page == "📊 Analytics Dashboard":
    st.title("📊 Analytics Dashboard")
    st.write("Visualize your learning progress and study patterns.")

    file_name = "study_data.csv"

    if os.path.exists(file_name):

        study_data = pd.read_csv(file_name)

        if not study_data.empty:

            # Convert Date column
            study_data["Date"] = pd.to_datetime(study_data["Date"])

            # Calculate metrics
            total_hours = study_data["Study Hours"].sum()
            total_sessions = len(study_data)
            completed_tasks = len(
                study_data[study_data["Status"] == "Completed"]
            )

            # Display metrics
            col1, col2, col3 = st.columns(3)

            col1.metric("⏱️ Total Study Hours", f"{total_hours:.1f}")
            col2.metric("📚 Study Sessions", total_sessions)
            col3.metric("✅ Completed Tasks", completed_tasks)

            st.divider()

            # Subject-wise study hours
            st.subheader("📚 Study Hours by Subject")

            subject_hours = study_data.groupby(
                "Subject"
            )["Study Hours"].sum()

            st.bar_chart(subject_hours)

            # Study hours over time
            st.subheader("📈 Study Hours Over Time")

            daily_hours = study_data.groupby(
                "Date"
            )["Study Hours"].sum()

            st.line_chart(daily_hours)

            # Status distribution
            st.subheader("📊 Task Status Overview")

            status_count = study_data["Status"].value_counts()

            st.bar_chart(status_count)

        else:
            st.info("📚 No study data available yet.")

    else:
        st.warning("⚠️ Please add study sessions first!")

# AI STUDY MENTOR PAGE
# AI STUDY MENTOR PAGE
elif page == "🤖 AI Study Mentor":
    st.title("🤖 AI Study Mentor")
    st.write("Ask questions and get learning guidance.")

    st.subheader("💬 Ask Your Study Question")

    question = st.text_area(
        "What do you need help with?",
        placeholder="Example: How can I prepare for my exams effectively?"
    )

    if st.button("✨ Get Study Guidance"):
        if question.strip():
            st.success("Here is your study guidance:")

            st.write(
                "📚 Break your topic into smaller parts and study one concept at a time."
            )

            st.write(
                "📝 Make short notes and revise them regularly."
            )

            st.write(
                "⏰ Use focused study sessions with short breaks."
            )

            st.write(
                "🧠 Practice questions to test your understanding."
            )

            st.info(
                f"💡 Your question was: {question}"
            )

        else:
            st.warning("⚠️ Please enter a question first!")

# DECISION ASSISTANT PAGE
elif page == "🧠 Decision Assistant":
    st.title("🧠 Study Decision Assistant")
    st.write("Compare two learning options using a weighted scoring system.")

    st.subheader("🤔 What do you want to compare?")

    option1 = st.text_input("Option 1", placeholder="Example: Python")
    option2 = st.text_input("Option 2", placeholder="Example: Java")

    st.subheader("⭐ Rate each option from 1 to 10")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### 📘 {option1 if option1 else 'Option 1'}")

        career1 = st.slider("Career Value (Option 1)", 1, 10, 5)
        interest1 = st.slider("Personal Interest (Option 1)", 1, 10, 5)
        difficulty1 = st.slider("Ease of Learning (Option 1)", 1, 10, 5)
        urgency1 = st.slider("Current Priority (Option 1)", 1, 10, 5)

    with col2:
        st.markdown(f"### 📕 {option2 if option2 else 'Option 2'}")

        career2 = st.slider("Career Value (Option 2)", 1, 10, 5)
        interest2 = st.slider("Personal Interest (Option 2)", 1, 10, 5)
        difficulty2 = st.slider("Ease of Learning (Option 2)", 1, 10, 5)
        urgency2 = st.slider("Current Priority (Option 2)", 1, 10, 5)

    st.subheader("⚖️ Choose Importance of Each Factor")

    weight_career = st.slider("Career Value Importance", 1, 5, 5)
    weight_interest = st.slider("Personal Interest Importance", 1, 5, 4)
    weight_difficulty = st.slider("Ease of Learning Importance", 1, 5, 3)
    weight_urgency = st.slider("Current Priority Importance", 1, 5, 4)

    if st.button("🧠 Compare Options"):

        score1 = (
            career1 * weight_career +
            interest1 * weight_interest +
            difficulty1 * weight_difficulty +
            urgency1 * weight_urgency
        )

        score2 = (
            career2 * weight_career +
            interest2 * weight_interest +
            difficulty2 * weight_difficulty +
            urgency2 * weight_urgency
        )

        st.divider()

        st.subheader("📊 Decision Result")

        result_col1, result_col2 = st.columns(2)

        result_col1.metric(
            option1 if option1 else "Option 1",
            score1
        )

        result_col2.metric(
            option2 if option2 else "Option 2",
            score2
        )

        if score1 > score2:
            st.success(
                f"🏆 Based on your ratings, **{option1}** is the better choice!"
            )

        elif score2 > score1:
            st.success(
                f"🏆 Based on your ratings, **{option2}** is the better choice!"
            )

        else:
            st.info("🤝 Both options have the same score!")

# TRUSTCHECK PAGE

elif page == "🔍 TrustCheck AI":
    st.title("🔍 TrustCheck AI")
    st.write("Analyze claims and learn whether they need additional verification.")

    claim = st.text_area(
        "📝 Enter a claim or piece of information:",
        placeholder="Example: AI will completely replace all programmers."
    )

    if st.button("🔍 Analyze Claim"):

        if claim.strip():

            # Convert claim to lowercase for analysis
            claim_lower = claim.lower()

            # Lists of words to detect
            absolute_words = [
                "always", "never", "everyone", "nobody",
                "all", "completely", "guaranteed"
            ]

            sensational_words = [
                "shocking", "unbelievable", "secret",
                "miracle", "100%", "definitely"
            ]

            # Find detected words
            found_absolute = [
                word for word in absolute_words
                if word in claim_lower
            ]

            found_sensational = [
                word for word in sensational_words
                if word in claim_lower
            ]

            st.subheader("🧠 TrustCheck Analysis")

            # Risk score
            risk_score = 0

            if found_absolute:
                risk_score += 2

                st.warning(
                    f"⚠️ Broad or absolute language detected: "
                    f"{', '.join(found_absolute)}"
                )

                st.write(
                    "Absolute statements are often difficult to prove "
                    "and should be checked carefully."
                )

            if found_sensational:
                risk_score += 2

                st.warning(
                    f"🚨 Sensational language detected: "
                    f"{', '.join(found_sensational)}"
                )

            # Check claim length
            if len(claim.split()) < 5:
                risk_score += 1
                st.warning(
                    "⚠️ This claim contains very little context. "
                    "More information may be needed."
                )

            # Source check
            st.info(
                "📚 Source Check: Does this claim include a reliable "
                "source or supporting evidence?"
            )

            st.divider()

            # Final result
            st.subheader("🎯 TrustCheck Result")

            if risk_score >= 4:
                st.error(
                    "🔴 HIGH VERIFICATION NEEDED\n\n"
                    "This claim contains language that may be exaggerated "
                    "or overly broad. Verify it using multiple reliable sources."
                )
            elif risk_score >= 2:
                st.warning(
                    "🟡 MODERATE VERIFICATION NEEDED\n\n"
                    "This claim should be checked before being trusted or shared."
                )

            else:
                st.success(
                    "🟢 NO OBVIOUS LANGUAGE WARNING DETECTED\n\n"
                    "However, this does not prove the claim is true. "
                    "Always verify important information using reliable sources."
                )

            st.divider()

            st.subheader("✅ How to Verify This Information")

            st.write("""
1. Check who originally made the claim.
2. Look for reliable sources and evidence.
3. Compare information from multiple trusted sources. 
4. Check whether the information is recent.
5. Be careful with exaggerated or emotional language.
""")

elif page == "📝 Technology Quiz":
    st.title("📝 Technology Literacy Quiz")
    st.write("Test your knowledge of modern technologies!")

    questions = [
        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automated Internet",
                "Advanced Information",
                "Artificial Integration"
            ],
            "answer": "Artificial Intelligence"
        },
        {
            "question": "What is Cloud Computing?",
            "options": [
                "Storing and accessing computing resources over the internet",
                "A type of computer hardware",
                "A weather prediction system",
                "A programming language"
            ],
            "answer": "Storing and accessing computing resources over the internet"
        },
        {
            "question": "What is Blockchain mainly used for?",
            "options": [
                "A secure distributed record of transactions",
                "Creating computer games",
                "Designing websites",
                "Sending emails"
            ],
            "answer": "A secure distributed record of transactions"
        },
        {
            "question": "What is Cybersecurity?",
            "options": [
                "Protecting systems and data from digital attacks",
                "Creating social media applications",
                "Improving internet speed",
                "Building robots"
            ],
            "answer": "Protecting systems and data from digital attacks"
        },
        {
            "question": "Which of these is commonly used in Machine Learning?",
            "options": [
                "Training data",
                "Keyboard design",
                "Printer ink",
                "Computer wallpaper"
            ],
            "answer": "Training data"
        }
    ]

    st.subheader("Answer the questions below 👇")

    user_answers = []

    for i, question in enumerate(questions):
        answer = st.radio(
            f"Q{i + 1}. {question['question']}",
            question["options"],
            key=f"question_{i}"
        )

        user_answers.append(answer)

    if st.button("📊 Submit Quiz"):

        score = 0

        for i, question in enumerate(questions):
            if user_answers[i] == question["answer"]:
                score += 1

        st.divider()

        st.subheader("🎉 Quiz Result")

        st.metric(
            "Your Score",
            f"{score} / {len(questions)}"
        )

        percentage = (score / len(questions)) * 100

        if percentage == 100:
            st.success("🏆 Excellent! You got all answers correct!")

        elif percentage >= 60:
            st.success("👏 Good job! Keep learning and improving!")

        else:
            st.warning("📚 Keep practicing! Learning takes time.")

        st.write(f"### 📈 Score Percentage: {percentage:.0f}%")
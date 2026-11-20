import streamlit as st
from pdf_processor import extract_text_from_pdf
from ai_engine import generate_summary, generate_flashcards, generate_quiz, get_next_difficulty

st.set_page_config(page_title="Smart Study Guide AI", page_icon="📚", layout="wide")

DEFAULTS = {
    "study_text": "",
    "summary": None,
    "flashcards": None,
    "quiz": None,
    "quiz_results": None,
    "difficulty": "Medium",
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.title("📚 Smart Study Guide & Practice Quiz Generator")
st.write("Turn lecture notes and course PDFs into study guides, flashcards, and adaptive practice quizzes.")

st.sidebar.header("Study Settings")
quiz_count = st.sidebar.slider("Number of quiz questions", 3, 15, 5)
flashcard_count = st.sidebar.slider("Number of flashcards", 5, 30, 10)
difficulty = st.sidebar.selectbox(
    "Quiz difficulty", ["Easy", "Medium", "Hard"],
    index=["Easy", "Medium", "Hard"].index(st.session_state.difficulty)
)

st.header("1. Add your study material")
uploaded_file = st.file_uploader("Upload a text-based PDF", type=["pdf"])
if uploaded_file is not None and st.button("Extract PDF text"):
    try:
        with st.spinner("Extracting PDF text..."):
            st.session_state.study_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted.")
    except Exception as exc:
        st.error(str(exc))

manual_text = st.text_area(
    "Or paste your lecture notes here",
    height=220,
    placeholder="Paste your notes, textbook excerpts, or course material..."
)
if manual_text.strip():
    st.session_state.study_text = manual_text

if st.session_state.study_text:
    st.success(f"Study material ready: {len(st.session_state.study_text):,} characters")
    with st.expander("Preview study material"):
        st.text(st.session_state.study_text[:5000])

st.divider()
st.header("2. Generate learning materials")
c1, c2, c3 = st.columns(3)

def show_error(exc):
    st.error(f"Could not complete the request: {exc}")

with c1:
    if st.button("📝 Generate summary", use_container_width=True):
        if not st.session_state.study_text.strip():
            st.warning("Add study material first.")
        else:
            try:
                with st.spinner("Generating summary..."):
                    st.session_state.summary = generate_summary(st.session_state.study_text)
            except Exception as exc:
                show_error(exc)

with c2:
    if st.button("🗂️ Generate flashcards", use_container_width=True):
        if not st.session_state.study_text.strip():
            st.warning("Add study material first.")
        else:
            try:
                with st.spinner("Creating flashcards..."):
                    st.session_state.flashcards = generate_flashcards(
                        st.session_state.study_text, flashcard_count
                    )
            except Exception as exc:
                show_error(exc)

with c3:
    if st.button("🎯 Generate quiz", use_container_width=True):
        if not st.session_state.study_text.strip():
            st.warning("Add study material first.")
        else:
            try:
                with st.spinner("Generating quiz..."):
                    st.session_state.quiz = generate_quiz(
                        st.session_state.study_text, quiz_count, difficulty
                    )
                    st.session_state.quiz_results = None
            except Exception as exc:
                show_error(exc)

if st.session_state.summary:
    st.divider()
    st.header("📖 Your study guide")
    summary = st.session_state.summary
    st.subheader(summary.title)
    st.write(summary.overview)
    for heading, items in [
        ("Key concepts", summary.key_concepts),
        ("Important terms", summary.important_terms),
        ("Study tips", summary.study_tips),
    ]:
        st.subheader(heading)
        for item in items:
            st.markdown(f"- {item}")

if st.session_state.flashcards:
    st.divider()
    st.header("🗂️ Flashcard practice")
    for i, card in enumerate(st.session_state.flashcards.flashcards, start=1):
        with st.expander(f"Card {i}: {card.question}"):
            st.markdown("**Answer**")
            st.write(card.answer)

if st.session_state.quiz:
    st.divider()
    st.header("🎯 Practice quiz")
    questions = st.session_state.quiz.questions
    with st.form("quiz_form"):
        answers = []
        for i, question in enumerate(questions):
            st.subheader(f"Question {i + 1}")
            st.write(question.question)
            answers.append(st.radio(
                "Choose one answer",
                question.options,
                index=None,
                key=f"quiz_{id(st.session_state.quiz)}_{i}",
            ))
            st.caption(f"Difficulty: {question.difficulty}")
        submitted = st.form_submit_button("Submit quiz", use_container_width=True)

    if submitted:
        if any(answer is None for answer in answers):
            st.warning("Please answer every question before submitting.")
        else:
            results = []
            correct = 0
            for question, answer in zip(questions, answers):
                is_correct = answer == question.correct_answer
                correct += int(is_correct)
                results.append({
                    "question": question.question,
                    "user_answer": answer,
                    "correct_answer": question.correct_answer,
                    "is_correct": is_correct,
                    "explanation": question.explanation,
                    "options": question.options,
                    "option_explanations": question.option_explanations,
                })
            score = round(correct / len(questions) * 100)
            st.session_state.quiz_results = {
                "score": score, "correct": correct,
                "total": len(questions), "results": results,
            }
            st.session_state.difficulty = get_next_difficulty(score)

if st.session_state.quiz_results:
    result = st.session_state.quiz_results
    st.divider()
    st.header("📊 Quiz results")
    st.metric("Your score", f"{result['score']}%")
    st.write(f"Correct answers: {result['correct']} / {result['total']}")
    if result["score"] >= 80:
        st.success("Excellent work! Try a harder quiz next.")
    elif result["score"] >= 50:
        st.info("Good effort. Review the explanations and practice again.")
    else:
        st.warning("Review the study guide and try an easier quiz.")
    st.subheader("Answer explanations")
    for i, item in enumerate(result["results"], start=1):
        with st.expander(f"Question {i}: {'Correct' if item['is_correct'] else 'Incorrect'}"):
            st.write(item["question"])
            st.write(f"**Your answer:** {item['user_answer']}")
            st.write(f"**Correct answer:** {item['correct_answer']}")
            st.write(item["explanation"])
            st.markdown("**Explanation for each option**")
            for option, explanation in zip(item["options"], item["option_explanations"]):
                st.markdown(f"- **{option}:** {explanation}")
    st.info(f"Recommended difficulty for your next quiz: {st.session_state.difficulty}")
    if st.button("🔄 Generate another quiz"):
        try:
            with st.spinner("Generating your next quiz..."):
                st.session_state.quiz = generate_quiz(
                    st.session_state.study_text, quiz_count, st.session_state.difficulty
                )
                st.session_state.quiz_results = None
            st.rerun()
        except Exception as exc:
            show_error(exc)

st.divider()
st.caption("Smart Study Guide & Practice Quiz Generator | Python • Streamlit • OpenAI")

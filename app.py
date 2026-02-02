import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Malose Jim | Mathematics Researcher",
    page_icon="📐",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main {
    padding: 2rem;
}
h1, h2, h3 {
    color: #1f4e79;
}
.sidebar .sidebar-content {
    background-color: #1f4e79;
}
.sidebar h2 {
    color: white;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About Me", "Education & Research", "Teaching & Experience", "Interactive Mathematics", "Contact"]
)

# ---------------- HOME ----------------
if page == "Home":
    st.title("📐 Malose Jim Mokonyama")
    st.subheader("MSc Mathematics Student | Researcher | Academic Tutor")

    st.markdown("""
    <div class="card">
    Welcome to my **researcher profile app** built with **Streamlit**.

    I am a Mathematics Master's student passionate about:
    - Pure & Applied Mathematics  
    - Research & Teaching  
    - Making Mathematics **accessible and exciting**  

    This app showcases my **academic journey, research interests, and an interactive maths experience** for learners.
    </div>
    """, unsafe_allow_html=True)

# ---------------- ABOUT ME ----------------
elif page == "About Me":
    st.header("👤 About Me")

    st.markdown("""
    <div class="card">
    I am a motivated and detail-oriented **Mathematics Master's student** with strong analytical,
    problem-solving, and quantitative skills.

    I have experience in:
    - Mathematical research  
    - Data analysis  
    - Academic tutoring  
    - Python & LaTeX  

    My goal is to **inspire learners** and contribute to research-driven mathematical solutions.
    </div>
    """, unsafe_allow_html=True)

# ---------------- EDUCATION & RESEARCH ----------------
elif page == "Education & Research":
    st.header("🎓 Education & Research")

    st.markdown("""
    <div class="card">
    **Bachelor of Science (Mathematics & Physics)**  
    *Sefako Makgatho Health Sciences University*  
    **Average:** 74%

    **BSc Honours in Mathematics**  
    *Sefako Makgatho Health Sciences University*  
    **Average:** 79% (Cum Laude)

    **Master of Science in Mathematics (Current)**  
    Research focus includes:
    - Mathematical analysis  
    - Topology & advanced structures  
    - Data science & machine learning applications
    </div>
    """, unsafe_allow_html=True)

    st.latex(r"\int_0^1 x^2 dx = \frac{1}{3}")
    st.caption("Mathematics is the language of the universe.")

# ---------------- TEACHING & EXPERIENCE ----------------
elif page == "Teaching & Experience":
    st.header("📘 Teaching & Experience")

    st.markdown("""
    <div class="card">
    **Academic Tutor** – Sefako Makgatho Health Sciences University  
    *(2025 – Present)*  

    - One-on-one and group tutoring  
    - Lesson planning and mentorship  

    **Mathematics Tutor** – Rostec College  
    *(2020 – 2023)*  

    - Student support & academic development  
    - Mathematics enrichment programs  
    </div>
    """, unsafe_allow_html=True)

# ---------------- INTERACTIVE MATHEMATICS ----------------
elif page == "Interactive Mathematics":
    st.header("🎲 Explore Mathematics (Interactive Zone)")

    st.markdown("""
    <div class="card">
    This section is designed to **make learners fall in love with mathematics**.
    Try changing the slider and see mathematics come alive!
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📈 Trigonometric Animation")

    n = st.slider("Choose number of points", 50, 500, 200)
    x = np.linspace(0, 2*np.pi, n)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("y = sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    st.pyplot(fig)

    st.latex(r"y = \sin(x)")
    st.caption("This simple wave explains sound, light, and even quantum mechanics!")

    st.subheader("🧠 Mini Math Challenge")

    answer = st.number_input("What is the value of ∫₀¹ 2x dx ?", step=0.1)

    if st.button("Check Answer"):
        if abs(answer - 1) < 0.01:
            st.success("🎉 Correct! You're thinking like a mathematician.")
        else:
            st.error("❌ Not quite. Try again!")

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.header("📬 Contact")

    st.markdown("""
    <div class="card">
    Email: malosejim421@gmail.com  \n
    Phone: 079 897 6062  
    Location: Pretoria, South Africa  

    *Let's collaborate, learn, and grow mathematics together.*
    </div>
    """, unsafe_allow_html=True)

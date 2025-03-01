import streamlit as st
from src.model import compute_similarity

st.title('AI Resume Screening & Candidate Ranking System')

job_desc = st.text_area('Enter Job Description:', '')

if st.button('Find Best Candidates'):
    if job_desc:
        results = compute_similarity(job_desc)
        st.write('### Top 10 Matching Resumes:')
        for file, score in results:
            st.write(f'{file} - Similarity Score: {score:.2f}')
    else:
        st.warning('Please enter a job description.')

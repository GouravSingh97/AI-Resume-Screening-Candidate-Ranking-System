import numpy as np
import os
import glob
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocessing import clean_text

def load_resumes():
    resumes = []
    files = glob.glob('dataset/*.txt')
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            resumes.append(clean_text(f.read()))
    return resumes, files

def compute_similarity(job_description):
    resumes, filenames = load_resumes()
    all_texts = [clean_text(job_description)] + resumes
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])[0]
    ranked_resumes = sorted(zip(filenames, similarity_scores), key=lambda x: x[1], reverse=True)
    return ranked_resumes[:10]

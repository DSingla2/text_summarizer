import streamlit as st
import torch
torch.classes.__path__ = []
from transformers import pipeline
st.title("Text_Summarizer")
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

#User Input
text= st.text_area("Paste your paragraph here: ")

if st.button("Summarize"): 
    if not text.strip(): 
        st.warning("Please enter some text.")
    else: 
        summary = summarizer(text, max_length= 100)
        st.subheader("Summary: ")
        st.write(summary[0]['summary_text'])
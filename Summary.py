import streamlit as st
import fitz  # PyMuPDF for extracting text
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "".join([page.get_text("text") for page in doc])
    return text

def summarize_text(text, num_sentences=5):
    """Summarize the extracted text."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

def main():
    st.title("PDF Summarizer")
    st.write("Upload a PDF and get a summarized version of its content.")
    
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            text = extract_text_from_pdf(uploaded_file)
            
        if text:
            num_sentences = st.slider("Number of summary sentences", 1, 10, 5)
            
            with st.spinner("Generating summary..."):
                summary = summarize_text(text, num_sentences)
                
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Could not extract text from the PDF. Make sure it's not a scanned document.")

if __name__ == "__main__":
    main()

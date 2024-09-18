import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Load NLTK data (this may require an internet connection)
nltk.download('punkt')

def process_description(description):
    # Tokenization
    tokens = word_tokenize(description)
    
    # TF-IDF or simple keyword extraction (replace with actual model if needed)
    tfidf_vectorizer = TfidfVectorizer()
    keywords = tfidf_vectorizer.fit_transform([description]).toarray()
    
    return keywords

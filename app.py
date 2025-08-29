from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

def clean_text(text):
    """Clean text and get words"""
    text = re.sub(r'[^a-z\s]', '', text.lower())
    return text.split()

def char_similarity(text1, text2):
    """Calculate character-level similarity using longest common subsequence"""
    text1 = re.sub(r'[^a-z]', '', text1.lower())
    text2 = re.sub(r'[^a-z]', '', text2.lower())
    
    if not text1 or not text2:
        return 0.0
    
    # Simple character overlap
    set1, set2 = set(text1), set(text2)
    common_chars = len(set1 & set2)
    total_chars = len(set1 | set2)
    
    return common_chars / total_chars if total_chars > 0 else 0.0

def cosine_sim(text1, text2):
    """Calculate cosine similarity"""
    try:
        vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
        matrix = vectorizer.fit_transform([text1, text2])
        return float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0])
    except:
        return 0.0

def jaccard_sim(words1, words2):
    """Calculate Jaccard similarity"""
    set1, set2 = set(words1), set(words2)
    if not set1 and not set2:
        return 1.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0

def word_overlap(words1, words2):
    """Calculate word overlap percentage"""
    set1, set2 = set(words1), set(words2)
    if not set1 and not set2:
        return 100.0
    shared = len(set1 & set2)
    total = len(set1) + len(set2)
    return (shared * 2 / total * 100) if total > 0 else 0.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    text1 = data.get('text1', '').strip()
    text2 = data.get('text2', '').strip()
    
    if not text1 or not text2:
        return jsonify({'error': 'Please enter both texts'}), 400
    
    words1 = clean_text(text1)
    words2 = clean_text(text2)
    
    shared_words = sorted(list(set(words1) & set(words2)))
    unique1 = sorted(list(set(words1) - set(words2)))
    unique2 = sorted(list(set(words2) - set(words1)))
    
    result = {
        'cosine_similarity': cosine_sim(text1, text2),
        'jaccard_index': jaccard_sim(words1, words2),
        'word_overlap': word_overlap(words1, words2),
        'character_similarity': char_similarity(text1, text2),
        'edit_distance': abs(len(text1) - len(text2)),  # Simple length difference
        'shared_words': shared_words,
        'unique_text1': unique1,
        'unique_text2': unique2,
        'stats': {
            'text1_words': len(words1),
            'text2_words': len(words2),
            'text1_chars': len(text1),
            'text2_chars': len(text2),
            'total_unique_words': len(set(words1) | set(words2))
        }
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import os
from dotenv import load_dotenv
import re
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Gemini API configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}'

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

def call_gemini_api(prompt):
    """Make HTTP request to Gemini API"""
    try:
        if not GEMINI_API_KEY:
            return None
            
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            if 'candidates' in data and len(data['candidates']) > 0:
                if 'content' in data['candidates'][0] and 'parts' in data['candidates'][0]['content']:
                    return data['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"Gemini API error: {response.status_code} - {response.text}")
            
        return None
        
    except Exception as e:
        print(f"Error calling Gemini API: {str(e)}")
        return None

def gemini_similarity_analysis(text1, text2):
    """Use Gemini AI to analyze text similarity and provide insights"""
    try:
        prompt = f"""
        Analyze the similarity between these two texts and provide a comprehensive analysis:

        Text 1: "{text1[:500]}..."
        
        Text 2: "{text2[:500]}..."

        Please provide:
        1. A similarity score from 0.0 to 1.0 based on semantic meaning
        2. Key insights about the relationship between the texts
        3. What makes them similar or different
        4. The main themes or topics in each text
        5. Any notable patterns or writing styles

        Format your response as JSON with these fields:
        {{
            "semantic_similarity": <float between 0.0 and 1.0>,
            "insights": "<string with analysis>",
            "themes_text1": ["<theme1>", "<theme2>"],
            "themes_text2": ["<theme1>", "<theme2>"],
            "key_differences": "<string>",
            "writing_style_comparison": "<string>"
        }}
        """
        
        response_text = call_gemini_api(prompt)
        
        if response_text:
            # Try to parse JSON from response
            try:
                # Extract JSON content between braces
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start != -1 and end != 0:
                    json_str = response_text[start:end]
                    parsed = json.loads(json_str)
                    # Ensure semantic_similarity is a float
                    if 'semantic_similarity' in parsed:
                        parsed['semantic_similarity'] = float(parsed['semantic_similarity'])
                    return parsed
            except json.JSONDecodeError:
                # If JSON parsing fails, create response from text
                pass
        
        # Fallback: create structured response from text
        return {
            "semantic_similarity": 0.5,  # Default value
            "insights": response_text if response_text else "Unable to generate AI analysis. Please check your API key and internet connection.",
            "themes_text1": ["General content"],
            "themes_text2": ["General content"],
            "key_differences": "Analysis could not be completed",
            "writing_style_comparison": "Unable to compare writing styles"
        }
        
    except Exception as e:
        return {
            "semantic_similarity": 0.0,
            "insights": f"Gemini analysis unavailable: {str(e)}",
            "themes_text1": ["Analysis unavailable"],
            "themes_text2": ["Analysis unavailable"],
            "key_differences": "Gemini API error",
            "writing_style_comparison": "Unable to analyze due to API error"
        }

def gemini_improvement_suggestions(text1, text2, similarities):
    """Get improvement suggestions from Gemini"""
    try:
        prompt = f"""
        Based on these similarity metrics between two texts:
        - Cosine Similarity: {similarities.get('cosine_similarity', 0):.3f}
        - Character Similarity: {similarities.get('character_similarity', 0):.3f}
        - Jaccard Index: {similarities.get('jaccard_index', 0):.3f}
        - Word Overlap: {similarities.get('word_overlap', 0):.1f}%

        Text 1: "{text1[:200]}..."
        Text 2: "{text2[:200]}..."

        Provide 3 specific suggestions for improving text similarity if that was the goal. 
        Keep each suggestion under 50 words and focus on practical writing tips.
        Format as a simple numbered list.
        """
        
        response_text = call_gemini_api(prompt)
        return response_text if response_text else "No suggestions available. Please check your API key."
        
    except Exception as e:
        return f"Unable to generate suggestions: {str(e)}"

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
    
    # Calculate traditional similarities
    similarities = {
        'cosine_similarity': cosine_sim(text1, text2),
        'jaccard_index': jaccard_sim(words1, words2),
        'word_overlap': word_overlap(words1, words2),
        'character_similarity': char_similarity(text1, text2),
        'edit_distance': abs(len(text1) - len(text2))
    }
    
    # Get Gemini AI analysis
    gemini_analysis = gemini_similarity_analysis(text1, text2)
    improvement_suggestions = gemini_improvement_suggestions(text1, text2, similarities)
    
    result = {
        **similarities,
        'shared_words': shared_words,
        'unique_text1': unique1,
        'unique_text2': unique2,
        'stats': {
            'text1_words': len(words1),
            'text2_words': len(words2),
            'text1_chars': len(text1),
            'text2_chars': len(text2),
            'total_unique_words': len(set(words1) | set(words2))
        },
        'gemini_analysis': gemini_analysis,
        'improvement_suggestions': improvement_suggestions
    }
    
    return jsonify(result)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'gemini_configured': bool(GEMINI_API_KEY),
        'version': '3.0'
    })

if __name__ == '__main__':
    app.run(debug=True)

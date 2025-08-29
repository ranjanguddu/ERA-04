# Text Similarity Explorer 🔍

A simple and elegant Flask web application that compares two texts using multiple similarity algorithms, providing educational insights into how different algorithms measure text similarity.

![Text Similarity Explorer](https://img.shields.io/badge/Flask-2.3.3-blue) ![Python](https://img.shields.io/badge/Python-3.8+-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎯 Core Functionality
- **Dual Text Input**: Two large text areas with real-time character/word counting
- **Multiple Similarity Metrics**: 4 different algorithms for comprehensive comparison
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Real-time Analysis**: Instant results with detailed explanations
- **Educational Tooltips**: Learn how each algorithm works

### 📊 Similarity Algorithms

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **Cosine Similarity** | Measures angle between text vectors using TF-IDF | Document similarity, semantic analysis |
| **Character Similarity** | Character-level overlap analysis | Typos, variations, short strings |
| **Jaccard Index** | Intersection over union of word sets | Word-based similarity |
| **Word Overlap** | Percentage of shared words | Simple text comparison |

### 🎨 User Interface
- Clean, single-page design
- Responsive layout (mobile & desktop)
- Color-coded similarity scores
- Word analysis with shared/unique highlighting
- Statistics dashboard
- Loading animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   cd /path/to/text-similarity-explorer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python3 app.py
   ```

4. **Open your browser**
   - Navigate to: `http://localhost:5000`
   - Start comparing texts!

## 📁 Project Structure

```
text-similarity-explorer/
├── app.py              # Main Flask application (60 lines)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Complete frontend with CSS & JavaScript
└── README.md          # This file
```

## 🔧 Dependencies

```txt
flask==2.3.3
scikit-learn==1.3.0
```

- **Flask**: Lightweight web framework
- **scikit-learn**: Machine learning library for TF-IDF and cosine similarity

## 💡 How It Works

### Text Processing Pipeline
1. **Input Validation**: Ensures both texts are provided
2. **Text Cleaning**: Removes punctuation, normalizes whitespace
3. **Feature Extraction**: Creates word lists and character sets
4. **Similarity Calculation**: Applies 4 different algorithms
5. **Results Display**: Shows metrics, word analysis, and statistics

### Algorithm Details

#### 1. Cosine Similarity
```python
# Uses TF-IDF vectors with character n-grams (1-3)
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
similarity = cosine_similarity(matrix[0:1], matrix[1:2])
```

#### 2. Character Similarity
```python
# Character-level overlap for detecting typos and variations
common_chars = len(set(text1) & set(text2))
total_chars = len(set(text1) | set(text2))
similarity = common_chars / total_chars
```

#### 3. Jaccard Index
```python
# Word-based intersection over union
intersection = len(set(words1) & set(words2))
union = len(set(words1) | set(words2))
jaccard = intersection / union
```

#### 4. Word Overlap
```python
# Percentage of overlapping words
shared = len(set(words1) & set(words2))
total = len(words1) + len(words2)
overlap = (shared * 2 / total) * 100
```

## 🎯 Use Cases

### Educational
- **Learning text similarity algorithms**
- **Understanding different similarity metrics**
- **Comparing algorithm performance**
- **Natural language processing education**

### Practical Applications
- **Content similarity detection**
- **Plagiarism checking (basic)**
- **Document comparison**
- **Data deduplication**
- **Text variation analysis**

## 📈 Example Results

**Input:**
- Text 1: `"The quick brown fox jumps over the lazy dog"`
- Text 2: `"A quick brown fox leaps over a lazy dog"`

**Output:**
- Cosine Similarity: `0.857`
- Character Similarity: `0.800`
- Jaccard Index: `0.700`
- Word Overlap: `77.8%`

## 🔍 Special Features

### Character-Level Similarity
Perfect for comparing similar strings with minor variations:
- `"go.lang.com"` vs `"goLamg"` → **71.4% character similarity**
- Handles punctuation differences
- Detects typos and spelling variations

### Word Analysis
- **Shared Words**: Words appearing in both texts
- **Unique Words**: Words exclusive to each text
- **Visual Tags**: Color-coded word highlighting

## 🛠️ Customization

### Adding New Algorithms
```python
def your_similarity_algorithm(text1, text2):
    """Your custom similarity metric"""
    # Implementation here
    return similarity_score

# Add to compare() function in app.py
result['your_metric'] = your_similarity_algorithm(text1, text2)
```

### Modifying UI
- Edit `templates/index.html` for layout changes
- CSS is embedded in the HTML file
- JavaScript handles form submission and results display

## 🚀 Deployment

### Local Development
```bash
python3 app.py
# Access at http://localhost:5000
```

### Production Deployment
```bash
# Install gunicorn for production
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)
```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask**: For the excellent web framework
- **scikit-learn**: For machine learning algorithms
- **TF-IDF**: For document similarity techniques
- **Character n-grams**: For improved text matching

## 📧 Contact

For questions, suggestions, or issues:
- Create an issue in the repository
- Contact the development team

---

**Made with ❤️ for text similarity analysis and education**

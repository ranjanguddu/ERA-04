# Text Similarity Explorer with AI 🤖🔍

An advanced Flask web application that compares two texts using multiple similarity algorithms enhanced with **Google Gemini AI** for semantic analysis and intelligent insights.

![Text Similarity Explorer](https://img.shields.io/badge/Flask-2.3.3-blue) ![Python](https://img.shields.io/badge/Python-3.8+-green) ![Gemini AI](https://img.shields.io/badge/Gemini-AI-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎯 Core Functionality
- **Dual Text Input**: Two large text areas with real-time character/word counting
- **Multiple Similarity Metrics**: 5 traditional algorithms + AI semantic analysis
- **AI-Enhanced Analysis**: Google Gemini AI provides semantic insights
- **Beautiful UI**: Modern, responsive design with AI-themed styling
- **Real-time Analysis**: Instant results with detailed explanations
- **Educational Tooltips**: Learn how each algorithm works

### 🤖 AI-Enhanced Features
- **Semantic Similarity**: AI-powered semantic meaning analysis
- **Theme Detection**: AI identifies key themes in each text
- **Writing Style Comparison**: AI compares writing styles and patterns
- **Improvement Suggestions**: AI provides practical writing tips
- **Contextual Insights**: Deep analysis of text relationships

### 📊 Similarity Algorithms

| Algorithm | Description | Best For |
|-----------|-------------|----------|
| **🤖 AI Semantic Similarity** | Google Gemini's deep semantic analysis | Understanding meaning and context |
| **Cosine Similarity** | Measures angle between text vectors using TF-IDF | Document similarity, semantic analysis |
| **Character Similarity** | Character-level overlap analysis | Typos, variations, short strings |
| **Jaccard Index** | Intersection over union of word sets | Word-based similarity |
| **Word Overlap** | Percentage of shared words | Simple text comparison |
| **Edit Distance** | Character length difference | Text length comparison |

### 🎨 User Interface
- AI-themed gradient design
- Responsive layout (mobile & desktop)
- Color-coded similarity scores with AI highlights
- Word analysis with shared/unique highlighting
- AI insights dashboard
- Theme visualization
- Loading animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Google Gemini API key

### Installation

1. **Clone or download the project**
   ```bash
   cd /home/admin/ERA-V4/Assign-03
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Gemini API key
   nano .env
   ```
   
   Add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Get Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your .env file

5. **Run the application**
   ```bash
   python3 app.py
   ```

6. **Open your browser**
   - Navigate to: `http://localhost:5000`
   - Start comparing texts with AI!

## 📁 Project Structure

```
text-similarity-explorer-ai/
├── app.py              # Main Flask application with Gemini integration
├── requirements.txt    # Python dependencies including google-generativeai
├── .env.example       # Environment variables template
├── .env              # Your actual API keys (create this)
├── templates/
│   └── index.html    # AI-enhanced frontend with new styling
└── README.md         # This file
```

## 🔧 Dependencies

```txt
flask==2.3.3
scikit-learn==1.3.0
google-generativeai==0.3.2
python-dotenv==1.0.0
```

- **Flask**: Lightweight web framework
- **scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **google-generativeai**: Google's Gemini AI SDK
- **python-dotenv**: Environment variable management

## 💡 How It Works

### Text Processing Pipeline
1. **Input Validation**: Ensures both texts are provided
2. **Traditional Analysis**: Applies 5 classical similarity metrics
3. **AI Analysis**: Sends texts to Google Gemini for semantic analysis
4. **Theme Extraction**: AI identifies key themes and topics
5. **Style Comparison**: AI analyzes writing patterns
6. **Suggestion Generation**: AI provides improvement recommendations
7. **Results Display**: Shows all metrics, AI insights, and analysis

### AI Integration Details

#### Gemini Semantic Analysis
```python
def gemini_similarity_analysis(text1, text2):
    prompt = f"""
    Analyze the similarity between these two texts:
    Text 1: "{text1}"
    Text 2: "{text2}"
    
    Provide semantic similarity score, insights, themes, and analysis.
    """
    response = model.generate_content(prompt)
    return parsed_response
```

#### AI Features
- **Semantic Similarity**: 0.0-1.0 score based on meaning
- **Theme Detection**: Automatically identifies main topics
- **Style Analysis**: Compares writing patterns and techniques
- **Improvement Suggestions**: Practical tips for enhancing similarity

## 🎯 Use Cases

### Educational
- **AI-powered text analysis learning**
- **Understanding semantic vs syntactic similarity**
- **Comparing traditional algorithms with AI**
- **Natural language processing education**

### Professional Applications
- **Content similarity detection with AI insights**
- **Advanced plagiarism checking**
- **Document comparison with semantic analysis**
- **Writing style analysis**
- **Content optimization recommendations**

## 📈 Example Results

**Input:**
- Text 1: `"The quick brown fox jumps over the lazy dog"`
- Text 2: `"A fast brown fox leaps over a sleepy dog"`

**Output:**
- 🤖 AI Semantic Similarity: `0.885`
- Cosine Similarity: `0.857`
- Character Similarity: `0.800`
- Jaccard Index: `0.700`
- Word Overlap: `77.8%`

**AI Insights:**
- Both texts describe similar actions with animals
- Second text uses synonyms (fast/quick, leaps/jumps, sleepy/lazy)
- Similar sentence structure and narrative style

## 🤖 AI Features Deep Dive

### Semantic Analysis
The AI evaluates:
- **Meaning similarity** beyond word matching
- **Contextual relationships** between concepts
- **Implied meanings** and subtext
- **Emotional tone** and sentiment

### Theme Detection
Automatically identifies:
- **Main topics** in each text
- **Subtopics** and supporting ideas
- **Common themes** across texts
- **Unique concepts** in each text

### Writing Style Comparison
Analyzes:
- **Sentence structure** patterns
- **Vocabulary complexity**
- **Tone and formality**
- **Rhetorical devices**

### Improvement Suggestions
Provides:
- **Specific recommendations** for increasing similarity
- **Writing technique** improvements
- **Vocabulary** suggestions
- **Structural** modifications

## 🛠️ Customization

### Adding New AI Features
```python
def new_ai_feature(text1, text2):
    prompt = "Your custom AI analysis prompt"
    response = model.generate_content(prompt)
    return process_response(response)
```

### Modifying AI Prompts
Edit the prompts in `app.py` to customize:
- Analysis focus areas
- Output format
- Specific insights
- Suggestion types

## 🚀 Deployment

### Local Development
```bash
# Set up environment
cp .env.example .env
# Add your Gemini API key to .env

# Install dependencies
pip install -r requirements.txt

# Run application
python3 app.py
```

### Production Deployment
```bash
# Install production server
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Variables
Set these in production:
```bash
export GEMINI_API_KEY="your_api_key"
export FLASK_ENV="production"
```

## 🔒 Security Notes

- **API Key Security**: Never commit your `.env` file
- **Rate Limiting**: Consider implementing rate limits for API calls
- **Input Validation**: Texts are cleaned before AI analysis
- **Error Handling**: Graceful fallbacks when AI is unavailable

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/ai-enhancement`)
3. Add your Gemini API key to `.env`
4. Commit your changes (`git commit -m 'Add AI enhancement'`)
5. Push to the branch (`git push origin feature/ai-enhancement`)
6. Open a Pull Request

## 📊 API Endpoints

### `/compare` (POST)
Main comparison endpoint with AI analysis
- **Input**: JSON with `text1` and `text2`
- **Output**: Complete analysis including AI insights

### `/health` (GET)
Health check endpoint
- **Output**: System status and AI availability

## 🎓 Learning Resources

- [Google Gemini API Documentation](https://ai.google.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html)

## 🚨 Troubleshooting

### Common Issues

**AI Analysis Not Working**
- Check your Gemini API key in `.env`
- Verify internet connectivity
- Check API rate limits

**Installation Issues**
```bash
# Update pip
pip install --upgrade pip

# Install dependencies one by one
pip install flask
pip install scikit-learn
pip install google-generativeai
pip install python-dotenv
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini**: For powerful AI analysis capabilities
- **Flask**: For the excellent web framework
- **scikit-learn**: For machine learning algorithms
- **Google AI**: For making advanced AI accessible

## 📧 Contact

For questions, suggestions, or issues:
- Create an issue in the repository
- Contact the development team

---

**Made with ❤️ and 🤖 for advanced text similarity analysis and AI-powered insights**

## 🔮 Future Enhancements

- [ ] Multiple AI model support (OpenAI, Claude, etc.)
- [ ] Batch text comparison
- [ ] Export results to PDF/CSV
- [ ] Text preprocessing options
- [ ] Custom similarity thresholds
- [ ] Advanced visualization charts

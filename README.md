# 🤖 AI Resume Intelligence System

An AI-powered Resume Analysis and Evaluation System that uses **Natural Language Processing (NLP)** and **Machine Learning (ML)** to analyze resumes, match them with job descriptions, and generate intelligent insights similar to real-world Applicant Tracking Systems (ATS).

---

## 🚀 Features

### 🧠 AI & NLP Capabilities

* Semantic similarity using Sentence-BERT
* NLP-based keyword extraction with spaCy
* Lemmatization and stopword removal
* Context-aware resume understanding

### 📄 Resume Analysis

* Smart section detection (Education, Experience, Projects, Skills)
* Experience calculation from date ranges
* Dynamic skill extraction (Hybrid NLP + skill dictionary)
* Keyword relevance analysis

### 📊 Scoring System

* Machine Learning-based scoring (Linear Regression)
* Multi-factor evaluation:

  * Similarity Score
  * Skill Match Score
  * Keyword Score
  * Experience Score

### 🌐 Profile Enrichment

* GitHub profile integration
* Repository analysis
* Top programming languages extraction

### 💡 Feedback System

* Resume quality feedback
* Action verb detection
* Achievement-based suggestions

---

## 🏗️ Project Architecture

```
resume-ai/
│
├── app.py                     # Main API (Flask)
├── parser/                   # Resume parsing logic
├── section_detector/         # Section detection module
├── scoring/                  # ML scoring system
├── nlp_features/             # NLP-based features
├── utils/                    # Preprocessing utilities
├── ml_model/                 # Trained ML model
├── github_integration/       # GitHub API logic
└── evaluation/               # Metrics (precision/recall)
```

---

## 🧪 Technologies Used

* Python 🐍
* Flask 🌐
* spaCy (NLP)
* Sentence-BERT (Semantic Similarity)
* Scikit-learn (ML Model)
* Pandas (Data Handling)
* GitHub API

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/krishnapatel-dev/AI-Resume-Intelligence-System.git
cd AI-Resume-Intelligence-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download NLP Model

```bash
python -m spacy download en_core_web_sm
```

### 4️⃣ Run Application

```bash
python app.py
```

---

## 📥 API Usage

### Endpoint:

```
POST /analyze
```

### Input:

* Resume (PDF/Text)
* Job Description (Text)

### Output:

```json
{
  "score": 60.93,
  "experience_years": 0.67,
  "skills": {...},
  "sections": {...},
  "keyword_analysis": {...},
  "github": {...},
  "feedback": [...]
}
```

---

## 🧠 How It Works

1. Resume is parsed and structured into sections
2. NLP preprocessing is applied
3. Skills and keywords are extracted
4. Semantic similarity is computed
5. Experience is calculated
6. ML model predicts final score
7. Feedback and insights are generated

---

## 📊 Evaluation Metrics (Optional)

* Precision
* Recall
* F1-score

Used to validate skill extraction and keyword matching accuracy.

---

## ⚠️ Limitations

* Model trained on small dataset (can be improved)
* Section detection is rule-based (semi-flexible)
* Skill extraction is hybrid (not fully semantic)

---

## 🔮 Future Improvements

* Use Transformer-based models for scoring
* Improve skill extraction using embeddings
* Add LinkedIn profile integration
* Build frontend UI (Streamlit / React)
* Deploy as SaaS platform

---

## 💼 Use Cases

* Resume screening automation
* Candidate ranking system
* ATS enhancement tools
* Career guidance platforms

---

## 🙌 Acknowledgment

Inspired by basic resume parsing systems, enhanced with AI, NLP, and ML techniques to create a more intelligent evaluation system.

---

## 📌 Author

**Krishna Patel**

* GitHub: https://github.com/krishnapatel-dev
* LinkedIn: https://www.linkedin.com/in/krishna-patel-7b0058280

---

⭐ If you found this project useful, consider giving it a star!

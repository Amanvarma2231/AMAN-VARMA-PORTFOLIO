import re
import math
from typing import List, Dict, Any

# Aman Varma Knowledge Base for AI RAG Assistant
AMAN_PROFILE = {
    "name": "Aman Varma",
    "role": "Python Backend, Generative AI & NLP Engineer",
    "location": "Ghaziabad, India",
    "email": "amangurauli@gmail.com",
    "mobile": "+91-6306572504",
    "github": "https://github.com/Amanvarma2231",
    "linkedin": "https://www.linkedin.com/in/aman-v-697771345",
    "education": {
        "degree": "B.Tech, Computer Science & Engineering",
        "institution": "NITRA Technical Campus, AKTU",
        "location": "Ghaziabad, UP, India",
        "cgpa": "7.12 / 10",
        "duration": "May 2022 – June 2026"
    },
    "experience": [
        {
            "role": "Python Developer Intern",
            "company": "Druidot Consulting (OPC) Pvt. Ltd.",
            "period": "Feb 2026 – Present (Remote)",
            "highlights": [
                "Developed Python-based AI and backend applications using Flask and FastAPI, integrating RESTful APIs and data-processing workflows.",
                "Worked on NLP-based text processing and analysis for AI-oriented application workflows.",
                "Integrated Generative AI and LLM-based capabilities through AI API integrations and prompt-driven workflows.",
                "Built and optimized REST APIs, backend services, automation, testing, and debugging.",
                "Performed data validation and processing with MySQL and MongoDB, supporting reliable AI and backend workflows."
            ]
        }
    ],
    "projects": [
        {
            "name": "NLPCRM – AI-Powered CRM Platform",
            "repo": "https://github.com/Amanvarma2231/NLPCRM",
            "live": "https://nlpcrm-1.onrender.com/",
            "tech": ["Python", "FastAPI", "Flask", "MySQL", "SQLite", "REST APIs", "JWT"],
            "highlights": [
                "Designed and developed 25+ RESTful API endpoints across contacts, NLP, email, and webhook modules.",
                "Implemented MySQL & SQLite database persistence, JWT access control, rate limiting, and input validation.",
                "Integrated NLP workflows for customer interaction analysis and automated email classification."
            ]
        },
        {
            "name": "ContentDesk – AI Content & Data Processing Platform",
            "repo": "https://github.com/Amanvarma2231/Content-_Desk",
            "live": "https://content-desk.onrender.com/",
            "tech": ["Python", "Flask", "SQLite", "REST APIs", "GitHub Actions", "TF-IDF"],
            "highlights": [
                "Engineered a shared Python/Flask backend serving web and desktop channels.",
                "Developed SEO-scoring crawler and TF-IDF near-duplicate detection workflow.",
                "Implemented 26 automated unit tests in GitHub Actions CI."
            ]
        },
        {
            "name": "TrainIQ – AI Model Training & Analytics Platform",
            "repo": "https://github.com/Amanvarma2231/TrainIQ",
            "live": "https://trainiq-x94b.onrender.com",
            "tech": ["Python", "Machine Learning", "REST APIs", "Analytics", "Render"],
            "highlights": [
                "Architected automated AI training pipeline tracking metric evaluations.",
                "Integrated model deployment monitoring with REST API endpoints."
            ]
        },
        {
            "name": "Enterprise Data Warehouse",
            "repo": "https://github.com/Amanvarma2231/Enterprise-Data_Warehouse",
            "live": "https://enterprise-datawarehouse-amhwlzks6yuybmcbxtls2v.streamlit.app/",
            "tech": ["Python", "Streamlit", "SQL", "Data Warehousing", "ETL"],
            "highlights": [
                "Developed interactive Streamlit data warehouse dashboard with ETL query engine.",
                "Optimized SQL query performance and data visualizations."
            ]
        },
        {
            "name": "Skill Development Platform",
            "repo": "https://github.com/Amanvarma2231/skill-development",
            "live": "https://skill-development-eosin.vercel.app/",
            "tech": ["JavaScript", "Full-Stack", "React / Next.js", "Vercel"],
            "highlights": [
                "Engineered skill assessment and tracking platform for interactive learning.",
                "Deployed on Vercel with responsive micro-learning modules."
            ]
        },
        {
            "name": "Voice Sentiment Analysis",
            "repo": "https://github.com/Amanvarma2231/Voice-Sentiment12",
            "live": "https://voice-sentiment12.vercel.app/",
            "tech": ["Python", "Speech AI", "Audio NLP", "Sentiment Analysis"],
            "highlights": [
                "Built voice emotion & sentiment classification model processing speech audio.",
                "Integrated real-time audio analytics and Vercel cloud deployment."
            ]
        }
    ],

    "skills": {
        "Languages": ["Python", "Java", "JavaScript", "C++", "SQL", "HTML5"],
        "AI & ML": ["Artificial Intelligence", "Machine Learning", "NLP", "Generative AI", "Prompt Engineering", "LLMs"],
        "Backend": ["FastAPI", "Flask", "Django", "RESTful APIs", "Web Services"],
        "API & Auth": ["REST API Design", "OpenAPI", "JWT", "HTTP", "Webhooks", "Rate Limiting"],
        "Databases": ["MySQL", "MongoDB", "SQLite", "CRUD Operations"],
        "DevOps & Tools": ["Git", "GitHub", "Docker", "CI/CD", "GitHub Actions", "Manual Testing", "Debugging"]
    },
    "publications": [
        "Presented 'Adaptive Residual-Energy Threshold LEACH for Performance & Energy Efficiency' at NGAISL-2026, HRIT University (Apr 2026)."
    ],
    "certifications": [
        "Python Programming Certification – Infosys Springboard",
        "Quantitative Research Job Simulation – JPMorgan"
    ]
}

def analyze_text_nlp(text: str) -> Dict[str, Any]:
    """
    Performs comprehensive NLP analysis on input text:
    - Sentiment score & classification
    - TF-IDF simulated keyword extraction
    - SEO & Readability score calculation (inspired by ContentDesk project)
    - Named Entity extraction (Tech, Metrics, Numbers, Email)
    - Structural statistics
    """
    if not text or not text.strip():
        return {"error": "Input text cannot be empty."}

    text_clean = text.strip()
    words = re.findall(r'\b\w+\b', text_clean)
    sentences = [s.strip() for s in re.split(r'[.!?]+', text_clean) if s.strip()]
    
    word_count = len(words)
    sentence_count = max(len(sentences), 1)
    char_count = len(text_clean)
    avg_word_len = round(sum(len(w) for w in words) / max(word_count, 1), 2)
    avg_sentence_len = round(word_count / sentence_count, 2)

    # Simple Lexicon Sentiment Analysis
    positive_words = {"great", "excellent", "amazing", "good", "fast", "optimized", "powerful", "best", "efficient", "innovative", "scalable", "successful", "robust", "high", "clean", "reliable", "smart", "advanced", "proactive"}
    negative_words = {"bad", "slow", "error", "bug", "failing", "poor", "broken", "issue", "difficult", "heavy", "delay", "vulnerable", "crash", "flaw"}

    words_lower = [w.lower() for w in words]
    pos_score = sum(1 for w in words_lower if w in positive_words)
    neg_score = sum(1 for w in words_lower if w in negative_words)
    
    total_sentiment_words = pos_score + neg_score
    if total_sentiment_words > 0:
        sentiment_ratio = (pos_score - neg_score) / (pos_score + neg_score)
    else:
        sentiment_ratio = 0.0

    if sentiment_ratio > 0.2:
        sentiment_label = "Positive"
        sentiment_color = "#10b981"
    elif sentiment_ratio < -0.2:
        sentiment_label = "Negative"
        sentiment_color = "#ef4444"
    else:
        sentiment_label = "Neutral"
        sentiment_color = "#3b82f6"

    # Simulated TF-IDF Keyword Extraction
    stopwords = {"the", "a", "an", "and", "or", "but", "is", "are", "was", "were", "to", "in", "on", "at", "for", "with", "by", "of", "it", "this", "that", "from", "as", "be", "has", "have", "had", "not", "can", "will", "should", "our", "my", "you", "we"}
    filtered_words = [w for w in words_lower if w not in stopwords and len(w) > 2]
    
    word_freq = {}
    for w in filtered_words:
        word_freq[w] = word_freq.get(w, 0) + 1
        
    # Calculate simulated TF-IDF weight = TF * log(100 / (freq + 1))
    tf_idf_keywords = []
    for w, count in word_freq.items():
        tf = count / max(len(filtered_words), 1)
        idf = math.log(10.0 / (count + 1)) + 1.0
        score = round(tf * idf * 10, 3)
        tf_idf_keywords.append({"keyword": w, "count": count, "score": score})

    tf_idf_keywords.sort(key=lambda x: x["score"], reverse=True)
    top_keywords = tf_idf_keywords[:8]

    # SEO Content & Readability Score (ContentDesk algorithm)
    # Flesch-Kincaid Reading Ease approximation
    syllable_count = sum(max(1, len(re.findall(r'[aeiouy]+', w.lower()))) for w in words)
    flesch_score = 206.835 - (1.015 * avg_sentence_len) - (84.6 * (syllable_count / max(word_count, 1)))
    flesch_score = max(0, min(100, round(flesch_score, 1)))

    seo_score = min(100, round(
        (min(word_count / 300, 1.0) * 40) + 
        (min(len(top_keywords) / 6, 1.0) * 30) + 
        (flesch_score * 0.3)
    , 1))

    # Entity Extraction (Tech Stack, Email, Metrics)
    tech_terms = {"python", "fastapi", "flask", "django", "mysql", "mongodb", "sqlite", "docker", "git", "nlp", "llm", "generative ai", "jwt", "rest", "api", "aws", "ci/cd"}
    found_entities = []
    
    for w in words_lower:
        if w in tech_terms:
            found_entities.append({"type": "TECHNOLOGY", "entity": w.upper()})
            
    # Email entity
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    for email in emails:
        found_entities.append({"type": "EMAIL", "entity": email})
        
    # Numbers/Metrics entity
    metrics = re.findall(r'\b\d+(?:\.\d+)?%?\b', text)
    for m in metrics[:5]:
        found_entities.append({"type": "NUMERIC_METRIC", "entity": m})

    # Deduplicate entities
    unique_entities = []
    seen = set()
    for e in found_entities:
        key = (e["type"], e["entity"])
        if key not in seen:
            seen.add(key)
            unique_entities.append(e)

    return {
        "stats": {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "char_count": char_count,
            "avg_word_length": avg_word_len,
            "avg_sentence_length": avg_sentence_len
        },
        "sentiment": {
            "label": sentiment_label,
            "score": round(sentiment_ratio, 2),
            "pos_words": pos_score,
            "neg_words": neg_score,
            "color": sentiment_color
        },
        "keywords": top_keywords,
        "seo_analysis": {
            "seo_score": seo_score,
            "readability_score": flesch_score,
            "grade_level": "Professional Technical" if flesch_score < 50 else ("Standard Reader" if flesch_score < 70 else "Easy Read")
        },
        "entities": unique_entities[:10]
    }

def generate_prompt_response(prompt: str, system_prompt: str = "", temperature: float = 0.7, mode: str = "assistant") -> Dict[str, Any]:
    """
    Simulates Generative AI & Prompt Engineering Studio output with custom temperature and personas.
    """
    if not prompt or not prompt.strip():
        return {"error": "Prompt cannot be empty."}

    p = prompt.strip().lower()
    
    # Custom response generation logic mimicking LLM completion
    if "python" in p or "fastapi" in p or "backend" in p:
        response_text = (
            "### Python FastAPI & AI Backend Architecture\n\n"
            "FastAPI is selected for high-concurrency asynchronous workloads. Key components of this architecture:\n"
            "1. **Asynchronous Execution (`async def`)**: Non-blocking I/O for database and AI model API calls.\n"
            "2. **Pydantic Data Schemas**: Strict request/response validation and automatic OpenAPI documentation.\n"
            "3. **Dependency Injection**: Reusable database sessions (`SQLAlchemy`/`Motor` for MongoDB) and authentication middleware (`JWT`).\n"
            "4. **AI Pipeline Integration**: Asynchronous dispatch of NLP classification and LLM prompt generation."
        )
    elif "nlp" in p or "sentiment" in p or "tf-idf" in p:
        response_text = (
            "### NLP Workflow & Text Processing Pipeline\n\n"
            "The NLP pipeline processes unstructured text in 4 optimized stages:\n"
            "1. **Tokenization & Normalization**: Regex-based token extraction, case standardization, and stop-word removal.\n"
            "2. **TF-IDF Vectorization**: Calculating term frequencies scaled by inverse document frequencies to weight unique domain keywords.\n"
            "3. **Lexicon & Semantic Scoring**: Evaluating sentiment polarity and readability metrics.\n"
            "4. **Structured JSON Output**: Returning normalized data ready for API consumption."
        )
    elif "llm" in p or "rag" in p or "generative" in p:
        response_text = (
            "### Retrieval-Augmented Generation (RAG) & Prompt Engineering\n\n"
            "To ground Generative AI models and prevent hallucinations:\n"
            "1. **Vector Embedding Search**: Document chunks indexed into vector stores.\n"
            "2. **Contextual Prompt Injection**: Injecting retrieved top-k facts into system instructions.\n"
            "3. **Hyperparameter Tuning**: Setting `temperature=" + str(temperature) + "` to balance creativity and factual precision.\n"
            "4. **Output Schema Enforcement**: Ensuring responses match structured JSON specs for seamless backend integration."
        )
    else:
        response_text = (
            f"### Generative AI Studio Response\n\n"
            f"**Mode**: `{mode}` | **Temperature**: `{temperature}`\n\n"
            f"Received prompt: *\"{prompt.strip()}\"*\n\n"
            f"**AI Analysis**: The prompt asks about scalable software engineering and AI system design. "
            f"Aman Varma's stack leverages Python, FastAPI, Flask, GenAI API integrations, and database persistence to build robust end-to-end applications."
        )

    tokens_used = len(prompt.split()) + len(response_text.split()) + 35
    
    return {
        "status": "success",
        "model": "Aman-GenAI-Engine-v1.0",
        "params": {
            "system_prompt": system_prompt or "You are an expert Python Backend & AI Engineer Assistant.",
            "temperature": temperature,
            "mode": mode
        },
        "response": response_text,
        "token_metrics": {
            "prompt_tokens": len(prompt.split()),
            "completion_tokens": len(response_text.split()),
            "total_tokens": tokens_used,
            "estimated_latency_ms": round(120 + (temperature * 80), 2)
        }
    }

def chat_with_aman_ai(user_query: str) -> str:
    """
    RAG Chatbot Assistant answering queries about Aman Varma's background, skills, experience, and projects.
    """
    q = user_query.lower().strip()
    
    if any(k in q for k in ["who is", "who are you", "tell me about aman", "about", "bio", "summary"]):
        return (
            "👋 **Hello! I'm Aman Varma's AI Assistant.**\n\n"
            "Aman Varma is a **Python Backend, Generative AI & NLP Engineer** (B.Tech CSE from NITRA Technical Campus, AKTU).\n\n"
            "• **Current Role**: Python Developer Intern at Druidot Consulting (Feb 2026 – Present).\n"
            "• **Core Expertise**: Python (FastAPI, Flask), REST APIs, Generative AI, NLP, LLM prompt engineering, MySQL, MongoDB, Docker, CI/CD.\n"
            "• **Featured Projects**: `NLPCRM` (25+ API endpoints AI CRM) & `ContentDesk` (AI Content & SEO Platform).\n\n"
            "How can I help you learn more about Aman's work or schedule an interview?"
        )
    
    if any(k in q for k in ["experience", "work", "job", "intern", "druidot"]):
        return (
            "💼 **Aman Varma's Experience**:\n\n"
            "**Python Developer Intern** @ *Druidot Consulting (OPC) Pvt. Ltd.* (Feb 2026 – Present, Remote)\n\n"
            "• Built Python AI & backend applications using **Flask** & **FastAPI** with RESTful API integration.\n"
            "• Developed **NLP text processing** and Generative AI/LLM prompt-driven application workflows.\n"
            "• Designed and optimized REST APIs, automated testing, data validation, and database operations with **MySQL** and **MongoDB**."
        )

    if any(k in q for k in ["project", "nlpcrm", "contentdesk", "trainiq", "warehouse", "skill", "voice", "apps", "build"]):
        return (
            "🚀 **Aman Varma's Live Deployed Projects**:\n\n"
            "1. **NLPCRM (AI-Powered CRM Platform)**:\n"
            "   - Live App: [nlpcrm-1.onrender.com](https://nlpcrm-1.onrender.com/)\n"
            "   - Source Code: [GitHub NLPCRM](https://github.com/Amanvarma2231/NLPCRM)\n"
            "   - Features: 25+ RESTful endpoints, JWT auth, rate limiting, NLP email intent classification.\n\n"
            "2. **ContentDesk (AI Content & SEO Platform)**:\n"
            "   - Live App: [content-desk.onrender.com](https://content-desk.onrender.com/)\n"
            "   - Source Code: [GitHub ContentDesk](https://github.com/Amanvarma2231/Content-_Desk)\n"
            "   - Features: Shared Flask backend, TF-IDF near-duplicate detection, 26 unit tests in GitHub Actions CI.\n\n"
            "3. **TrainIQ (AI Model Training Platform)**:\n"
            "   - Live App: [trainiq-x94b.onrender.com](https://trainiq-x94b.onrender.com)\n"
            "   - Source Code: [GitHub TrainIQ](https://github.com/Amanvarma2231/TrainIQ)\n\n"
            "4. **Enterprise Data Warehouse**:\n"
            "   - Live App: [Streamlit Enterprise Warehouse](https://enterprise-datawarehouse-amhwlzks6yuybmcbxtls2v.streamlit.app/)\n"
            "   - Source Code: [GitHub Data Warehouse](https://github.com/Amanvarma2231/Enterprise-Data_Warehouse)\n\n"
            "5. **Skill Development Platform**:\n"
            "   - Live App: [skill-development-eosin.vercel.app](https://skill-development-eosin.vercel.app/)\n"
            "   - Source Code: [GitHub Skill Development](https://github.com/Amanvarma2231/skill-development)\n\n"
            "6. **Voice Sentiment Analysis**:\n"
            "   - Live App: [voice-sentiment12.vercel.app](https://voice-sentiment12.vercel.app/)\n"
            "   - Source Code: [GitHub Voice Sentiment](https://github.com/Amanvarma2231/Voice-Sentiment12)"
        )

    if any(k in q for k in ["skill", "stack", "technology", "python", "fastapi", "ai", "llm", "nlp"]):
        return (
            "🛠️ **Aman Varma's Technical Skills**:\n\n"
            "• **Languages**: Python, Java, JavaScript, C++, SQL, HTML5\n"
            "• **AI / ML / NLP**: Generative AI, LLMs, Prompt Engineering, NLP, TF-IDF, Sentiment Analysis, Speech AI\n"
            "• **Backend**: FastAPI, Flask, Django, RESTful APIs, Web Services, Microservices\n"
            "• **API & Auth**: JWT, OpenAPI / Swagger, Webhooks, Rate Limiting, HTTP\n"
            "• **Databases**: MySQL, MongoDB, SQLite, Redis, Data Warehousing\n"
            "• **DevOps & Tools**: Git, GitHub, Docker, CI/CD (GitHub Actions), Vercel, Render, Streamlit"
        )

    if any(k in q for k in ["contact", "email", "phone", "hire", "reach", "linkedin", "github"]):
        return (
            "📬 **Contact Aman Varma**:\n\n"
            "• 📧 **Email**: [amangurauli@gmail.com](mailto:amangurauli@gmail.com)\n"
            "• 📱 **Phone**: +91-6306572504\n"
            "• 📍 **Location**: Ghaziabad, UP, India\n"
            "• 💼 **LinkedIn**: [linkedin.com/in/aman-v-697771345](https://www.linkedin.com/in/aman-v-697771345)\n"
            "• 🐙 **GitHub**: [github.com/Amanvarma2231](https://github.com/Amanvarma2231)\n\n"
            "Feel free to submit a message in the contact form below!"
        )


    if any(k in q for k in ["education", "college", "degree", "aktu", "nitra", "cgpa"]):
        return (
            "🎓 **Education & Academics**:\n\n"
            "**B.Tech in Computer Science & Engineering**\n"
            "• Institution: NITRA Technical Campus, AKTU (Ghaziabad, UP, India)\n"
            "• CGPA: **7.12 / 10** (2022 – 2026)\n"
            "• Publication: Presented research paper *'Adaptive Residual-Energy Threshold LEACH for Performance & Energy Efficiency'* at NGAISL-2026 (HRIT University)."
        )

    return (
        f"🤖 Thank you for asking about: *\"{user_query}\"*\n\n"
        f"Aman Varma is a Python Backend & AI Engineer specialized in **FastAPI, Flask, Generative AI, NLP, and database workflows**.\n\n"
        f"You can explore his live **NLP Tool**, **GenAI Studio**, and **REST API Tester** on this portfolio, or contact him at **amangurauli@gmail.com**!"
    )

/* ==========================================================================
   Aman Varma Portfolio - Modern React 18 Application
   Stateful React Components for AI Studio, API Sandbox, Projects & Contact
   ========================================================================== */

const { useState, useEffect, useRef } = React;

// 1. Navigation Bar Component
function Navbar({ activeSection, backendStatus }) {
    const [mobileOpen, setMobileOpen] = useState(false);

    return (
        <header className="navbar" id="navbar">
            <div className="container nav-container">
                <a href="#hero" className="nav-logo">
                    <img src="/static/images/logo.jpg" alt="Aman Varma Logo" className="brand-logo-img" />
                    <span className="logo-code">&lt;</span>Aman Varma<span className="logo-code"> /&gt;</span>
                    <span className="badge-role"><i class="fa-brands fa-react text-cyan"></i> React & FastAPI</span>
                </a>

                <nav className={`nav-menu ${mobileOpen ? 'mobile-open' : ''}`}>
                    <a href="#about" className={`nav-link ${activeSection === 'about' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}>About</a>
                    <a href="#skills" className={`nav-link ${activeSection === 'skills' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}>Skills</a>
                    <a href="#experience" className={`nav-link ${activeSection === 'experience' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}>Experience</a>
                    <a href="#projects" className={`nav-link ${activeSection === 'projects' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}>Projects</a>
                    <a href="#ai-studio" className={`nav-link highlight-link ${activeSection === 'ai-studio' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}><i className="fa-solid fa-wand-magic-sparkles"></i> AI Studio</a>
                    <a href="#api-sandbox" className={`nav-link highlight-link ${activeSection === 'api-sandbox' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}><i className="fa-solid fa-server"></i> API Sandbox</a>
                    <a href="#certifications" className={`nav-link ${activeSection === 'certifications' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}>Certifications</a>
                    <a href="#contact" className={`nav-link ${activeSection === 'contact' ? 'active' : ''}`} onClick={() => setMobileOpen(false)}>Contact</a>
                </nav>

                <div className="nav-actions">
                    <div className="status-pill" title="FastAPI Backend Health">
                        <span className="status-dot"></span>
                        <span className="status-text">{backendStatus}</span>
                    </div>
                    <a href="/api/download-resume" download className="btn btn-secondary btn-sm"><i className="fa-solid fa-download"></i> Resume</a>
                    <a href="#contact" className="btn btn-primary btn-sm"><i className="fa-regular fa-paper-plane"></i> Hire Me</a>
                </div>

                <button className="nav-toggle" onClick={() => setMobileOpen(!mobileOpen)} aria-label="Toggle Navigation">
                    <i className={`fa-solid ${mobileOpen ? 'fa-xmark' : 'fa-bars'}`}></i>
                </button>
            </div>
        </header>
    );
}

// 2. React AI Studio Component
function ReactAIStudio() {
    const [activeTab, setActiveTab] = useState('nlp');

    // NLP Tool State
    const [nlpText, setNlpText] = useState("FastAPI combined with Generative AI and NLP workflows delivers exceptional microservices. Aman Varma engineered 25+ RESTful endpoints at Druidot Consulting to streamline AI data pipelines.");
    const [nlpLoading, setNlpLoading] = useState(false);
    const [nlpResult, setNlpResult] = useState(null);

    // GenAI Studio State
    const [systemPersona, setSystemPersona] = useState("You are a Senior Python Backend Architect specializing in FastAPI and LLM systems.");
    const [temperature, setTemperature] = useState(0.7);
    const [promptText, setPromptText] = useState("Explain how FastAPI handles async requests and integrates with Generative AI prompt pipelines.");
    const [genAiLoading, setGenAiLoading] = useState(false);
    const [genAiResponse, setGenAiResponse] = useState(null);

    // Chatbot State
    const [chatInput, setChatInput] = useState("");
    const [messages, setMessages] = useState([
        { sender: 'bot', text: "👋 Hi! I'm Aman Varma's React AI Assistant. Ask me anything about Aman's experience at Druidot Consulting, B.Tech CSE degree, Python/FastAPI skills, or NLPCRM & ContentDesk projects!" }
    ]);
    const [chatLoading, setChatLoading] = useState(false);
    const chatEndRef = useRef(null);

    useEffect(() => {
        if (chatEndRef.current) {
            chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [messages, chatLoading]);

    // NLP Run Handler
    const handleRunNLP = async () => {
        if (!nlpText.trim()) return;
        setNlpLoading(true);
        try {
            const res = await fetch('/api/ai/nlp-analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: nlpText })
            });
            if (res.ok) {
                const data = await res.json();
                setNlpResult(data);
            }
        } catch (err) {
            setNlpResult({
                stats: { word_count: nlpText.split(/\s+/).length, sentence_count: 2, char_count: nlpText.length },
                sentiment: { label: 'Positive', score: 0.85, color: '#10b981' },
                keywords: [{ keyword: 'fastapi', count: 2 }, { keyword: 'python', count: 2 }],
                seo_analysis: { seo_score: 92, readability_score: 76 },
                entities: [{ type: 'TECHNOLOGY', entity: 'FASTAPI' }]
            });
        } finally {
            setNlpLoading(false);
        }
    };

    // GenAI Run Handler
    const handleRunGenAI = async () => {
        if (!promptText.trim()) return;
        setGenAiLoading(true);
        try {
            const res = await fetch('/api/ai/genai-prompt', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: promptText, system_prompt: systemPersona, temperature: parseFloat(temperature), mode: 'assistant' })
            });
            if (res.ok) {
                const data = await res.json();
                setGenAiResponse(data);
            }
        } catch (err) {
            setGenAiResponse({
                response: "### Python FastAPI & AI Architecture\n\nFastAPI handles asynchronous requests (`async def`) for high throughput AI pipelines.",
                token_metrics: { total_tokens: 142, estimated_latency_ms: 68 }
            });
        } finally {
            setGenAiLoading(false);
        }
    };

    // Chat Handler
    const handleSendChat = async (queryText) => {
        const text = queryText || chatInput;
        if (!text.trim()) return;

        const newMsgs = [...messages, { sender: 'user', text }];
        setMessages(newMsgs);
        setChatInput("");
        setChatLoading(true);

        try {
            const res = await fetch('/api/ai/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });
            if (res.ok) {
                const data = await res.json();
                setMessages([...newMsgs, { sender: 'bot', text: data.reply }]);
            }
        } catch (err) {
            setMessages([...newMsgs, { sender: 'bot', text: "👋 **Aman Varma** is a Python Backend & AI Engineer! Contact him at **amangurauli@gmail.com**." }]);
        } finally {
            setChatLoading(false);
        }
    };

    return (
        <section className="section ai-studio-section" id="ai-studio">
            <div class="container">
                <div className="section-header">
                    <span className="section-subtitle">REACT POWERED INTERACTIVE DEMO</span>
                    <h2 className="section-title"><i className="fa-brands fa-react text-cyan"></i> React AI & NLP Studio</h2>
                    <p className="section-desc">Stateful React components communicating in real-time with Python FastAPI backend.</p>
                    <div className="title-bar"></div>
                </div>

                <div className="studio-tabs">
                    <button className={`tab-btn ${activeTab === 'nlp' ? 'active' : ''}`} onClick={() => setActiveTab('nlp')}>
                        <i className="fa-solid fa-align-left"></i> Live NLP Analyzer
                    </button>
                    <button className={`tab-btn ${activeTab === 'genai' ? 'active' : ''}`} onClick={() => setActiveTab('genai')}>
                        <i className="fa-solid fa-sliders"></i> GenAI Prompt Studio
                    </button>
                    <button className={`tab-btn ${activeTab === 'rag' ? 'active' : ''}`} onClick={() => setActiveTab('rag')}>
                        <i className="fa-solid fa-comments"></i> Aman AI Assistant (RAG)
                    </button>
                </div>

                <div className="glass-card studio-container">
                    {/* Tab 1: NLP Analyzer */}
                    {activeTab === 'nlp' && (
                        <div className="nlp-grid">
                            <div className="nlp-input-col">
                                <label className="input-label"><i className="fa-solid fa-pen-to-square"></i> Input Text:</label>
                                <textarea className="form-control" rows="6" value={nlpText} onChange={(e) => setNlpText(e.target.value)}></textarea>
                                <div className="preset-buttons">
                                    <span className="preset-label">Presets:</span>
                                    <button className="btn-preset" onClick={() => setNlpText("FastAPI combined with Generative AI and NLP workflows delivers exceptional microservices. Aman Varma engineered 25+ RESTful endpoints at Druidot Consulting.")}>Tech Article</button>
                                    <button className="btn-preset" onClick={() => setNlpText("Great experience working with the AI CRM platform! The NLP intent classification and REST API response times are remarkably fast.")}>Feedback</button>
                                    <button className="btn-preset" onClick={() => setNlpText("")}>Clear</button>
                                </div>
                                <button className="btn btn-primary btn-block mt-3" onClick={handleRunNLP} disabled={nlpLoading}>
                                    {nlpLoading ? <><i className="fa-solid fa-spinner fa-spin"></i> Analyzing...</> : <><i className="fa-solid fa-play"></i> Run React NLP Analysis</>}
                                </button>
                            </div>

                            <div className="nlp-output-col">
                                <div className="output-box">
                                    {nlpResult ? (
                                        <div>
                                            <div className="result-header-badge">
                                                <span className="sentiment-pill" style={{ background: `${nlpResult.sentiment.color}20`, color: nlpResult.sentiment.color, border: `1px solid ${nlpResult.sentiment.color}50` }}>
                                                    Sentiment: {nlpResult.sentiment.label} ({nlpResult.sentiment.score})
                                                </span>
                                                <span className="badge badge-info">SEO Score: {nlpResult.seo_analysis.seo_score} / 100</span>
                                            </div>

                                            <div className="metrics-mini-grid">
                                                <div className="mini-card"><div className="mini-val">{nlpResult.stats.word_count}</div><div className="mini-lbl">Words</div></div>
                                                <div className="mini-card"><div className="mini-val">{nlpResult.stats.sentence_count}</div><div className="mini-lbl">Sentences</div></div>
                                                <div className="mini-card"><div className="mini-val">{nlpResult.seo_analysis.readability_score}</div><div className="mini-lbl">Readability</div></div>
                                            </div>

                                            <div className="mt-3">
                                                <div className="input-label" style={{fontSize:'0.75rem'}}><i className="fa-solid fa-tags"></i> Top TF-IDF Keywords:</div>
                                                <div className="keyword-tags">
                                                    {nlpResult.keywords.map((k, i) => <span key={i} className="kw-tag">{k.keyword} ({k.count || 1})</span>)}
                                                </div>
                                            </div>
                                        </div>
                                    ) : (
                                        <div className="empty-state">
                                            <i className="fa-solid fa-chart-pie"></i>
                                            <p>Click "Run React NLP Analysis" to see live stateful results!</p>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Tab 2: GenAI Studio */}
                    {activeTab === 'genai' && (
                        <div className="genai-grid">
                            <div className="genai-controls">
                                <div className="form-group">
                                    <label className="input-label">System Persona:</label>
                                    <select className="form-control" value={systemPersona} onChange={(e) => setSystemPersona(e.target.value)}>
                                        <option value="You are a Senior Python Backend Architect specializing in FastAPI and LLM systems.">Python Backend Architect</option>
                                        <option value="You are an AI & NLP Data Engineer.">NLP & Data Specialist</option>
                                        <option value="You are a Technical Hiring Manager.">Technical Recruiter</option>
                                    </select>
                                </div>

                                <div className="form-group mt-3">
                                    <label className="input-label">Temperature: <span className="text-cyan font-bold">{temperature}</span></label>
                                    <input type="range" min="0.0" max="1.5" step="0.1" value={temperature} onChange={(e) => setTemperature(e.target.value)} className="range-slider" />
                                </div>

                                <div className="form-group mt-3">
                                    <label className="input-label">Prompt Input:</label>
                                    <textarea className="form-control" rows="4" value={promptText} onChange={(e) => setPromptText(e.target.value)}></textarea>
                                </div>

                                <button className="btn btn-primary btn-block mt-3" onClick={handleRunGenAI} disabled={genAiLoading}>
                                    {genAiLoading ? <><i className="fa-solid fa-spinner fa-spin"></i> Generating...</> : <><i className="fa-solid fa-sparkles"></i> Generate React Response</>}
                                </button>
                            </div>

                            <div className="genai-output">
                                <div className="code-preview genai-preview">
                                    <div className="code-header">
                                        <span className="code-title"><i className="fa-solid fa-microchip"></i> React State Output</span>
                                        <span className="token-badge">{genAiResponse ? `${genAiResponse.token_metrics.total_tokens} Tokens` : '0 Tokens'}</span>
                                    </div>
                                    <div className="genai-response-body">
                                        {genAiResponse ? genAiResponse.response : <p className="text-muted">Generated response will appear here...</p>}
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Tab 3: RAG Chatbot */}
                    {activeTab === 'rag' && (
                        <div className="chat-wrapper">
                            <div className="chat-header">
                                <div className="chat-avatar"><i className="fa-solid fa-robot"></i></div>
                                <div>
                                    <h4>Aman Varma React RAG Assistant</h4>
                                    <span className="status-online"><i className="fa-solid fa-circle"></i> Connected to FastAPI</span>
                                </div>
                            </div>

                            <div className="chat-messages">
                                {messages.map((msg, i) => (
                                    <div key={i} className={`chat-bubble ${msg.sender === 'user' ? 'user-bubble' : 'bot-bubble'}`}>
                                        {msg.text}
                                    </div>
                                ))}
                                {chatLoading && (
                                    <div className="chat-bubble bot-bubble">
                                        <i className="fa-solid fa-ellipsis fa-beat"></i> Thinking...
                                    </div>
                                )}
                                <div ref={chatEndRef} />
                            </div>

                            <div className="chat-chips">
                                <button className="chip-btn" onClick={() => handleSendChat("Tell me about Aman's background")}>Summary</button>
                                <button className="chip-btn" onClick={() => handleSendChat("What experience does Aman have at Druidot Consulting?")}>Experience</button>
                                <button className="chip-btn" onClick={() => handleSendChat("What live projects has Aman deployed?")}>Projects</button>
                                <button className="chip-btn" onClick={() => handleSendChat("What is Aman's tech stack?")}>Skills</button>
                            </div>

                            <div className="chat-input-bar">
                                <input type="text" className="chat-input" placeholder="Type a message..." value={chatInput} onChange={(e) => setChatInput(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleSendChat()} />
                                <button className="btn btn-primary" onClick={() => handleSendChat()}><i className="fa-solid fa-paper-plane"></i></button>
                            </div>
                        </div>
                    )}

                </div>
            </div>
        </section>
    );
}

// 3. React REST API Sandbox Component
function ReactAPISandbox() {
    const endpoints = [
        { id: "get_contacts", method: "GET", path: "/api/v1/contacts", desc: "List all CRM contacts" },
        { id: "post_contact", method: "POST", path: "/api/v1/contacts", desc: "Create new CRM contact" },
        { id: "post_nlp_classify", method: "POST", path: "/api/v1/nlp/classify-intent", desc: "NLP intent classification" },
        { id: "post_auth_login", method: "POST", path: "/api/v1/auth/login", desc: "JWT token authentication" },
        { id: "get_analytics", method: "GET", path: "/api/v1/analytics/overview", desc: "CRM analytics overview" }
    ];

    const [selectedId, setSelectedId] = useState("get_contacts");
    const [payloadText, setPayloadText] = useState("");
    const [executing, setExecuting] = useState(false);
    const [responseOutput, setResponseOutput] = useState("Click 'Execute React Request' to test...");
    const [statusBadge, setStatusBadge] = useState("200 OK");
    const [latency, setLatency] = useState("-- ms");

    const currentEp = endpoints.find(e => e.id === selectedId) || endpoints[0];

    const handleExecute = async () => {
        setExecuting(true);
        const startTime = performance.now();

        try {
            const res = await fetch('/api/sandbox/execute', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ endpoint_id: selectedId })
            });
            if (res.ok) {
                const data = await res.json();
                const ms = data.execution_time_ms || Math.round(performance.now() - startTime);
                setStatusBadge(`${data.status_code || 200} OK`);
                setLatency(`${ms} ms`);
                setResponseOutput(JSON.stringify(data.response_data || data, null, 2));
            }
        } catch (err) {
            setResponseOutput(JSON.stringify({ status_code: 200, message: "Simulated response" }, null, 2));
        } finally {
            setExecuting(false);
        }
    };

    return (
        <section className="section api-sandbox-section" id="api-sandbox">
            <div className="container">
                <div className="section-header">
                    <span className="section-subtitle">REACT STATEFUL API TESTER</span>
                    <h2 className="section-title"><i className="fa-solid fa-server text-cyan"></i> Interactive REST API Sandbox</h2>
                    <p className="section-desc">Test live RESTful endpoints designed by Aman Varma for the NLPCRM project.</p>
                    <div className="title-bar"></div>
                </div>

                <div className="glass-card api-sandbox-card">
                    <div className="sandbox-controls">
                        <div className="control-row">
                            <div className="control-group flex-1">
                                <label className="input-label">Select Endpoint:</label>
                                <select className="form-control" value={selectedId} onChange={(e) => setSelectedId(e.target.value)}>
                                    {endpoints.map(ep => (
                                        <option key={ep.id} value={ep.id}>{ep.method} {ep.path} ({ep.desc})</option>
                                    ))}
                                </select>
                            </div>
                            <button className="btn btn-primary btn-send-request" onClick={handleExecute} disabled={executing}>
                                {executing ? <><i className="fa-solid fa-spinner fa-spin"></i> Executing...</> : <><i className="fa-solid fa-paper-plane"></i> Execute React Request</>}
                            </button>
                        </div>

                        <div className="endpoint-meta-bar">
                            <span className={`method-badge ${currentEp.method === 'GET' ? 'method-get' : 'method-post'}`}>{currentEp.method}</span>
                            <span className="path-display">{currentEp.path}</span>
                            <span className="endpoint-desc text-muted">{currentEp.desc}</span>
                        </div>
                    </div>

                    <div className="sandbox-panes">
                        <div className="pane request-pane">
                            <div className="pane-header">Request Payload (JSON)</div>
                            <textarea className="form-control code-font" rows="8" value={payloadText} onChange={(e) => setPayloadText(e.target.value)} placeholder="// No payload required for GET request"></textarea>
                        </div>

                        <div className="pane response-pane">
                            <div className="pane-header">
                                <span>React Response State</span>
                                <div className="response-status-group">
                                    <span className="badge badge-success">{statusBadge}</span>
                                    <span className="badge badge-info"><i className="fa-solid fa-stopwatch"></i> {latency}</span>
                                </div>
                            </div>
                            <pre className="code-preview-box"><code>{responseOutput}</code></pre>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}

// 4. Main App Container Mounting React Components
function MainApp() {
    const [backendStatus, setBackendStatus] = useState("FastAPI Connected");

    useEffect(() => {
        fetch('/api/health')
            .then(res => res.json())
            .then(data => setBackendStatus("FastAPI + React Active"))
            .catch(err => setBackendStatus("Live Client Mode"));
    }, []);

    return (
        <div>
            <ReactAIStudio />
            <ReactAPISandbox />
        </div>
    );
}

// Mount React Root
document.addEventListener('DOMContentLoaded', () => {
    const reactContainer = document.getElementById('react-root');
    if (reactContainer) {
        const root = ReactDOM.createRoot(reactContainer);
        root.render(<MainApp />);
    }
});

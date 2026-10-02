/* ==========================================================================
   Aman Varma Portfolio - REST API Sandbox Tester Logic
   Simulates NLPCRM RESTful API Endpoints
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    initAPISandbox();
});

const ENDPOINTS_DATA = {
    "get_contacts": {
        "method": "GET",
        "path": "/api/v1/contacts",
        "desc": "Retrieves paginated list of CRM contacts with optional search filter.",
        "sample_body": "",
        "response": {
            "status_code": 200,
            "total": 142,
            "page": 1,
            "limit": 10,
            "contacts": [
                {"id": "c-101", "name": "Rajesh Kumar", "email": "rajesh@techcorp.in", "company": "TechCorp", "status": "Lead", "score": 88},
                {"id": "c-102", "name": "Priya Sharma", "email": "priya@innovate.io", "company": "Innovate Labs", "status": "Active", "score": 95}
            ]
        }
    },
    "post_contact": {
        "method": "POST",
        "path": "/api/v1/contacts",
        "desc": "Creates a new CRM contact record with Pydantic input validation.",
        "sample_body": JSON.stringify({
            "name": "Aman Varma",
            "email": "amangurauli@gmail.com",
            "company": "Druidot Consulting",
            "phone": "+91-6306572504",
            "tags": ["Python", "FastAPI", "GenAI"]
        }, null, 2),
        "response": {
            "status_code": 201,
            "message": "Contact created successfully",
            "contact_id": "c-103",
            "created_at": "2026-10-01T21:30:00Z",
            "data": {
                "name": "Aman Varma",
                "email": "amangurauli@gmail.com",
                "company": "Druidot Consulting",
                "status": "New Lead"
            }
        }
    },
    "post_nlp_classify": {
        "method": "POST",
        "path": "/api/v1/nlp/classify-intent",
        "desc": "Analyzes raw email/message text and assigns lead intent, sentiment, and priority level.",
        "sample_body": JSON.stringify({
            "text": "We are looking for an experienced Python FastAPI and Generative AI developer to join our engineering team immediately.",
            "threshold": 0.75
        }, null, 2),
        "response": {
            "status_code": 200,
            "intent": "Hiring / Project Inquiry",
            "confidence_score": 0.96,
            "priority": "HIGH",
            "sentiment": "Positive",
            "extracted_skills": ["Python", "FastAPI", "Generative AI"],
            "suggested_action": "Route to Recruitment Lead"
        }
    },
    "post_auth_login": {
        "method": "POST",
        "path": "/api/v1/auth/login",
        "desc": "Authenticates user credentials and returns signed JWT access token with rate-limit protection.",
        "sample_body": JSON.stringify({
            "username": "aman.varma",
            "password": "••••••••••••"
        }, null, 2),
        "response": {
            "status_code": 200,
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWFuLnZhcm1hIiwiaWF0IjoxNzI3ODMwNDAwLCJleHAiOjE3Mjc5MTY4MDB9",
            "token_type": "bearer",
            "expires_in": 86400,
            "user": {"username": "aman.varma", "role": "Backend Admin"}
        }
    },
    "get_analytics": {
        "method": "GET",
        "path": "/api/v1/analytics/overview",
        "desc": "Aggregates CRM pipeline conversion metrics, NLP sentiment breakdown, and database response latency.",
        "sample_body": "",
        "response": {
            "status_code": 200,
            "active_leads": 1240,
            "nlp_classifications_today": 348,
            "avg_api_latency_ms": 14.2,
            "sentiment_breakdown": {
                "positive": "68%",
                "neutral": "24%",
                "negative": "8%"
            },
            "database_status": "MySQL & SQLite Persistence Healthy"
        }
    }
};

function initAPISandbox() {
    const selectEndpoint = document.getElementById('api-endpoint-select');
    const metaBox = document.getElementById('endpoint-meta');
    const reqBody = document.getElementById('api-request-body');
    const resBox = document.getElementById('api-response-body');
    const btnSend = document.getElementById('btn-send-api');
    const statusBadge = document.getElementById('res-status-badge');
    const latencyBadge = document.getElementById('res-latency');

    if (!selectEndpoint) return;

    const updateEndpointUI = (epKey) => {
        const ep = ENDPOINTS_DATA[epKey];
        if (!ep) return;

        const methodClass = ep.method === 'GET' ? 'method-get' : 'method-post';
        metaBox.innerHTML = `
            <span class="method-badge ${methodClass}">${ep.method}</span>
            <span class="path-display">${ep.path}</span>
            <span class="endpoint-desc text-muted">${ep.desc}</span>
        `;

        reqBody.value = ep.sample_body || "// No request payload required for GET endpoints.";
    };

    selectEndpoint.addEventListener('change', (e) => {
        updateEndpointUI(e.target.value);
    });

    // Initial load
    updateEndpointUI(selectEndpoint.value);

    btnSend.addEventListener('click', async () => {
        const epKey = selectEndpoint.value;
        const startTime = performance.now();

        btnSend.disabled = true;
        btnSend.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Executing...`;
        resBox.textContent = "Executing API request...";

        let userPayload = null;
        if (reqBody.value && reqBody.value.trim() && !reqBody.value.startsWith("//")) {
            try {
                userPayload = JSON.parse(reqBody.value);
            } catch (e) {
                // Ignore parse error
            }
        }

        try {
            const res = await fetch('/api/sandbox/execute', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ endpoint_id: epKey, payload: userPayload })
            });

            if (res.ok) {
                const data = await res.json();
                const latency = data.execution_time_ms || Math.round(performance.now() - startTime);
                
                statusBadge.textContent = `${data.status_code || 200} OK`;
                statusBadge.className = "badge badge-success";
                latencyBadge.innerHTML = `<i class="fa-solid fa-stopwatch"></i> ${latency} ms`;

                resBox.textContent = JSON.stringify(data.response_data || data, null, 2);
            } else {
                throw new Error('Endpoint execution error');
            }
        } catch (err) {
            // Local fallback
            const ep = ENDPOINTS_DATA[epKey];
            const latency = Math.round(performance.now() - startTime + 18);
            
            statusBadge.textContent = `${ep.response.status_code || 200} OK`;
            statusBadge.className = "badge badge-success";
            latencyBadge.innerHTML = `<i class="fa-solid fa-stopwatch"></i> ${latency} ms`;

            resBox.textContent = JSON.stringify(ep.response, null, 2);
        } finally {
            btnSend.disabled = false;
            btnSend.innerHTML = `<i class="fa-solid fa-paper-plane"></i> Send Request`;
        }
    });
}

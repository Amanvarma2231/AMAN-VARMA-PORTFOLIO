import time
from typing import Dict, Any

# Simulated NLPCRM Endpoint Specifications
NLPCRM_ENDPOINTS = [
    {
        "id": "get_contacts",
        "method": "GET",
        "path": "/api/v1/contacts",
        "title": "List All Contacts",
        "module": "Contacts",
        "description": "Retrieves paginated list of CRM contacts with optional search filter.",
        "sample_body": None,
        "sample_headers": {"Authorization": "Bearer eyJhbGciOiJIUzI1Ni..."},
        "simulated_response": {
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
    {
        "id": "post_contact",
        "method": "POST",
        "path": "/api/v1/contacts",
        "title": "Create Contact",
        "module": "Contacts",
        "description": "Creates a new CRM contact record with Pydantic input validation.",
        "sample_body": {
            "name": "Aman Varma",
            "email": "amangurauli@gmail.com",
            "company": "Druidot Consulting",
            "phone": "+91-6306572504",
            "tags": ["Python", "FastAPI", "GenAI"]
        },
        "sample_headers": {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJI..."},
        "simulated_response": {
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
    {
        "id": "post_nlp_classify",
        "method": "POST",
        "path": "/api/v1/nlp/classify-intent",
        "title": "Classify Email Intent (NLP)",
        "module": "NLP Engine",
        "description": "Analyzes raw email/message text and assigns lead intent, sentiment, and priority level.",
        "sample_body": {
            "text": "We are looking for an experienced Python FastAPI and Generative AI developer to join our engineering team immediately.",
            "threshold": 0.75
        },
        "sample_headers": {"Content-Type": "application/json"},
        "simulated_response": {
            "status_code": 200,
            "intent": "Hiring / Project Inquiry",
            "confidence_score": 0.96,
            "priority": "HIGH",
            "sentiment": "Positive",
            "extracted_skills": ["Python", "FastAPI", "Generative AI"],
            "suggested_action": "Route to Recruitment Lead"
        }
    },
    {
        "id": "post_auth_login",
        "method": "POST",
        "path": "/api/v1/auth/login",
        "title": "JWT Token Generation",
        "module": "Security",
        "description": "Authenticates user credentials and returns signed JWT access token with rate-limit protection.",
        "sample_body": {
            "username": "aman.varma",
            "password": "••••••••••••"
        },
        "sample_headers": {"Content-Type": "application/json"},
        "simulated_response": {
            "status_code": 200,
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWFuLnZhcm1hIiwiaWF0IjoxNzI3ODMwNDAwLCJleHAiOjE3Mjc5MTY4MDB9",
            "token_type": "bearer",
            "expires_in": 86400,
            "user": {"username": "aman.varma", "role": "Backend Admin"}
        }
    },
    {
        "id": "get_analytics",
        "method": "GET",
        "path": "/api/v1/analytics/overview",
        "title": "CRM Analytics Overview",
        "module": "Analytics",
        "description": "Aggregates CRM pipeline conversion metrics, NLP sentiment breakdown, and database response latency.",
        "sample_body": None,
        "sample_headers": {"Authorization": "Bearer eyJhbGciOiJI..."},
        "simulated_response": {
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
]

def get_available_endpoints():
    return NLPCRM_ENDPOINTS

def execute_simulated_endpoint(endpoint_id: str, payload: Dict[str, Any] = None) -> Dict[str, Any]:
    start_time = time.time()
    
    target = None
    for ep in NLPCRM_ENDPOINTS:
        if ep["id"] == endpoint_id:
            target = ep
            break
            
    if not target:
        return {"error": f"Endpoint '{endpoint_id}' not found.", "status_code": 404}

    # Simulate realistic network delay (15 - 45 ms)
    time.sleep(0.025)
    execution_time_ms = round((time.time() - start_time) * 1000, 2)
    
    resp = dict(target["simulated_response"])
    if payload and "text" in payload:
        # If user passed custom text in payload, customize response
        resp["analyzed_input"] = payload["text"]

    return {
        "endpoint": target["path"],
        "method": target["method"],
        "status_code": resp.get("status_code", 200),
        "execution_time_ms": execution_time_ms,
        "headers": {
            "Server": "FastAPI/0.109.0 (Uvicorn)",
            "Content-Type": "application/json",
            "X-RateLimit-Limit": "100",
            "X-RateLimit-Remaining": "98",
            "X-Process-Time-Sec": f"{execution_time_ms / 1000:.4f}"
        },
        "response_data": resp
    }

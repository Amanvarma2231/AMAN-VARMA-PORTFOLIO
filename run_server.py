import sys
import uvicorn

if __name__ == "__main__":
    print("[INFO] Starting Aman Varma Portfolio FastAPI Server on http://127.0.0.1:8000 ...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


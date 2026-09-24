from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

JUDGE0_API_URL = "https://api.judge0.com/submissions"

@app.post("/compile/")
async def compile_code(code_request: CodeRequest):
    headers = {"Content-Type": "application/json"}
    data = {
        "source_code": code_request.code,
        "language_id": 71,  # 71 corresponds to Python 3.8 in Judge0
        "stdin": "",  # Optional, input to the program
        "expected_output": "",  # Optional, expected output for testing
        "cpu_time_limit": 2,  # Optional, CPU time limit in seconds
        "wall_time_limit": 5,  # Optional, wall time limit in seconds
        "memory_limit": 128000,  # Optional, memory limit in bytes
    }
    
    response = requests.post(JUDGE0_API_URL, json=data, headers=headers)
    
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail="Failed to compile code")
    
    submission_token = response.json()["token"]
    result_url = f"{JUDGE0_API_URL}/{submission_token}"
    
    # Poll Judge0 API for the result (as an example, you might want to implement this)
    # Alternatively, Judge0 also supports webhook notifications for completion
    
    return {"result_url": result_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)

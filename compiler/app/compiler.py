import sys
import io
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

from compiler.app.main import JUDGE0_API_URL, CodeRequest

# def compile_code(code: str) -> str:
#     old_stdout = sys.stdout
#     redirected_output = sys.stdout = io.StringIO()

#     try:
#         exec(code)  # Execute the code
#     except Exception as e:
#         return f"Error: {e}"
#     finally:
#         sys.stdout = old_stdout

#     return redirected_output.getvalue()


def compile_code(code_request: CodeRequest):
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
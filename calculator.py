from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Calculator")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class CalculationRequest(BaseModel):
    expression: str


@app.get("/", response_class=FileResponse)
async def calculator_page():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/calc")
async def calculate(request: CalculationRequest):
    expression = request.expression.strip()

    allowed_characters = set("0123456789+-*/().% ")

    if not expression:
        raise HTTPException(status_code=400, detail="Enter an expression.")

    if any(character not in allowed_characters for character in expression):
        raise HTTPException(status_code=400, detail="Invalid expression.")

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return {"expression": expression, "result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid expression.")


if __name__ == "__main__":
    uvicorn.run("calculator:app", host="127.0.0.1", port=8000, reload=True)
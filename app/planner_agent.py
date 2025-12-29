import json
from pathlib import Path

def plan_requirement(requirement: str):
    """
    LLM-powered planner (mocked response, production-ready design)
    """

    # Load prompt (agent design)
    prompt = Path("app/prompts/planner_prompt.txt").read_text()

    # ---- MOCK LLM RESPONSE (replace with real OpenAI call later) ----
    llm_response = {
        "entities": ["User"],
        "features": [
            "User registration",
            "User login",
            "JWT authentication"
        ],
        "apis": [
            {"method": "POST", "path": "/register"},
            {"method": "POST", "path": "/login"}
        ]
    }
    # ---------------------------------------------------------------

    return llm_response

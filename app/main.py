from fastapi import FastAPI
from app.planner_agent import plan_requirement
from app.code_agent import generate_code

app = FastAPI()

@app.post("/generate")
def generate(requirement: str, project_name: str):
    plan = plan_requirement(requirement)
    path = generate_code(plan, project_name)

    return {
        "message": "Project generated successfully",
        "path": path,
        "plan": plan
    }

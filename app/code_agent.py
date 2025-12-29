from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("app/templates"))

def generate_code(plan: dict, project_name: str):
    project_path = f"generated_projects/{project_name}"
    os.makedirs(project_path, exist_ok=True)
    # DOCKERFILE
    docker_template = env.get_template("Dockerfile.jinja")
    docker_content = docker_template.render()

    with open(f"{project_path}/Dockerfile", "w") as f:
        f.write(docker_content)

    # README
    readme_template = env.get_template("README.jinja")
    readme_content = readme_template.render(
        project_name=project_name,
        features=plan["features"],
        apis=plan["apis"]
    )

    with open(f"{project_path}/README.md", "w") as f:
        f.write(readme_content)

    # MAIN API
    main_template = env.get_template("main_api.jinja")
    main_content = main_template.render(
        apis=plan["apis"],
        features=plan["features"]
    )

    with open(f"{project_path}/main.py", "w") as f:
        f.write(main_content)

    # JWT AUTH
    if "JWT authentication" in plan["features"]:
        auth_template = env.get_template("auth.jinja")
        with open(f"{project_path}/auth.py", "w") as f:
            f.write(auth_template.render())

    # DATABASE MODELS
    for entity in plan["entities"]:
        model_template = env.get_template("model.jinja")
        model_code = model_template.render(entity=entity)

        with open(f"{project_path}/models.py", "w") as f:
            f.write(model_code)

        crud_template = env.get_template("crud.jinja")
        crud_code = crud_template.render(entity=entity)

        with open(f"{project_path}/crud.py", "w") as f:
            f.write(crud_code)

    return project_path

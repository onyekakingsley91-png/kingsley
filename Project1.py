from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to my DevOps project!"}
@app.get("/health")
def health_check():
    return {"status": "healthy"}
@app.get("/tasks")
def get_tasks():
    return {
        "tasks": [
            {"id": 1, "name": "Learn Linux", "completed": True},
            {"id": 2, "name": "Learn Git", "completed": True},
            {"id": 3, "name": "Learn Docker", "completed": False}
        ]
    }
import os

BASE_DIR = r"C:\Users\nnaya\Desktop\ai_business_agent"

folders = [
    "data",
    "models",
    "notebooks"
]

files = [
    "data/sales.csv",
    "models/.gitkeep",
    "app.py",
    "agent.py",
    "model.py",
    "utils.py",
    "frontend.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

# Create folders
for folder in folders:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

# Create empty files
for file in files:
    file_path = os.path.join(BASE_DIR, file)
    with open(file_path, "w") as f:
        pass

print("✅ ai_business_agent project structure created successfully!")

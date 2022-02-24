import os
directories = [
        os.path.join(".github", "workflows"),
        "artifacts",
        os.path.join("data", "raw"),
        os.path.join("data", "processed"),
        "data_given",
        "notebooks",
        os.path.join("prediction_service", "model"),
        "report",
        "saved_models",
        "src",
        "tests",
        os.path.join("web_app", "static"),
        os.path.join("web_app", "templates"),
        os.path.join("web_app/static", "css"),
        os.path.join("web_app/static", "script"),
    ]

files = [
        ".gitignore",
        "Procfile"
        "README.md",
        "LICENSE",
        "app.py",
        "dvc.yaml",
        "params.yaml",
        "requirements.txt",
        "setup.py",
        "tox.ini",
        os.path.join('src', '__init__.py')
        ]

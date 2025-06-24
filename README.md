# Partner Workflow

Partner is an experimental application for building and managing software projects
with the help of a Large Language Model (LLM). The goal is to streamline the
software engineering workflow by providing a simple web interface for
brainstorming ideas, generating code snippets and managing project files.

## Features

* **LLM Integration** – connect to any HTTP based LLM API by supplying an API
  key, endpoint and model name.
* **Project Management** – initialise git repositories and create project files
  from the web interface or Python API.
* **Web UI** – small Flask app that exposes a chat style prompt box and shows
  responses from the LLM.
* **Brainstorming** – helper function to generate project ideas using the LLM.

## Requirements

* Python 3.8+
* see `requirements.txt` for Python dependencies.

## Quick Start

```bash
pip install -r requirements.txt
export LLM_API_KEY=your-key
export LLM_ENDPOINT=https://example.com/v1
export LLM_MODEL=model-name
python app.py
```

Open `http://localhost:5000` in a browser and submit a task prompt to interact
with the LLM.

## License

This project is provided under the terms of the MIT License. See `LICENSE` for
full details.

# AI-Based Assistant for Justice Services

An AI-powered conversational assistant designed to make justice-related information easier to explore through a simple, interactive chatbot interface.

Built with Python, Gradio, and the Hugging Face Inference API, the application uses a large language model to generate responses to user queries and supports configurable response-generation parameters.

## Overview

Accessing and understanding legal information can be challenging. This project explores how conversational AI can provide an accessible starting point for users seeking general justice-related information.

The application provides a chat interface where users can ask questions, maintain conversational context, and adjust model-generation settings to customize responses.

**Note:** This is an AI-based informational prototype, not a substitute for professional legal advice or assistance from a qualified lawyer.

## Features

- **Interactive AI chatbot:** Ask questions through a conversational interface.
- **Large language model integration:** Uses the `openai/gpt-oss-20b` model through the Hugging Face Inference API.
- **Conversation history:** Maintains chat context during an interaction.
- **Configurable system instructions:** Customize the assistant's behavior through a system-message field.
- **Adjustable response generation:** Configure maximum output tokens, temperature, and top-p sampling.
- **Gradio interface:** Provides a web-based interface for interacting with the model.
- **Hugging Face authentication:** Uses Gradio's login functionality to obtain an authenticated inference token.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Gradio | Interactive chatbot interface |
| Hugging Face Hub | Model inference API integration |
| GPT-OSS 20B | Language generation |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
AI-Based-Assistant-for-Justice-Services/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by the installed dependencies
- pip package manager
- Internet connectivity
- A Hugging Face account with access to the required inference service and model

### 1. Clone the repository

```bash
git clone https://github.com/sandeeppatr143-alt/AI-Based-Assistant-for-Justice-Services.git
cd AI-Based-Assistant-for-Justice-Services
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux or macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local URL displayed in the terminal to access the chatbot.

## How to Use

1. Launch the application.
2. Sign in through the Hugging Face login interface if prompted.
3. Enter a question in the chatbot.
4. Review the generated response and continue the conversation.
5. Adjust the system message, maximum output tokens, temperature, or top-p settings as needed.

## Configuration

The application exposes several generation parameters:

| Parameter | Purpose |
|---|---|
| System message | Defines the assistant's instructions and behavior |
| Max new tokens | Sets the maximum generated response length |
| Temperature | Controls variation in generated responses |
| Top-p | Controls nucleus sampling during generation |

The actual output depends on the model, prompt, inference availability, and selected parameters.

## Responsible Use

AI-generated legal information can be incomplete, outdated, or inaccurate.

- Verify important information using authoritative government sources and applicable legislation.
- Consult a qualified legal professional for case-specific advice.
- Do not rely on generated responses as a substitute for legal representation.
- Avoid entering confidential case details, personal identifiers, or sensitive documents.
- Do not assume that the model has access to current legislation or live court records.

## Limitations

- Responses depend on the selected language model and its available knowledge.
- The application does not establish that generated information is legally authoritative.
- Inference availability, authentication, rate limits, and usage restrictions may affect operation.
- This repository does not claim integration with official court databases or government justice-service systems.

## Future Improvements

Potential enhancements include:

- Retrieval-augmented generation using verified legal documents.
- Citations and links to authoritative legal sources.
- Support for Indian legal terminology and regional languages.
- Improved safeguards against misleading legal responses.
- Automated evaluation of answer quality and factual accuracy.
- Deployment with appropriate authentication, privacy controls, and monitoring.


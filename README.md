#  BunnyBot: Multimodal AI Personal Assistant

> An undergraduate capstone project (2023) exploring conversational AI, voice interaction, multimodal assistance, and personalized user management using Python.

---

## Overview

BunnyBot is a desktop-based AI assistant developed in Python as my undergraduate capstone project.

The project was initiated in July 2023, shortly after large language models became publicly accessible through APIs. At that time, conversational AI desktop applications with integrated speech interaction, image generation, user authentication, and persistent user history were still relatively uncommon in educational projects.

Rather than developing a simple chatbot, the objective was to design an extensible AI assistant capable of acting as a personal digital secretary by integrating multiple AI-powered services into a single desktop application.

---

## Motivation

The main motivation behind BunnyBot was to investigate how different AI capabilities could be combined into one unified assistant.

Instead of treating AI as a question-answering system, the project explored the idea of a digital personal assistant capable of managing different aspects of daily interaction, including:

- Conversational AI
- Voice-based communication
- Image generation
- Language translation
- Personal note management
- Multi-user account management
- Persistent conversation history

The long-term vision was an assistant capable of coordinating multiple intelligent services through one personalized interface.

---

## Features

- Secure user registration and authentication
- Multi-user account management
- SQLite database integration
- Personalized conversation history
- Voice-based AI assistant
- AI-powered text conversations
- AI image generation
- Language translation
- Personal note management
- Graphical desktop interface using Tkinter
- OpenAI API integration
- User profile management

---

## System Architecture

```
User
   │
   ▼
Authentication
   │
   ▼
Account Manager
   │
   ▼
BunnyBot Core
   ├── Voice Assistant
   ├── AI Chat
   ├── Image Generation
   ├── Translation
   ├── Notes
   │
   ▼
SQLite Database
   │
   ▼
Conversation History
```


---

## Technologies

- Python
- Tkinter
- SQLite3
- OpenAI API
- Pillow
- SpeechRecognition
- Requests
- JSON
- Threading

---

## Database Design

BunnyBot stores personalized information for every registered user.

### User Table

- Mobile Number
- First Name
- Last Name
- Birth Date
- Gender
- Country
- Email
- Password

### Conversation Table

- User Query
- Assistant Response
- Mobile Number

### Translation History

- Source Text
- Target Text
- Source Language
- Target Language
- Mobile Number

The database enables independent user accounts with isolated interaction histories.

---

## Screenshots

| Login | Registration |
|-------|--------------|
| <img width="621" height="429" alt="Screenshot 2024-02-18 170301" src="https://github.com/user-attachments/assets/669c1888-f89c-4a5d-9f08-ff85f2268c8e" />| <img width="623" height="431" alt="Screenshot 2024-02-18 170309" src="https://github.com/user-attachments/assets/c63dd876-992e-4c65-929a-bef8cb421e5d" />|

| AI Assistant | Translator |
|-------------|------------|
| <img width="622" height="430" alt="Screenshot 2024-02-18 170346" src="https://github.com/user-attachments/assets/4757d4bd-c54d-4af1-921b-979d5f7b24de" />| <img width="619" height="430" alt="Screenshot 2024-02-18 170409" src="https://github.com/user-attachments/assets/764891db-09f7-42f9-a65c-30a5145ad751" />|

| Image Generation | Notepad |
|-----------------|---------|
| <img width="622" height="430" alt="Screenshot 2024-02-18 170403" src="https://github.com/user-attachments/assets/1e477378-3ca2-4628-8510-316b4c7b3784" />| <img width="623" height="430" alt="Screenshot 2024-02-18 170418" src="https://github.com/user-attachments/assets/1cd75fbc-19e1-46c8-9c61-159530704f51" />|

---

## Project Structure

```
BunnyBot-Multimodal-AI-Assistant
│
├── src
├── screenshots
├── architecture
├── docs
├── database
├── assets
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/BunnyBot-Multimodal-AI-Assistant.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your OpenAI API Key.

Run the application.

```bash
python src/BunnyBot.py
```

---

## Security Notice

For security reasons, API keys are **not included** in this repository.

Replace the placeholder value inside the source code with your own API key before running the application.

---

## Academic Context

This project was developed as an undergraduate capstone project in Computer Engineering.

Project Start Date:

**19 July 2023**

Institution:

**Islamic Azad University**

Supervisor:

**Marzieh Dadvar**

---

## Project Goals

The project investigates how conversational AI can be integrated into a desktop environment together with authentication, persistent storage, voice interaction, and multimodal AI services.

Although the implementation relies on external AI APIs, the software architecture, graphical interface, database design, user management, and application integration were designed and implemented as part of this project.

---

## Future Improvements

Future versions may include:

- Local LLM support
- Retrieval-Augmented Generation (RAG)
- Long-term memory
- Calendar integration
- Email assistant
- Cloud synchronization
- Mobile application
- Plugin architecture
- Multi-agent framework

---

## Citation

If you use this repository in academic work, please cite it using the provided `CITATION.cff` file.

---

## License

This project is released under the MIT License.

---

## Author

**Hannah Fathi**

M.Sc. Student in Artificial Intelligence and Robotics

Interested in:

- Artificial Intelligence
- Computer Vision
- Remote Sensing
- Multimodal AI
- Large Language Models
- AI Systems

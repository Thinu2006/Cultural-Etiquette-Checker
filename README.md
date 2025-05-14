# 🌐 Cultural Etiquette Checker
![image Alt](https://github.com/Thinu2006/Cultural-Etiquette-Checker/blob/e8c7cd5d135daf90925198b6337685b1131a62ea/images/Cultural%20Etiquette%20Checker.png)

An interactive **LLM-powered AI tool** that provides detailed cultural etiquette advice for any country and situation using **Mistral LLM running locally through Ollama** and a simple web UI with Gradio.

---

## 🎯 Main Objective

The primary goal of this project is to demonstrate how to build an **LLM application using a local LLM (Mistral) via Ollama**, and integrate it into a user-friendly Gradio web interface.  
This project shows how LLMs can be used for **knowledge advisory systems**, providing **structured, context-aware cultural etiquette advice**.

---

## 📋 Project Description

**Cultural Etiquette Checker** assists users in understanding cultural norms, do's and don'ts, polite phrases, and behavior in various situations like business meetings, dining, greetings, etc. 

It leverages **Mistral LLM**, runs locally using **Ollama**, and provides instant answers via a **Gradio web interface**.

---

## 🚀 Features

- ✅ Uses **Mistral LLM** (via Ollama) for cultural etiquette generation.
- ✅ Structured advice format:
  - Overview
  - Do's
  - Don'ts
  - Phrases
  - Tips
- ✅ Simple and intuitive **web interface using Gradio**.
- ✅ Integrated **connection check and error handling**.

---

## 🛠 Technologies Used

- [Ollama](https://ollama.com/) (to run Mistral locally)
- [Mistral](https://mistral.ai/) (LLM model)
- [Gradio](https://gradio.app/) (for the UI)
- Python 

---

## 💻 Installation

### 1. Install Dependencies
```bash
pip install gradio ollama
```

### 2. Install & Run Ollama
Ensure Ollama is installed and running:
```bash
ollama serve
```

### 3. Pull the Mistral Model
```bash
ollama pull mistral
```

### 4. Run the App
```bash
python cultural_etiquette_checker.py
```
App will run at http://localhost:7860

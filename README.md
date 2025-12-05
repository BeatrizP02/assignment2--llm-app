# Devil's Advocate Debate Generator 

This is my LLM-powered application for **Assignment 2** of my Topics in Computer Science course.

The app generates **balanced debates** on user-provided topics using:

- **Tool Use Enhancement** (`choose_structure("debate")`)
- **Safety Filters** (rejects harmful topics)
- **Telemetry Logging**
- **Offline Evaluation Suite (18 tests)**

---

## Features

- Generates 4-part debates:
  - Argument For  
  - Argument Against  
  - Neutral Summary  
  - Discussion Questions  

- Rejects:
  - extremism  
  - violence  
  - illegal requests  
  - political manipulation  
  - prompt injections  

- Logs latency + pathway + model used  
- Fully reproducible through CLI  
- Offline evaluation script included  

---

## Installation

Install Python 3.10+  
Install **Ollama** at https://ollama.com/

Then pull the model:

```bash
MODEL = "qwen2.5:1.5b"


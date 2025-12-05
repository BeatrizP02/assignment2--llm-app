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

### Safety Filtering (Custom Tiered System)
The safety module rejects topics involving:
- extremism  
- violence or harm  
- weapon creation or usage  
- assassination or overthrow  
- prompt injection attempts  
- **modern war, military conflict, or geopolitical disputes** (e.g., “war,” “conflict,” “military,” “invasion”)

### Additional Functionality
- CLI help menu (`/help`)
- Input validation for empty/unsafe topics
- Telemetry logs written to `telemetry_logs.jsonl`
- Fully reproducible pipeline
- **94.4% offline evaluation pass rate** (17/18 tests)

---

## Installation

### 1. Install Python 3.10+  
### 2. Install **Ollama** at https://ollama.com/

### 3. Then pull the model:

```bash
ollama pull qwen2.5:1.5b
```

### 4. Install Python dependencies: 
```bash
pip install -r requirements.txt
```

## Usage 
### Run application
```bash
python app.py
```

### Then, enter a topic: E.x. Enter a debate topic: privacy vs security

----

## System Architecture Diagram 
           +---------------------+
           |      User (CLI)     |
           +----------+----------+
                      |
                      v
           +---------------------+
           |       app.py        |
           | - input loop        |
           | - help menu         |
           +----------+----------+
                      |
                      v
           +---------------------+
           |   Safety Filter     |
           | check_input_safety  |
           +----------+----------+
                      |
                      v
           +---------------------+
           |    Tool Function    |
           | choose_structure()  |
           +----------+----------+
                      |
                      v
           +---------------------+
           |   LLM Client Layer  |
           |    ollama_chat()    |
           +----------+----------+
                      |
                      v
           +---------------------+
           |     Ollama Model    |
           |    qwen2.5:1.5b     |
           +---------------------+


## Offline Evaluation Results 
### To run the evaluation suite:
```bash
python eval_tests.py
```

### My system achieved: PASS RATE: 18/18 (100.0%)
  -All safety tests passed successfully including all safey, tone, and robustness checks

## Telemetry Logging 
Each debate generation logs:
  -timestamp
  -model used
  -input length
  -response latency

Logs are saved in: telemetry_logs.jsonl
View them using"
```bash
cat telemetry_logs.jsonl
```

## Demo Video
Youtube Link: https://youtu.be/X5EnxWXibpQ
import time
import json
from datetime import datetime

LOG_FILE = "telemetry_logs.jsonl"

def log_event(pathway: str, latency: float, input_length: int, model: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "pathway": pathway,
        "latency": latency,
        "input_length": input_length,
        "model": model
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

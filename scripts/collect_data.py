import json
import os
import platform
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "log.json")

os.makedirs(DATA_DIR, exist_ok=True)

entry = {
    "timestamp": datetime.utcnow().isoformat(),
    "platform": platform.system(),
    "python_version": platform.python_version()
}

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = []

data.append(entry)

with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=2)

print("Data logged successfully")
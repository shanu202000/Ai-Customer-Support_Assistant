# %%
from pathlib import Path
import sys

source_path = globals().get("__file__")
start_path = Path(source_path).resolve().parent if source_path else Path.cwd().resolve()
for candidate in (start_path, *start_path.parents):
    if (candidate / "pyproject.toml").is_file():
        PROJECT_ROOT = candidate
        break
else:
    raise FileNotFoundError("Could not locate the project root (pyproject.toml).")

project_root = str(PROJECT_ROOT)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

from app.ai.decide import decide

# %%
import asyncio

question = "My board loses air overnight."
thread = f"Subject: Playground question\n\nCustomer:\n{question}"
decision = asyncio.run(asyncio.to_thread(decide, thread))

# %%
print(decision.model_dump_json(indent=2))

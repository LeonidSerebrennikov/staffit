from pathlib import Path
import importlib

for file_path in Path(__file__).parent.glob("*.py"):
    if file_path.name != "__init__.py":
        module_name = file_path.stem
        importlib.import_module(f".{module_name}", __package__)
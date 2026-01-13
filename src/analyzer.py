import os
import re
import json
import sys

def analyze(path):
    classes = set()
    functions = set()

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                        classes.update(re.findall(r"class (\w+)", content))
                        functions.update(re.findall(r"def (\w+)\(", content))
                except:
                    pass

    return {
        "classes": list(classes),
        "functions": list(functions)
    }

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    result = analyze(target)

    os.makedirs("output", exist_ok=True)
    with open("output/entities.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Analysis complete. Output written to output/entities.json")

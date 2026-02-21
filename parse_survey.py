import re
import os

with open("/Users/alex/Alex/monash/continual-learning/refs/Continual Learning of Large Language Models: A Comprehensive Survey/Continual Learning of Large Language Models: A Comprehensive Survey.md", "r") as f:
    lines = f.readlines()

methods = []
for i in range(len(lines)):
    line = lines[i]
    # Look for bolded model names, which in this survey seems to be like **O-LoRA** or **ELLE**
    # or sections like `2.2.2 Techniques of Continual Learning`
    # Many Continual Learning papers just list them and explain them.
    # We will search for bold words that are followed by citations, e.g., "**Adapter** [12]"
    matches = re.findall(r'\*\*([A-Za-z0-9\-]+)\*\*(?:\s+\[\d+(?:,\s*\d+)*\]|\s+is\s|\s+proposes)', line)
    for match in matches:
        if len(match) > 2 and match not in ['Continual', 'Learning', 'Large', 'Language', 'Models']:
            methods.append(match)

methods = list(set(methods))
print(sorted(methods))

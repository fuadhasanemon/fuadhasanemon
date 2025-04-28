import random
from datetime import datetime

# List of quotes
quotes = [
    '"Code is like humor. When you have to explain it, it’s bad." – Cory House',
    '"First, solve the problem. Then, write the code." – John Johnson',
    '"Experience is the name everyone gives to their mistakes." – Oscar Wilde',
    '"Java is to JavaScript what car is to Carpet." – Chris Heilmann',
    '"Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code." – Dan Salomon',
    '"Fix the cause, not the symptom." – Steve Maguire',
    '"Simplicity is the soul of efficiency." – Austin Freeman',
    '"Before software can be reusable it first has to be usable." – Ralph Johnson',
    '"Make it work, make it right, make it fast." – Kent Beck'
]

# Pick a random quote
quote_of_the_day = random.choice(quotes)

# Read the README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.readlines()

# Replace the Quote section
with open("README.md", "w", encoding="utf-8") as f:
    for line in content:
        if line.strip().startswith(">"):
            f.write(f"> {quote_of_the_day}\n")
        else:
            f.write(line)

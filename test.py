import os

secret = os.environ.get("CLAUDE_MODEL")

if secret:
    print("foi")
else:
    print("nao foi")

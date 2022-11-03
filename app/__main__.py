import sys

from .app import App

if len(sys.argv) <= 1:
    print("File not provided.")
    sys.exit()
app = App()
app.run(sys.argv[1])

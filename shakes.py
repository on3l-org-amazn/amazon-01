#!/usr/env python3

import sys
from flask import Flask

app = Flask()

@app.route("/"):
def index():
    return "This is the home page"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

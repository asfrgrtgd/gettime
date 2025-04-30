from flask import Flask, jsonify, request
from datetime import datetime, timezone, timedelta
import sd
app = Flask(__name__)
JST = timezone(timedelta(hours=9))

@app.route("/")
def sum_digits():
    return sd.sd()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

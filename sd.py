from datetime import datetime, timezone, timedelta
from flask import Flask, jsonify, request

def sd():
    JST = timezone(timedelta(hours=9))
    timestr = datetime.now(JST).strftime("%H%M%S")
    return jsonify(
        time=timestr,
        digit_sum=sum(int(d) for d in timestr)
    )
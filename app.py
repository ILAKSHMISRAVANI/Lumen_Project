from flask import Flask

@app.route("/", methods=["GET"])
def loginpage():
    return "Hello World :)"

import os
import sys

from flask import Flask, request, jsonify, render_template

from miller_rabin import probably_prime

DEBUG = True if os.environ.get("DEBUG", "") == "" else bool(os.environ.get("DEBUG"))

try:
    PORT = int(sys.argv[1])
except IndexError:
    PORT = 5000

APPLICATION_HOST = os.environ.get("APPLICATION_HOST", "localhost:{0}".format(PORT))

app = Flask(__name__)


@app.route("/")
def index():
    example_link = "http://{0}/miller-rabin?prime=98764321261&accuracy=10000".format(APPLICATION_HOST)
    return render_template("index.html", example_link=example_link)


@app.route("/miller-rabin")
def miller_rabin_route():
    prime = int(request.args.get("prime"))
    accuracy = int(request.args.get("accuracy"))
    return jsonify(result=probably_prime(prime, accuracy))


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT, host="0.0.0.0")

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import Optimizer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

@app.route('/app/') 
@cross_origin()
def result():
    tickers = request.args.get('tickers')
    #tickers = "GOOGL TSLA"
    minr, maxr = Optimizer.optimize(tickers)
    data = {"minr": minr.to_json(), "maxr": maxr.to_json()}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import Optimizer

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

@app.route('/app/') 
def result():
    tickers = request.args.get('tickers')
    #tickers = "GOOGL TSLA"
    minr, maxr = Optimizer.optimize(tickers)
    data = {"minr": minr.to_json(), "maxr": maxr.to_json()}
    print(minr.to_json())
    print(maxr.to_json())
    
    print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
    
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/insightsApi/expectedCompletionTime', methods=['POST'])
def calculateExpectedCompletionTime():
    data = request.get_json()
    
    result = {'prediction': 'Sample completion time'}
    
    return jsonify(result)


@app.route('/insightsApi/bookRecommendations', methods=['POST'])
def calculateBookRecommendations():
    data = request.get_json()
    
    result = {'prediction': 'Sample book recommendations'}
    
    return jsonify(result)


@app.route('/insightsApi/popularBooks', methods=['POST'])
def calculatePopularBooks():
    data = request.get_json()
    
    result = {'prediction': 'Sample popular books'}
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

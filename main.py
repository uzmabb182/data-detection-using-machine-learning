from flask import Flask, render_template, jsonify
from data import reduced_column_names

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/Analysis')
def about():
    return render_template('about.html')


@app.route('/Supervised_Machine_Learning')
def predictions():
    return render_template('predictions.html')


@app.route('/api/feature_names')
def feature_names():
    return jsonify(reduced_column_names)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)
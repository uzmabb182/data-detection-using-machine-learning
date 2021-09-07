from flask import Flask, render_template, jsonify, request
from data import reduced_column_names
import joblib
import pandas as pd
app = Flask(__name__)
trained_machine_learning_model=joblib.load('static/data_processing/reduced_features_random_forest_updated.joblib')

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


@app.route('/api/generate_prediction', methods=['POST'])
def generate_prediction():
    user_inputs=request.json
    predict_df=pd.DataFrame({
    'SUSPECT_ARRESTED_FLAG':[int(user_inputs['SUSPECT_ARRESTED_FLAG'])],
    'YEAR':[int(user_inputs['YEAR'])],
    'OBSERVED_DURATION_MINUTES':[int(user_inputs['OBSERVED_DURATION_MINUTES'])],
    'DAY':[int(user_inputs['DAY'])],
    'MONTH':[int(user_inputs['MONTH'])],
    'STOP_DURATION_MINUTES':[int(user_inputs['STOP_DURATION_MINUTES'])],
    'SUSPECT_HEIGHT':[int(user_inputs['SUSPECT_HEIGHT'])],
    'SUSPECT_WEIGHT':[int(user_inputs['SUSPECT_WEIGHT'])],
    'SUSPECT_REPORTED_AGE':[int(user_inputs['SUSPECT_REPORTED_AGE'])],
    'SECONDS':[int(user_inputs['SECONDS'])],
    'STOP_LOCATION_X':[float(user_inputs['STOP_LOCATION_X'])],
    'STOP_LOCATION_Y':[float(user_inputs['STOP_LOCATION_Y'])]
    })
    prediction=str(trained_machine_learning_model.predict(predict_df)[0])
    return jsonify([prediction])


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
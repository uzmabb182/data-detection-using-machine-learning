from flask import Flask, render_template, jsonify, request
from data import reduced_column_names_and_labels
from data import arrest_reduced_column_names_and_labels
import joblib
import pandas as pd
app = Flask(__name__)
trained_machine_learning_model=joblib.load('static/data_processing/reduced_features_random_forest_updated.joblib')
trained_machine_learning_model_1=joblib.load('static/data_processing/reduced_features_random_forest_arrest.joblib')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/analysis')
def visual_analysis():
    return render_template('analysis.html')


@app.route('/tableau')
def visual_tableau():
    return render_template('tableau.html')


@app.route('/summon_predictions')
def predictions():
    return render_template('summon_predictions.html')


@app.route('/api/generate_summon_prediction', methods=['POST'])
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
    return jsonify(reduced_column_names_and_labels)

@app.route('/arrest_predictions')
def predictions_arrest():
    return render_template('arrest_predictions.html')


@app.route('/api/generate_arrest_prediction', methods=['POST'])
def generate_prediction_arrest():
    user_inputs=request.json
    predict_df=pd.DataFrame({
    'SEARCHED_FLAG':[int(user_inputs['SEARCHED_FLAG'])],
    'WEAPON_FOUND_FLAG':[int(user_inputs['WEAPON_FOUND_FLAG'])],
    'SUSPECT_REPORTED_AGE':[int(user_inputs['SUSPECT_REPORTED_AGE'])],
    'STOP_DURATION_MINUTES':[int(user_inputs['STOP_DURATION_MINUTES'])],
    'MONTH':[int(user_inputs['MONTH'])],
    'DAY':[int(user_inputs['DAY'])],
    'OBSERVED_DURATION_MINUTES':[int(user_inputs['OBSERVED_DURATION_MINUTES'])],
    'FRISKED_FLAG':[int(user_inputs['FRISKED_FLAG'])],
    'YEAR':[int(user_inputs['YEAR'])],
    'OFFICER_EXPLAINED_STOP_FLAG':[int(user_inputs['OFFICER_EXPLAINED_STOP_FLAG'])],
    'OFFICER_IN_UNIFORM_FLAG':[float(user_inputs['OFFICER_IN_UNIFORM_FLAG'])],
    'SUMMONS_ISSUED_FLAG':[float(user_inputs['SUMMONS_ISSUED_FLAG'])]
    })
    prediction_arrest=str(trained_machine_learning_model_1.predict(predict_df)[0])
    return jsonify([prediction_arrest])


@app.route('/api/arrest_feature_names')
def feature_names_arrest():
    return jsonify(arrest_reduced_column_names_and_labels)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)
from flask import Flask, render_template, request
import pickle

model = pickle.load(open("model/model_randomforest.pkl", "rb"))
app = Flask(__name__)

@app.route('/')
def loadpage():
    return render_template('index.html')

@app.route('/y_predict', methods=['POST'])
def prediction():
    Age = request.form["Age"]
    SystolicBP = request.form["SystolicBP"]
    DiastolicBP = request.form["DiastolicBP"]
    BS = request.form["BS"]
    BodyTemp = request.form["BodyTemp"]
    HeartRate = request.form["HeartRate"]
    
    p=[[float(Age), float(SystolicBP), float(DiastolicBP), float(BS), float(BodyTemp), float(HeartRate)]]
    prediction=model.predict(p)
    
    if(prediction == ['high risk']):
        text = "Patient is at High Risk"
    elif(prediction == ['mid risk']):
        text = "Patient is at Mid Risk"
    else:
        text = "Patient is at Low Risk"

    return render_template("index.html", prediction_text=text)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
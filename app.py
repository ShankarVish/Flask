import pickle
from flask import Flask , request

app = Flask(__name__)

#model_pickle =open("/Users/shankarvishnu/Desktop/code/MLOps/Flask/artefacts/classifier.pkl", "rb")
model_pickle = open("artefacts/classifier.pkl", "rb")
clf = pickle.load(model_pickle)

# CREATING ENDPOINTS
@app.route("/ping", methods=['GET'])  # mapping "ping" function to the URL
def ping():
    return {"message": "Hi There, I'm Working"}


# DEFINING THE ENDPOINT WHICH WILL KE THE PREDICTION
@app.route("/predict" , methods= ["POST"])
def prediction():
    """
    Returns loan application status using ML model
    """
    loan_req = request.get_json()
    print(loan_req)
    
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000

    # Making predictions 
    prediction = clf.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return {"Loan Approval Status":pred }

if __name__ == "__main__":
    app.run(debug=True)






""""
{
"Gender": "Male",
"Married": "Unmarried",
"ApplicantIncome": 500000,
"Credit_History": "Cleared Debts",
"LoanAmount": 50000
}

"""
import pandas as pd
import joblib
import sklearn
sklearn.set_config(enable_metadata_routing=False)

class CraditModel():
    def __init__(self, ModelPath: str, PreProcessorPath: str) -> None:
        self.ModelPath = ModelPath
        self.PreProcessorPath = PreProcessorPath
        
        # Create and load the model
        self.Model = joblib.load(self.ModelPath)
        
        # Load the preprocessor
        self.preprocessor = joblib.load(self.PreProcessorPath)
    

    
    def Prediction(self, InputData: dict) -> list:
        if not isinstance(InputData, pd.DataFrame):
            input_data = pd.DataFrame(InputData, index=[0])
        else:
            input_data = InputData
        
        input_data = self.preprocessor.transform(input_data)
        output = self.Model.predict(input_data )
        return output.tolist()


        

if __name__ == "__main__":
     
    Model= CraditModel(ModelPath="model_credit.joblib" , PreProcessorPath="preprocessor.pkl")

    loan_data = {
    'Month': 'May',
    'Age': 28,
    'Occupation': 'Teacher',
    'Annual_Income': 34847.84,
    'Monthly_Inhand_Salary': 3037.986667,
    'Num_Bank_Accounts': 2,
    'Num_Credit_Card': 4,
    'Interest_Rate': 6,
    'Num_of_Loan': 1,
    'Delay_from_due_date': 3,
    'Num_of_Delayed_Payment': 1,
    'Changed_Credit_Limit': 6.42,
    'Num_Credit_Inquiries': 2.0,
    'Credit_Mix': 'Good',
    'Outstanding_Debt': 605.03,
    'Credit_Utilization_Ratio': 34.977895,
    'Credit_History_Age': '26 Years and 11 Months',
    'Payment_of_Min_Amount': 'No',
    'Total_EMI_per_month': 18.816215,
    'Amount_invested_monthly': 130.11542024292334,
    'Payment_Behaviour': 'Low_spent_Small_value_payments',
    'Monthly_Balance': 444.8670318506144
    }

    output =Model.Prediction(InputData=loan_data)

    print(output)

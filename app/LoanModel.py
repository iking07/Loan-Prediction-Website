import tensorflow as tf
import pandas as pd
import pickle

class LoanModel():
    def __init__(self, ModelPath: str, PreProcessorPath: str) -> None:
        self.ModelPath = ModelPath
        self.PreProcessorPath = PreProcessorPath
        
        # Create and load the model
        self.Model = self.create_model()
        self.Model.load_weights(self.ModelPath)
        
        # Load the preprocessor
        with open(self.PreProcessorPath, 'rb') as file:
            self.preprocessor = pickle.load(file)
    
    def create_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(37,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(2, activation='softmax')
        ])
        return model
    
    def Prediction(self, InputData: dict) -> list:
        if not isinstance(InputData, pd.DataFrame):
            input_data = pd.DataFrame(InputData, index=[0])
        else:
            input_data = InputData
        
        input_data = self.preprocessor.transform(input_data)
        output = self.Model.predict(input_data , verbose=0)
        return output.tolist()


        

if __name__ == "__main__":
     
    Model= LoanModel(ModelPath="model.keras" , PreProcessorPath="preprocessor.pkl")

    loan_data = {
    'Loan Amount': 3558,
    'Funded Amount': 27818,
    'Funded Amount Investor': 14366.99572,
    'Term': 59,
    'Interest Rate': 7.516895,
    'Home Ownership': 46869.40606,
    'Verification Status': 'Not Verified',
    'Loan Title': 'Uncategorized',
    'Debit to Income': 38.480037,
    'Delinquency - two years': 0,
    'Inquires - six months': 0,
    'Open Account': 8,
    'Public Record': 0,
    'Revolving Balance': 1054,
    'Revolving Utilities': 50.710557,
    'Total Accounts': 14,
    'Total Received Interest': 159.964983,
    'Total Received Late Fee': 0.006574,
    'Recoveries': 6.858643,
    'Collection Recovery Fee': 43.220717,
    'Collection 12 months Medical': 0.0,
    'Application Type': 'INDIVIDUAL',
    'Last week Pay': 134.0,
    'Accounts Delinquent': 0.0,
    'Total Collection Amount': 59.0,
    'Total Current Balance': 228507.0,
    'Total Revolving Credit Limit': 8455.0
    }

    output =Model.Prediction(InputData=loan_data)

    print(output)

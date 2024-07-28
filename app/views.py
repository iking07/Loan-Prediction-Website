from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .LoanModel import LoanModel
from .CraditModel import CraditModel
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import tensorflow as tf
import json
import os


Loan_Model =LoanModel(ModelPath=os.path.join(settings.STATIC_ROOT ,"models","LoanPrediction","model.keras" ),PreProcessorPath=os.path.join(settings.STATIC_ROOT ,"models","LoanPrediction","preprocessor.pkl"))

Cradit_Model = CraditModel(ModelPath=os.path.join(settings.STATIC_ROOT,"models","CraditScore","model_credit.joblib" ),PreProcessorPath=os.path.join(settings.STATIC_ROOT ,"models","CraditScore","preprocessor.pkl"))


def index(request):
    return render(request,"Index.html")

def about(request):
    return render(request ,"AboutUs.html")

def test(request):
    return render(request , "test.html")




@csrf_exempt
@require_http_methods(["POST"])
def loan_prediction(request):
    try:
        data = json.loads(request.body)
        loan_data = {
            'Loan Amount': float(data.get('loan-amount', 0)),
            'Funded Amount': float(data.get('funded-amount', 0)),
            'Funded Amount Investor': float(data.get('funded-amount-investor', 14366.99572)),
            'Term': int(data.get('loan-term', 0)),
            'Interest Rate': float(data.get('interest-rate', 0)),
            'Home Ownership': 46869.40606,
            'Verification Status': data.get('verification-status', 'Not Verified'),
            'Loan Title': data.get('loan-title', 'Uncategorized'),
            'Debit to Income': float(data.get('debt-to-income', 38.480037)),
            'Delinquency - two years': int(data.get('delinquency-two-years', 0)),
            'Inquires - six months': int(data.get('inquiries-six-months', 0)),
            'Open Account': int(data.get('open-accounts', 8)),
            'Public Record': int(data.get('public-record', 0)),
            'Revolving Balance': float(data.get('revolving-balance', 1054)),
            'Revolving Utilities': float(data.get('revolving-utilities', 50.710557)),
            'Total Accounts': int(data.get('total-accounts', 14)),
            'Total Received Interest': float(data.get('total-received-interest', 159.964983)),
            'Total Received Late Fee': float(data.get('total-received-late-fee', 0.006574)),
            'Recoveries': float(data.get('recoveries', 6.858643)),
            'Collection Recovery Fee': float(data.get('collection-recovery-fee', 43.220717)),
            'Collection 12 months Medical': float(data.get('collection-12-months-medical', 0.0)),
            'Application Type': data.get('application-type', 'INDIVIDUAL'),
            'Last week Pay': float(data.get('last-week-pay', 134.0)),
            'Accounts Delinquent': float(data.get('accounts-delinquent', 0.0)),
            'Total Collection Amount': float(data.get('total-collection-amount', 59.0)),
            'Total Current Balance': float(data.get('total-current-balance', 228507.0)),
            'Total Revolving Credit Limit': float(data.get('total-revolving-credit-limit', 8455.0))
        }
        try:
            result = Loan_Model.Prediction(loan_data)
        except Exception as e :
            print(e)
            result = "error"    
        return JsonResponse({'prediction': result})
    except Exception as e:
        print(e)
        return JsonResponse({'prediction': "error"})

 

        












@csrf_exempt
@require_http_methods(["POST"])
def CraditPrediction(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            loan_data = {
                'Month': data.get('Month', ''),
                'Age': int(data.get('Age', 0)),
                'Occupation': data.get('Occupation', ''),
                'Annual_Income': float(data.get('Annual Income', 0)),
                'Monthly_Inhand_Salary': float(data.get('Monthly Inhand Salary', 0)),
                'Num_Bank_Accounts': int(data.get('Number of bank accounts', 0)),
                'Num_Credit_Card': int(data.get('Number of Credit Cards', 0)),
                'Interest_Rate': float(data.get('interest rate', 0)),
                'Num_of_Loan': int(data.get('Number of Loans', 0)),
                'Delay_from_due_date': int(data.get('Delay from Due Date', 0)),
                'Num_of_Delayed_Payment': int(data.get('Number of Delayed Payment', 0)),
                'Changed_Credit_Limit': float(data.get('Changed Credit Limit', 0)),
                'Num_Credit_Inquiries': float(data.get('Number of Credi Inquiries', 0)),
                'Credit_Mix': data.get('Credit Mix', ''),
                'Outstanding_Debt': float(data.get('Outstanding Debt', 0)),
                'Credit_Utilization_Ratio': float(data.get('Credit Utilization', 0)),
                'Credit_History_Age': f"{data.get('Credit History Age', 0)} Years and 0 Months" ,
                'Payment_of_Min_Amount': data.get('Payments of Minimum Amount', ''),
                'Total_EMI_per_month': float(data.get('Total EMI per month', 0)),
                'Amount_invested_monthly': float(data.get('Amount Invested Monthly', 0)),
                'Payment_Behaviour': data.get('Payment Behaviour', ''),
                'Monthly_Balance': float(data.get('Monthly Balance', 0))
            }

            output =Cradit_Model.Prediction(InputData=loan_data)

            return JsonResponse({'prediction': output[0]})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    # loan_data = {
    # 'Month': 'May',
    # 'Age': 28,
    # 'Occupation': 'Teacher',
    # 'Annual_Income': 34847.84,
    # 'Monthly_Inhand_Salary': 3037.986667,
    # 'Num_Bank_Accounts': 2,
    # 'Num_Credit_Card': 4,
    # 'Interest_Rate': 6,
    # 'Num_of_Loan': 1,
    # 'Delay_from_due_date': 3,
    # 'Num_of_Delayed_Payment': 1,
    # 'Changed_Credit_Limit': 6.42,
    # 'Num_Credit_Inquiries': 2.0,
    # 'Credit_Mix': 'Good',
    # 'Outstanding_Debt': 605.03,
    # 'Credit_Utilization_Ratio': 34.977895,
    # 'Credit_History_Age': '26 Years and 11 Months',
    # 'Payment_of_Min_Amount': 'No',
    # 'Total_EMI_per_month': 18.816215,
    # 'Amount_invested_monthly': 130.11542024292334,
    # 'Payment_Behaviour': 'Low_spent_Small_value_payments',
    # 'Monthly_Balance': 444.8670318506144
    # }

    # output =Cradit_Model.Prediction(InputData=loan_data)
    # return HttpResponse(f"{(output[0])}")

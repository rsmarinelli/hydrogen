### Hydrogen Payroll Transaction Mock-Up API

# Author: Ryan Marinelli
# Date: December 2020


# Import Python Libraries
import pandas as pd
from flask import Flask, request 
from flask_restful import  Api , Resource

# Import Data
payroll_transactions_csv = 'data/payroll_debit_card_transaction_data.csv'
employee_profile_csv = 'data/employee_profile_data.csv'
cards_csv = 'data/cards_data.csv'

# Build API
app = Flask(__name__)
api = Api(app)

class Home(Resource):    
    def get(self):
        #home endpoint to inform the user about the available endpoints
        message = "API contains the following Endpoints: [/transactions, /employees, /cards]."
        return message


class PayrollTransactions(Resource):
    def get(self):      
        try: 
            data = pd.read_csv(payroll_transactions_csv)
        except Exception:
            return { 'message': 'Error processing data. Unable to return transactions.', 'status': 500 }, 500 
        
        # Optional Parameter to return specific employee transactions
        employee_id = request.args.get('employee_id')        
        if employee_id is not None:
            data = data[data.employee_id == employee_id]
        
        # Returns appropriate transaction(s) - defaults to all 
        data = data.to_dict('records') 
            
        return {'data': data}, 200
    
class Employees(Resource):
    def get(self):
        try: 
            data = pd.read_csv(employee_profile_csv)
        except Exception:
            return { 'message': 'Error processing data. Unable to return employee information.', 'status': 500 }, 500 
        
        # Optional Parameter to return specific employee information
        employee_id = request.args.get('employee_id')        
        if employee_id is not None:
            data = data[data.employee_id == employee_id]
        
        # Returns appropriate employee(s) - defaults to all 
        data = data.to_dict('records') 
            
        return {'data': data}, 200

class Cards(Resource):
    def get(self):
        try: 
            data = pd.read_csv(cards_csv)
        except Exception:
            return { 'message': 'Error processing data. Unable to return card information.', 'status': 500 }, 500 
        
        # Optional Parameter to return specific employee cards
        employee_id = request.args.get('employee_id')        
        if employee_id is not None:
            data = data[data.employee_id == employee_id]
        
        # Returns appropriate card(s) - defaults to all 
        data = data.to_dict('records') 
            
        return {'data': data}, 200
    
# Endpoints
api.add_resource(Home, '/')
api.add_resource(PayrollTransactions, '/transactions')  # '/transactions' endpoint to access payroll transaction data
api.add_resource(Employees, '/employees')  # '/employees' endpoint to access employee profile data
api.add_resource(Cards, '/cards')  # '/cards' endpoint to access cards data

      
# Execute Flask App
if __name__ == '__main__':
    app.run() 
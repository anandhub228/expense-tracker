"""
Expense Tracker

A command-line expense tracking application built with Python.
Features:
- Add, edit, delete expenses
- Search and filter expenses
- Budget tracking
- Monthly and category summaries

Created by: Anandhu B
Date: May 2026
"""

import json
import os
from datetime import datetime

EXPENSE = "expense_track.json"
BUDGET = "budget.json"

if os.path.exists(BUDGET):
    with open(BUDGET) as f:
        budget = json.load(f)
else:
    budget = 0
    
if os.path.exists(EXPENSE):
    with open(EXPENSE) as f:
        expense = json.load(f)
        
else:
    expense = []
    
 # Main loop       
while True:
    print("\n1. Add expense")
    print("2. View expense")
    print("3. Delete expense")
    print("4. Show total expense")
    print("5. Edit expense")
    print("6. Search expense")
    print("7. Category summary")
    print("8. Monthly summary")
    print("9. Filter by category")
    print("10. Highest expense")
    print("11. Lowest expense")
    print("12. Set budget")
    print("13. Current budget")
    print("14. Exit")
    
    choice = input("Enter your choice:").lower()
    
    # ADDING EXPENSE
    if choice =="1" or choice == "add expense":
        name = input("Enter expense name:")
        try:
            amount = float(input("Enter expense amount:"))
        except ValueError:
            print("Please enter a valid number")
            continue
        if amount <= 0:
            print("Amount must be greater than 0")
            continue
        category = input("Enter the category:")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_expense = { "name":name, "amount": amount, "category":category, "date":date}
        expense.append(new_expense)
        with open(EXPENSE, "w") as f:
            json.dump(expense, f, indent=4)
        print("Expense added successfully")
            
        total = 0
        for item in expense:
            total += item["amount"]
        if budget > 0 and total > budget:
            print(f"WARNING! Budget exceeded by {total - budget}")
     
    # VIEWING EXPENSE               
    elif choice =="2" or choice == "view expense":
        if len(expense) == 0:
            print("No expense available")
        else:
            print("\nYour expense")
            for item in expense:
                print(f"Name:{item['name']} | Amount: {item['amount']} | Category:{item['category']} | Date:{item['date']}")   
                
     # DELETING  EXPENSE       
    elif choice == "3" or choice =="delete expense": 
        if len(expense) == 0:
            print("No expense available")
        else:
            print("\nYour expense")
            for index, item in enumerate(expense, start=1):
                print(f"{index}. Name:{item['name']} | amount: {item['amount']} | Category:{item['category']}")
                                        
            try:
                delete_index = int(input("Enter expense number to delete:"))
                if delete_index < 1 or delete_index > len(expense):
                    print("Invalid expense number")
                    continue
                removed_expense = expense.pop(delete_index - 1)                
                with open(EXPENSE, "w") as f:
                    json.dump(expense, f, indent=4)
                    print("Deleted:", removed_expense)
            except ValueError:
                print("Invalid expense number")
   
   # SHOWING TOTAL EXPENSE
    elif choice == "4" or choice == "show total expense":
        total = 0
        for item in expense:
            total += item["amount"]
        print(f"Total expense is: {total}")
    
    # EDITING EXPENSE
    elif choice == "5" or choice == "edit expense":
        if len(expense) == 0:
            print("No expense available to edit")
        else:
            print("\nYour expense:")
            for index, item in enumerate(expense, start=1):
                print(f"{index}. Name:{item['name']} | amount: {item['amount']} | Category:{item['category']}")
            try:
                edit_index = int(input("Enter the expense number to edit:"))
                if edit_index < 1 or edit_index > len(expense):                                        
                    print("Invalid expense number")
                    continue
                edit_expense = expense[edit_index - 1]
            except ValueError:
                print("Invalid choice number")
                continue
            new_name = input("Enter new name:")
            edit_expense["name"] = new_name
            try:
                new_amount = float(input("Enter new amount:"))
            except ValueError:
                print("Please enter a valid number")
                continue
            if new_amount <= 0:
                print("Amount must be greater than 0")
                continue
            edit_expense["amount"] = new_amount
            new_category = input("Enter new category:")
            edit_expense["category"] = new_category
            new_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            edit_expense["date"] = new_date
            with open(EXPENSE, "w") as f:
                json.dump(expense, f, indent=4)
            print("Expense edited successfully")
     
    # SEARCHING EXPENSE       
    elif choice == "6" or choice == "search expense":
        search_expense = input("Enter expense name or category to search:")
        if search_expense.strip() == "":
            print("Search cannot be empty")
            continue
        found = False
        for item in expense:
            condition_for_name = search_expense.lower() in item["name"].lower()
            condition_for_category = search_expense.lower() in item["category"].lower()
            if condition_for_name or condition_for_category:
                found = True
                print(f"Name:{item['name']} | Amount:{item['amount']} | Category:{item['category']} | Date:{item['date']}") 
        if not found:
            print("Expense not found")                
    
    # CATEGORY SUMMARY
    elif choice == "7" or choice == "category summary":
        summary = {}
        for item in expense:
            category = item["category"]
            amount = item["amount"]
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount 
        for category, amount in summary.items():
            print(f"{category} : {amount}")  
     
     # MONTHLY SUMMARY
    elif choice == "8" or choice == "monthly summary":
        monthly_summary = {}
        for item in expense:
            date = item["date"]
            month = date[:7]
            amount = item["amount"]
            if month in monthly_summary:
                monthly_summary[month] += amount
            else:
                monthly_summary[month] = amount
        for month, amount in monthly_summary.items():
                print(f"{month} : {amount}")
                
    # FILTER BY CATEGORY   
    elif choice == "9" or choice == "filter by category":
        filter_category = input("Enter category to filter:").lower()
        found = False
        for item in expense:
            category = item["category"].lower()
            if filter_category == category:
                found = True
                print(f"Name:{item['name']} | Amount:{item['amount']} | Category:{item['category']} | Date:{item['date']}")
        if not found:
            print("Expense category not found")
            
    # HIGHEST EXPENSE
    elif choice == "10" or choice == "highest expense":
        if len(expense) == 0:
            print("No expense available")
        else:
            highest_expense = expense[0]
            for item in expense:
                amount = item["amount"]
                if amount > highest_expense["amount"]:
                    highest_expense = item
            print(f"Name:{highest_expense['name']} | Amount:{highest_expense['amount']} | Category:{highest_expense['category']} | Date:{highest_expense['date']}")
   
    # LOWEST EXPENSE
    elif choice =="11" or choice == "lowest expense":
        if len(expense) == 0:
            print("No expense available")
        else:
            lowest_expense = expense[0]
            for item in expense:
                amount = item["amount"]
                if amount < lowest_expense["amount"]:
                    lowest_expense = item                
            print(f"Name:{lowest_expense['name']} | Amount:{lowest_expense['amount']} | Category:{lowest_expense['category']} | Date:{lowest_expense['date']}")
            
    # SET BUDGET
    elif choice == "12" or choice == "set budget":
        try:
            set_budget = float(input("Enter your budget:"))
        except ValueError:
            print("Please enter a valid number")
            continue
        if set_budget <= 0:
            print("Budget must be greater than 0")
            continue
        budget = set_budget
        with open(BUDGET, "w") as f:
            json.dump(budget, f, indent = 4)
        print("Budget set successfully")
        print(f"current budget:{budget}")
        
    # CURRENT BUDGET    
    elif choice == "13" or choice == "current budget":
        total = 0
        for item in expense:
            total += item["amount"]
        if budget == 0:
            print("No budget set")
        else:
            print(f"Current budget: {budget}")
            print(f"Spent:{total}")
            remaining = budget - total
            if remaining > 0:
                print(f"Remaining:{remaining}")
            else:
                print(f"Over budget by:{-remaining}")
    
   # EXITING                                                   
    elif choice == "14" or choice == "exit":
        print("Goodbye!")      
        break         
     
    else:
        print("\nInvalid choice, please enter a valid one")
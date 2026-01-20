# Expense Tracker CLI

A simple and efficient Command Line Interface (CLI) tool to manage your personal finances. This project was developed as a solution for the [roadmap.sh](https://roadmap.sh/projects/expense-tracker) Expense Tracker challenge.

## Features

- **Add Expenses**: Track your spending with a description and amount.
- **List All Expenses**: View all your recorded transactions in a formatted table.
- **Delete Expenses**: Remove records by their unique ID.
- **Summary**: Get a total of all expenses or filter the total by a specific month.
- **Update**: Edit existing expenses easily.
- **Data Persistence**: All data is stored locally in a text file (`file.txt`).

## Requirements

- Python 3.x

## How to Install

1. Clone this repository:
   ```bash
   git clone [https://github.com/mgbrouli/Expense-Tracker.git](https://github.com/mgbrouli/Expense-Tracker.git)
Navigate to the project folder:

   ```bash
cd Expense-Tracker
Usage
Run the script using the following commands:

1. Add a new expense
   
python main.py add --description "Lunch" --amount 20
2. List all expenses


python main.py list
3. Delete an expense


python main.py remove --id 1
4. View total summary


python main.py summary
5. View summary for a specific month (e.g., August)


python main.py summary --month 8
6. Update an expense


python main.py update --id 1 --description "Groceries" --amount 50
Project Structure
main.py: The entry point of the application, handles CLI arguments using argparse.

util.py: Contains the Item class and helper functions for file manipulation (CRUD operations).

file.txt: The local database where expenses are saved.

Author
Created by mgbrouli.

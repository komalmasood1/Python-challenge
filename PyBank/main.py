import csv
file_name="03-Python_Homework_PyBank_Resources_budget_data.csv"
with open(file_name, newline='')as csvfile:
    reader = csv.reader(csvfile)

    header = next(reader)
    previous_value = next(reader)[1]
    # print(previous_value)
    profit_losses=0
    for row in reader: 
        profit_losses+= int(row[1])-int (previous_value)
        previous_value=row[1]

    print (profit_losses)
        
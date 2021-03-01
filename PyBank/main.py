import os
import csv

budgetcsv = './Resources/budget_data.csv'

with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    months = 0
    total = 0
    listofchange = []
    previousrow = 0
    counter = 1
    profitlist = []
    previousrow = 0
    date = []

    for row in csvreader:
        profit = int(row[1]) 
        months += 1 #get total number of months
        total += profit #get total profit/loss
        listofchange.append(profit) #append all numbers to list
        profitlist.append(profit - previousrow)
        previousrow = profit
        date.append(row[0])
        
    change = listofchange[-1] - listofchange[0] #number of last - number of first
    totalchange = change/(months-1) #average over 85 months
    increase = max(profitlist) #finding greatest increase and decrease in profits, use it to find the matching in index so date will match 
    increaseindex = profitlist.index(increase)
    decrease = min(profitlist)
    decreaseindex = profitlist.index(decrease)    

    print('Financial Analysis')
    print('--------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${int(total)}')
    print(f'Average Change: ${totalchange:.2f}')
    print(f'Greatest Increase in Profits: {date[increaseindex]} ${increase}')
    print(f'Greatest Decrease in Profits: {date[decreaseindex]} ${decrease}')
   

outputfile = 'Analysis/budget_data_hl.txt'

with open(outputfile, 'w') as output:
    output.write('Financial Analysis\n')
    output.write('--------------------------\n')
    output.write(f'Total Months: {months}\n')
    output.write(f'Total: ${int(total)}\n')
    output.write(f'Average Change: ${totalchange:.2f}\n')
    output.write(f'Greatest Increase in Profits: {date[increaseindex]} ${increase}\n')
    output.write(f'Greatest Decrease in Profits: {date[decreaseindex]} ${decrease}')


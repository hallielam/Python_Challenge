import os
import csv
from collections import Counter

pollcsv = 'Resources/election_data.csv'

with open(pollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    totalvotes = 0
    candidates = []
   
    for row in csvreader:
        totalvotes += 1 #count number of votes
        candidates.append(row[2])
    
    uniquenames = list(Counter(candidates).keys()) #using collections, get uniqute values and the counts of those values
    votenumber = list(Counter(candidates).values()) #cast as list so index can be accessed later


    print(uniquenames)
    print(votenumber)
    print('Election Results')
    print('--------------------')
    print(f'Total Votes: {totalvotes}')
    print('--------------------')
    for name, number in zip(uniquenames, votenumber):
        print(f'{name}: {float(number)/totalvotes *100:.3f}% ({number})')
    print('--------------------')
    mostvoted = max(votenumber)
    mostvotedindex = votenumber.index(mostvoted)
    #print(mostvoted)
    #print(mostvotedindex)
    print(f'Winner: {uniquenames[mostvotedindex]}')
    print('--------------------')

outputfile = 'Analysis/election_data_hl.txt'

with open(outputfile, 'w') as output:

    output.write('Election Results\n')
    output.write('--------------------\n')
    output.write(f'Total Votes: {totalvotes}\n')
    output.write('--------------------\n')
    for name, number in zip(uniquenames, votenumber):
        output.write(f'{name}: {float(number)/totalvotes *100:.3f}% ({number})\n')
    output.write('--------------------\n')
    mostvoted = max(votenumber)
    mostvotedindex = votenumber.index(mostvoted)
    output.write(f'Winner: {uniquenames[mostvotedindex]}\n')
    output.write('--------------------')
    
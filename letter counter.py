import csv

letters = []
count = []

for x in "abcdefghijklmnopqrstuvwxyz -'�./":
    letters.append(x)
    count.append(0)


with open("5LetterWords.csv", mode="r") as csv_file:
    csvFile = csv.reader(csv_file)

    #count the letters in the file
    for lines in csvFile:
        for x in lines[0]:
            count[letters.index(x.lower())] += 1


for inx,value in enumerate(letters):
    print(value, count[inx])






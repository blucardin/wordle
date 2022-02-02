import csv

# opening the CSV file
total_5_letter = 0
rows = []

with open("5LetterWords.csv", "w") as csv_file:
    csvwriter = csv.writer(csv_file)

    with open('dictionary.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # displaying the contents of the CSV file
        for lines in csvFile:
            if len(lines[0]) == 5:
                total_5_letter += 1
                rows.append([lines[0].replace("\"", ""), lines[1].replace("\"", ""), lines[2].replace("\"", "")])

        csvwriter.writerows(rows)

print(rows)

print("Total 5 letter words:", total_5_letter)

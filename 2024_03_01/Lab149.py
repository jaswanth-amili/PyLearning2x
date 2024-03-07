import csv

test_data = [
    ['Name',"Age","City"],
    ['Sita',"30","Chittor"],
    ['Jack',"24","Chennai"]
]


try:
    with open("mydata.csv", 'w') as file:
        writer = csv.writer(file)
        for row in writer:
            writer.writerow(row)
except FileNotFoundError as f:
    print(f)
finally:
    print("Close your files")
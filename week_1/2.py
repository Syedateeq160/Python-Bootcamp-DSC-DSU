
def recordMaker():
    numberOfRecords = int(input('Enter the number of students: '))
    print(f'Enter the {numberOfRecords} following this format! ')

    records = []

    for i in range(numberOfRecords):
        rollNumber = input("Roll number: ")
        name = input('Name: ')
        age = int(input('Age: '))
        marks = int(input('Marks: '))
        while marks > 100:
            marks = int(input("Marks cannot be greater than 100, Bitch!"))
        records.append({'RollNumber': rollNumber, 'Name': name, 'Age': age, 'Marks': marks})
        print()

    print("Results: \n")
    print("---------------------------")
    print("|R.No | Name | Age | Marks|")
    print("---------------------------")

    for i in range(numberOfRecords):
        print(records[i]["RollNumber"], end=" | ")
        print(records[i]["Name"],  end=" | ")
        print(records[i]["Age"],   end=" | ")
        print(records[i]["Marks"], end=" | \n")

    print("---------------------------")

    sumx = 0

    for i in range(numberOfRecords):
        sumx = sumx + records[i]["Marks"]

    print(f"\nAverage = {numberOfRecords}")

    marks = []

    for i in range(numberOfRecords):
        tempMarks = [records[i]["Marks"]]
        marks.append(tempMarks)

    print('\nClass Highest: ', max(marks))
    print('Class Lowest: ', min(marks))


recordMaker()

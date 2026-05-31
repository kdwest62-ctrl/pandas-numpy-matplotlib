import matplotlib.pyplot as plt
import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print("1. Statistics\n2. Average Scores\n3. Exit")
while True:
    option = input("Select option (number): ")
    if option == '1':
        print(df.to_string())
    elif option == '2':
        data = []
        students = df['student_name'].tolist()
        for student in students:
            math = df[df['student_name'] == student]['math_score'].values[0]
            english = df[df['student_name'] == student]['english_score'].values[0]
            science = df[df['student_name'] == student]['science_score'].values[0]
            history = df[df['student_name'] == student]['history_score'].values[0]
            average = (math + english + science + history) / 4
            data.append(average)
        plt.hist(data, bins=5, edgecolor='black')
        plt.title('')
        plt.xlabel('Average Scores')
        plt.ylabel('Number of Students')
        plt.show()
    elif option == '3':
        print("Program closed")
        break
    else:
        print("Option not available")

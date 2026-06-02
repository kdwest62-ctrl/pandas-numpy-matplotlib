import matplotlib.pyplot as plt
import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print("1. CSV\n2. Average Scores\n3. Bottom 5\n4. Exit")
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
        students = df['student_name'].tolist()
        math_scores = []
        english_scores = []
        science_scores = []
        history_scores = []
        for student in students:
            math = df[df['student_name'] == student]['math_score'].values[0]
            math_scores.append(math)
            english = df[df['student_name'] == student]['english_score'].values[0]
            english_scores.append(english)
            science = df[df['student_name'] == student]['science_score'].values[0]
            science_scores.append(science)
            history = df[df['student_name'] == student]['history_score'].values[0]
            history_scores.append(history)

        math_dict = dict(zip(students, math_scores))
        sorted_math = {k: v for k, v in sorted(math_dict.items(), key=lambda item: item[1])}
        sliced_math = {k: v for i, (k, v) in enumerate(sorted_math.items()) if i < 5}

        english_dict = dict(zip(students, english_scores))
        sorted_english = {k: v for k, v in sorted(english_dict.items(), key=lambda item: item[1])}
        sliced_english = {k: v for i, (k, v) in enumerate(sorted_english.items()) if i < 5}

        science_dict = dict(zip(students, science_scores))
        sorted_science = {k: v for k, v in sorted(science_dict.items(), key=lambda item: item[1])}
        sliced_science = {k: v for i, (k, v) in enumerate(sorted_science.items()) if i < 5}

        history_dict = dict(zip(students, history_scores))
        sorted_history = {k: v for k, v in sorted(history_dict.items(), key=lambda item: item[1])}
        sliced_history = {k: v for i, (k, v) in enumerate(sorted_history.items()) if i < 5}
        print("a. Math\nb. English\nc. Science\nd. History")
        subject = input("Select subject (letter): ")
        if subject == 'a':
            categories = [i for i in sliced_math.keys()]
            values = [i for i in sliced_math.values()]
            plt.bar(categories, values, color='skyblue', edgecolor='black', width=0.6)
            plt.title(f'Highest score: {max(math_dict.values())}')
            plt.xlabel('Students')
            plt.ylabel('Scores')
            plt.show()
        elif subject == 'b':
            categories = [i for i in sliced_english.keys()]
            values = [i for i in sliced_english.values()]
            plt.bar(categories, values, color='skyblue', edgecolor='black', width=0.6)
            plt.title(f'Highest score: {max(english_dict.values())}')
            plt.xlabel('Students')
            plt.ylabel('Scores')
            plt.show()
        elif subject == 'c':
            categories = [i for i in sliced_science.keys()]
            values = [i for i in sliced_science.values()]
            plt.bar(categories, values, color='skyblue', edgecolor='black', width=0.6)
            plt.title(f'Highest score: {max(science_dict.values())}')
            plt.xlabel('Students')
            plt.ylabel('Scores')
            plt.show()
        elif subject == 'd':
            categories = [i for i in sliced_history.keys()]
            values = [i for i in sliced_history.values()]
            plt.bar(categories, values, color='skyblue', edgecolor='black', width=0.6)
            plt.title(f'Highest score: {max(history_dict.values())}')
            plt.xlabel('Students')
            plt.ylabel('Scores')
            plt.show()
        else:
            print("Subject not available")
    elif option == '4':
        print("Program closed")
        break
    else:
        print("Option not available")

import matplotlib.pyplot as plt
import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
menu = ["1. CSV",
        "2. Average Scores",
        "3. Bottom 5",
        "4. Attendance vs Performance",
        "5. Score Threshold",
        "6. Exit"]
for i in menu:
    print(i)
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
        column_data = df['attendance_percent'].tolist()
        attendance = []
        for entry in column_data:
            if entry not in attendance:
                attendance.append(entry)
        performance = []
        for entry in attendance:
            if column_data.count(entry) > 1:
                attend = df[df['attendance_percent'] == entry]
                math = attend['math_score'].tolist()
                math = sum(math) / len(math)
                english = attend['english_score'].tolist()
                english = sum(english) / len(english)
                science = attend['science_score'].tolist()
                science = sum(science) / len(science)
                history = attend['history_score'].tolist()
                history = sum(history) / len(history)
                average = (math + english + science + history) / 4
                performance.append(average)
            elif column_data.count(entry) == 1:
                math = df[df['attendance_percent'] == entry]['math_score'].values[0]
                english = df[df['attendance_percent'] == entry]['english_score'].values[0]
                science = df[df['attendance_percent'] == entry]['science_score'].values[0]
                history = df[df['attendance_percent'] == entry]['history_score'].values[0]
                average = (math + english + science + history) / 4
                performance.append(average)
        reference = dict(zip(attendance, performance))
        sorted_ref = {key: reference[key] for key in sorted(reference)}
        x = [k for k in sorted_ref.keys()]
        y = [v for v in sorted_ref.values()]
        plt.plot(x, y)
        plt.title("Attendance vs Performance")
        plt.xlabel("Attendance (%)")
        plt.ylabel("Average Performance")
        plt.show()
    elif option == '5':
        def over(d, baseline):
            count = 0
            for e in d:
                if e >= baseline:
                    count += 1
            return count
        def equal(d, baseline):
            count = 0
            for e in d:
                if e == baseline:
                    count += 1
            return count
        def under(d, baseline):
            count = 0
            for e in d:
                if e < baseline:
                    count += 1
            return count
        def chart(statistics, baseline, names):
            plt.pie(statistics, labels=names)
            plt.title(f'Score Threshold: {baseline}')
            plt.show()
        subject = input("Subject: ")
        if subject in ['math', 'english', 'science', 'history']:
            if subject == 'math':
                threshold = int(input("Score threshold: "))
                math_score = df['math_score'].tolist()
                success = over(math_score, threshold)
                average = equal(math_score, threshold)
                failed = under(math_score, threshold)
                stats = [success, average, failed]
                label = ['Over', 'Equal', 'Under']
                chart(stats, threshold, label)
            elif subject == 'english':
                threshold = int(input("Score threshold: "))
                english_score = df['english_score'].tolist()
                success = over(english_score, threshold)
                average = equal(english_score, threshold)
                failed = under(english_score, threshold)
                stats = [success, average, failed]
                label = ['Over', 'Equal', 'Under']
                chart(stats, threshold, label)
            elif subject == 'science':
                threshold = int(input("Score threshold: "))
                science_score = df['science_score'].tolist()
                success = over(science_score, threshold)
                average = equal(science_score, threshold)
                failed = under(science_score, threshold)
                stats = [success, average, failed]
                label = ['Over', 'Equal', 'Under']
                chart(stats, threshold, label)
            elif subject == 'history':
                threshold = int(input("Score threshold: "))
                history_score = df['history_score'].tolist()
                success = over(history_score, threshold)
                average = equal(history_score, threshold)
                failed = under(history_score, threshold)
                stats = [success, average, failed]
                label = ['Over', 'Equal', 'Under']
                chart(stats, threshold, label)
        else:
            print("Subject not in list")
    elif option == '6':
        print("Program closed")
        break
    else:
        print("Option not available")

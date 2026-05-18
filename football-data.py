import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

path = Path(input("CSV path: "))
if 'football_data' in path.name:
    df = pd.read_csv(path)
    df['Goals_For'] = df['Goals_For'].astype('Int64')
    df['Goals_Against'] = df['Goals_Against'].astype('Int64')
    scored = df['Goals_For'].sum()
    conceded = df['Goals_Against'].sum()
    played = df['Result (W/L/D)'].count()
    results = df['Result (W/L/D)'].tolist()
    print("Options")
    print("1. Statistics\n2. Analysis\n3. Charts\n4. Simulate\n5. Exit")
    while True:
        choice = input("Select option (num): ")
        if choice == '1':
            print(df.to_string())
        elif choice == '2':
            pass
        elif choice == '3':
            print("a. Results\nb. Cumulative Goal Difference\nc. Home vs Away Performance\nd. Season Form")
            chart = input("Select chart (letter): ")
            if chart == 'a':
                a = [results.count('W'), results.count('L'), results.count('D')]
                labels = ['W', 'L', 'D']
                plt.pie(a, labels=labels)
                plt.show()
            elif chart == 'b':
                x = df['Match_Number'].tolist()
                y1 = np.array(df['Goal_Difference'].tolist())
                y = np.cumsum(y1)
                plt.plot(x, y, color="orange", marker="+")
                plt.title("Cumulative Goal Difference")
                plt.xlabel("Match Number")
                plt.ylabel("Goal Difference")
                plt.show()
            elif chart == 'c':
                home_matches = df[df['Home/Away'] == 'H']
                home_results_list = home_matches['Result (W/L/D)'].tolist()
                away_matches = df[df['Home/Away'] == 'A']
                away_results_list = away_matches['Result (W/L/D)'].tolist()
                fig, (ax1, ax2) = plt.subplots(1, 2)
                ax1.bar(['W', 'L', 'D'],
                        [home_results_list.count('W'), home_results_list.count('L'), home_results_list.count('D')])
                ax1.set_title('First Plot')
                ax2.bar(['W', 'L', 'D'],
                        [away_results_list.count('W'), away_results_list.count('L'), away_results_list.count('D')])
                ax2.set_title('Second Plot')
                plt.ylim(top=max(home_results_list.count('W'), home_results_list.count('L'), home_results_list.count('D')))
                plt.tight_layout()
                plt.show()
            elif chart == 'd':
                y = df['Result (W/L/D)'].tolist()
                x = df['Match_Number'].tolist()
                plt.plot(x, y, color="blue", markersize=10,
                         marker=".", markerfacecolor="cyan")
                plt.title("Form Guide")
                plt.xlabel("Match Number")
                plt.ylabel("Result (W/L/D)")
                plt.gca().invert_yaxis()
                plt.show()
            else:
                print("Chart not available")
        elif choice == '4':
            results = df['Result (W/L/D)'].tolist()
            fixtures = input("Fixtures (example = HHA): ")
            letters = []
            for item in fixtures:
                if item in ['H', 'A']:
                    letters.append(item)
            print(letters)

            home_matches = df[df['Home/Away'] == 'H']
            home_goals_for = home_matches['Goals_For'].tolist()
            home_goals_against = home_matches['Goals_Against'].tolist()
            away_matches = df[df['Home/Away'] == 'A']
            away_goals_for = away_matches['Goals_For'].tolist()
            away_goals_against = away_matches['Goals_Against'].tolist()

            def get_nums(data):
                output = []
                for entry in data:
                    if entry not in output:
                        output.append(int(entry))
                return output
            def get_prob(data, num_list):
                prob_per_num = []
                for number in num_list:
                    p = data.count(number)
                    w = len(data)
                    per = p / w
                    prob_per_num.append(per)
                return prob_per_num

            scores = []
            for item in letters:
                res = []
                if item == 'H':
                    a = get_nums(home_goals_for)
                    b = get_prob(home_goals_for, a)
                    gf = np.random.choice(a, p=b)
                    a = get_nums(home_goals_against)
                    b = get_prob(home_goals_against, a)
                    ga = np.random.choice(a, p=b)
                    res.append(gf)
                    res.append(ga)
                    scores.append(res)
                elif item == 'A':
                    a = get_nums(away_goals_for)
                    b = get_prob(away_goals_for, a)
                    gf = np.random.choice(a, p=b)
                    a = get_nums(away_goals_against)
                    b = get_prob(away_goals_against, a)
                    ga = np.random.choice(a, p=b)
                    res.append(gf)
                    res.append(ga)
                    scores.append(res)
            print(scores)

            goals_for = []
            goals_against = []
            for item in scores:
                goals_for.append(item[0])
                goals_against.append(item[1])

            result = []
            for item in scores:
                if item[0] > item[1]:
                    result.append('W')
                elif item[0] < item[1]:
                    result.append('L')
                elif item[0] == item[1]:
                    result.append('D')
            print(result)
        elif choice == '5':
            break
        else:
            print("Option not available")
else:
    print("Wrong CSV")

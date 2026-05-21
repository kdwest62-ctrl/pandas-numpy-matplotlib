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
    home_matches = df[df['Home/Away'] == 'H']
    home_goals_for = home_matches['Goals_For'].tolist()
    home_goals_against = home_matches['Goals_Against'].tolist()
    home_goal_diff = home_matches['Goal_Difference'].tolist()
    home_results = home_matches['Result (W/L/D)'].tolist()
    home_points = home_results.count('W') * 3 + home_results.count('D') * 1
    total_home_goals_for = sum(home_goals_for)
    total_home_goals_against = sum(home_goals_against)
    total_home_goal_diff = sum(home_goal_diff)

    away_matches = df[df['Home/Away'] == 'A']
    away_goals_for = away_matches['Goals_For'].tolist()
    away_goals_against = away_matches['Goals_Against'].tolist()
    away_goal_diff = away_matches['Goal_Difference'].tolist()
    away_results = away_matches['Result (W/L/D)'].tolist()
    away_points = away_results.count('W') * 3 + away_results.count('D') * 1
    total_away_goals_for = sum(away_goals_for)
    total_away_goals_against = sum(away_goals_against)
    total_away_goal_diff = sum(away_goal_diff)

    matches_played = len(home_results) + len(away_results)
    total_points = home_points + away_points
    points_per_match = total_points / matches_played
    total_goals_for = total_home_goals_for + total_away_goals_for
    total_goals_against = total_home_goals_against + total_away_goals_against
    total_goal_diff = total_home_goal_diff + total_away_goal_diff
    print("Options")
    print("1. Statistics\n2. Analysis\n3. Charts\n4. Simulate\n5. Exit")
    while True:
        choice = input("Select option (num): ")
        if choice == '1':
            print(df.to_string())
        elif choice == '2':
            print(f"Matches played: {len(results)}")
            print(f"Home matches: {len(home_matches)}")
            print(f"Away matches: {len(away_matches)}")
            print(f"Record (W/L/D): {results.count('W')}-{results.count('L')}-{results.count('D')}")
            print(f"Home record: {home_results.count('W')}-{home_results.count('L')}-{home_results.count('D')}")
            print(f"Away record: {away_results.count('W')}-{away_results.count('L')}-{away_results.count('D')}")
            data = {'': ['Goals For', 'Goals Against', 'Goal Difference', 'Points'],
                    'Season (total)': [total_goals_for, total_goals_against, total_goal_diff, total_points],
                    'Home (total)': [total_home_goals_for, total_home_goals_against, total_home_goal_diff, home_points],
                    'Away (total)': [total_away_goals_for, total_away_goals_against, total_away_goal_diff, away_points],
                    'Season (average)': list(map(lambda n: n / len(results),
                                                 [total_goals_for, total_goals_against, total_goal_diff, total_points])),
                    'Home (average)': list(map(lambda n: n / len(results),
                                               [total_home_goals_for, total_home_goals_against, total_home_goal_diff, home_points])),
                    'Away (average)': list(map(lambda n: n / len(results),
                                               [total_away_goals_for, total_away_goals_against, total_away_goal_diff, away_points]))}
            df = pd.DataFrame(data)
            print(df.to_string())
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
                fig, (ax1, ax2) = plt.subplots(1, 2)
                ax1.bar(['W', 'L', 'D'],
                        [home_results.count('W'), home_results.count('L'), home_results.count('D')])
                ax1.set_title('First Plot')
                ax2.bar(['W', 'L', 'D'],
                        [away_results.count('W'), away_results.count('L'), away_results.count('D')])
                ax2.set_title('Second Plot')
                plt.ylim(top=max(home_results.count('W'), home_results.count('L'), home_results.count('D')))
                plt.tight_layout()
                plt.show()
            elif chart == 'd':
                y = df['Result (W/L/D)'].tolist()
                x = df['Match_Number'].tolist()
                plt.plot(x, y, color="red", markersize=10,
                         marker=".", markerfacecolor="orange", linewidth=1, markeredgecolor="red")
                plt.title("Form Guide")
                plt.xlabel("Match Number")
                plt.ylabel("Result (W/L/D)")
                plt.gca().invert_yaxis()
                plt.show()
            else:
                print("Chart not available")
        elif choice == '4':
            def get_nums(d):
                nums = []
                for entry in d:
                    if entry not in nums:
                        nums.append(int(entry))
                return nums
            def get_prob(d, num_list):
                percentages = []
                for num in num_list:
                    part = d.count(num)
                    whole = len(d)
                    percent = part / whole
                    percentages.append(percent)
                return percentages

            played = len(home_matches) + len(away_matches)
            print(f"Matches played: {played}")
            schedule = input("Input schedule (H/A): ")
            count = 0
            for match in schedule:
                if match not in ['H', 'A']:
                    count += 1
            if count == 0:
                scores = []
                for match in schedule:
                    res = []
                    if match == 'H':
                        choices = get_nums(home_goals_for)
                        probability = get_prob(home_goals_for, choices)
                        gf = np.random.choice(choices, p=probability)
                        choices = get_nums(home_goals_against)
                        probability = get_prob(home_goals_against, choices)
                        ga = np.random.choice(choices, p=probability)
                        res.append(gf)
                        res.append(ga)
                        scores.append(res)
                    elif match == 'A':
                        choices = get_nums(away_goals_for)
                        probability = get_prob(away_goals_for, choices)
                        gf = np.random.choice(choices, p=probability)
                        choices = get_nums(away_goals_against)
                        probability = get_prob(away_goals_against, choices)
                        ga = np.random.choice(choices, p=probability)
                        res.append(gf)
                        res.append(ga)
                        scores.append(res)

                goals_for = []
                goals_against = []
                results = []
                for score in scores:
                    goals_for.append(score[0])
                    goals_against.append(score[1])
                    if score[0] > score[1]:
                        results.append('W')
                    elif score[0] < score[1]:
                        results.append('L')
                    elif score[0] == score[1]:
                        results.append('D')

                data = {'Home/Away': [i for i in schedule],
                        'Goals_For': [i for i in goals_for],
                        'Goals_Against': [i for i in goals_against],
                        'Results (W/L/D)': [i for i in results]}
                df = pd.DataFrame(data)
                print(df.to_string())
            else:
                print("Invalid input detected! Matches must only be H or A")
        elif choice == '5':
            break
        else:
            print("Option not available")
else:
    print("Wrong CSV")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = input("CSV path: ")
df = pd.read_csv(path)
df['Goals_For'] = df['Goals_For'].astype('Int64')
df['Goals_Against'] = df['Goals_Against'].astype('Int64')
scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
played = df['Result (W/L/D)'].count()
results = df['Result (W/L/D)'].tolist()
print("Options")
print("1. Show CSV\n2. Statistical Analysis\n3. Charts\n4. Simulate remaining matches\n5. Exit")
while True:
    choice = input("Select option (num): ")
    if choice == '1':
        print(df.to_string())
    elif choice == '2':
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

        print(f"Matches played: {len(results)}")
        print(f"Record (W/L/D): {results.count('W')}-{results.count('L')}-{results.count('D')}")
        print(f"Home record: {home_results.count('W')}-{home_results.count('L')}-{home_results.count('D')}")
        print(f"Away record: {away_results.count('W')}-{away_results.count('L')}-{away_results.count('D')}")
        data = {'Data': ['Goals For', 'Goals Against', 'Goal Difference', 'Points'],
                'Season (total)': [total_goals_for, total_goals_against, total_goal_diff, total_points],
                'Home (total)': [total_home_goals_for, total_home_goals_against, total_home_goal_diff, home_points],
                'Away (total)': [total_away_goals_for, total_away_goals_against, total_away_goal_diff, away_points],
                'Season (average)': list(map(lambda n: n / len(results),
                                             [total_goals_for, total_goals_against, total_goal_diff, total_points])),
                'Home (average)': [total_home_goals_for / 25, total_home_goals_against / 25, total_home_goal_diff / 25,
                                   home_points / 25],
                'Away (average)': [total_away_goals_for / 25, total_away_goals_against / 25, total_away_goal_diff / 25,
                                   away_points / 25]}
        df = pd.DataFrame(data)
        print(df.to_string())
    elif choice == '3':
        print("a. Results\nb. Cumulative goal difference\nc. Home vs Away performance\nd. Season form guide")
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
        pass
    elif choice == '5':
        break
    else:
        print("Option not available")

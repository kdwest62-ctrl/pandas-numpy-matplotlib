import pandas as pd

path = input("CSV file: ")
df = pd.read_csv(path)
scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
played = df['Result (W/L/D)'].count()
remain = df['Result (W/L/D)'].isna().sum()
print(f"Matches played: {played} | remaining: {remain}")
print(f"Goals scored: {int(scored)} | average: {scored / played}")
print(f"Goals conceded: {int(conceded)} | average: {conceded / played}")
print(f"Goal difference: {int(scored - conceded)}")

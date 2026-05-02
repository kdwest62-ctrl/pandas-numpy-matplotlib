import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
played = df['Goals_For'].count()
print(f"Goals scored: {int(scored)}")
print(f"Average goals scored: {scored / played}")
print(f"Goals conceded: {int(conceded)}")
print(f"Average goals conceded: {conceded / played}")
print(f"Goal difference: {int(scored - conceded)}")

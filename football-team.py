import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
scored = df['Goals_For'].sum()
conceded = df['Goals_Against'].sum()
print(f"Goals scored: {int(scored)}")
print(f"Goals conceded: {int(conceded)}")
print(f"Goal difference: {int(scored - conceded)}")

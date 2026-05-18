import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print("1. Statistics\n2. Class Performance Heatmap\n3. Exit")
while True:
    option = input("Select option (number): ")
    if option == '1':
        print(df.to_string())
    elif option == '2':
        print("a. Students vs Subjects\nb. Performance Matrices\nc. Normalized Score")
        chart = input("Select chart (letter): ")
        if chart == 'a':
            pass
        elif chart == 'b':
            pass
        elif chart == 'c':
            pass
        else:
            print("Chart not available")
    elif option == '3':
        break
    else:
        print("Option not available")

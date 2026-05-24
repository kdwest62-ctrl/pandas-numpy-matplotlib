import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print("Options")
options = ["1. CSV",
           "2. Units Sold + Sales",
           "3. Top 3 Products",
           "4. Customer Segmentation",
           "5. Moving Average",
           "6. Exit"]
for option in options:
    print(option)
while True:
    select = input("Select option (number): ")
    if select == '1':
        print(df.to_string())
    elif select == '2':
        print("a. Product\nb. Category\nc. Region")
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            pass
        elif choice == 'b':
            pass
        elif choice == 'c':
            pass
        else:
            print("Choice not available")
    elif select == '3':
        pass
    elif select == '4':
        print("a. Purchase Frequency\nb. Favorite Product\nc. Favorite Category")
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            pass
        elif choice == 'b':
            pass
        elif choice == 'c':
            pass
        else:
            print("Choice not available")
    elif select == '5':
        pass
    elif select == '6':
        print("Program closed")
        break
    else:
        print("Option not available")

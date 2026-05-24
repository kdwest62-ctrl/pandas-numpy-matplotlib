import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print("Options")
options = ["1. CSV",
           "2. Engagement Stats",
           "3. Reach Stats",
           "4. 7-Day Trend of Average Likes",
           "5. Exit"]
for option in options:
    print(option)
while True:
    select = input("Select option (number): ")
    if select == '1':
        print(df.to_string())
    elif select == '2':
        stats = ["a. Platform",
                 "b. Content Type",
                 "c. Weighted Score",
                 "d. Engagement by Hour",
                 "e. Weekday vs Weekend"]
        for stat in stats:
            print(stat)
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            ig = df[df['platform'] == 'Instagram']
            ig_likes = ig['likes'].tolist()
            ig_shares = ig['shares'].tolist()
            ig_comments = ig['comments'].tolist()

            fb = df[df['platform'] == 'Facebook']
            fb_likes = fb['likes'].tolist()
            fb_shares = fb['shares'].tolist()
            fb_comments = fb['comments'].tolist()

            twt = df[df['platform'] == 'Twitter']
            twt_likes = twt['likes'].tolist()
            twt_shares = twt['shares'].tolist()
            twt_comments = twt['comments'].tolist()

            data = {'platform': ['Instagram', 'Facebook', 'Twitter'],
                    'likes': [sum(ig_likes), sum(fb_likes), sum(twt_likes)],
                    'shares': [sum(ig_shares), sum(fb_shares), sum(twt_shares)],
                    'comments': [sum(ig_comments), sum(fb_comments), sum(twt_comments)]}
            df = pd.DataFrame(data)
            print(df.to_string())
        elif choice == 'b':
            pass
        elif choice == 'c':
            pass
        elif choice == 'd':
            pass
        elif choice == 'e':
            pass
        else:
            print("Choice not available")
    elif select == '3':
        print("a. Platform\nb. Content Type")
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            pass
        elif choice == 'b':
            pass
        else:
            print("Choice not available")
    elif select == '4':
        pass
    elif select == '5':
        print("Program closed")
        break
    else:
        print("Option not available")

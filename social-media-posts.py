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
            img = df[df['content_type'] == 'Image']
            img_likes = img['likes'].tolist()
            img_shares = img['shares'].tolist()
            img_comments = img['comments'].tolist()

            vid = df[df['content_type'] == 'Video']
            vid_likes = vid['likes'].tolist()
            vid_shares = vid['shares'].tolist()
            vid_comments = vid['comments'].tolist()

            txt = df[df['content_type'] == 'Text']
            txt_likes = txt['likes'].tolist()
            txt_shares = txt['shares'].tolist()
            txt_comments = txt['comments'].tolist()

            link_likes = df[df['content_type'] == 'Link']['likes'].values[0]
            link_shares = df[df['content_type'] == 'Link']['shares'].values[0]
            link_comments = df[df['content_type'] == 'Link']['comments'].values[0]

            reel_likes = df[df['content_type'] == 'Reel']['likes'].values[0]
            reel_shares = df[df['content_type'] == 'Reel']['shares'].values[0]
            reel_comments = df[df['content_type'] == 'Reel']['comments'].values[0]

            carousel_likes = df[df['content_type'] == 'Carousel']['likes'].values[0]
            carousel_shares = df[df['content_type'] == 'Carousel']['shares'].values[0]
            carousel_comments = df[df['content_type'] == 'Carousel']['comments'].values[0]

            data = {'content_type': ['Image', 'Video', 'Text', 'Link', 'Reel', 'Carousel'],
                    'likes': [sum(img_likes), sum(vid_likes), sum(txt_likes), link_likes, reel_likes, carousel_likes],
                    'shares': [sum(img_shares), sum(vid_shares), sum(txt_shares), link_shares, reel_shares,
                               carousel_shares],
                    'comments': [sum(img_comments), sum(vid_comments), sum(txt_comments), link_comments, reel_comments,
                                 carousel_comments]}
            df = pd.DataFrame(data)
            print(df.to_string())
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

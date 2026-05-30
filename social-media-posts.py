import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
ig = df[df['platform'] == 'Instagram']
ig_likes = ig['likes'].tolist()
ig_shares = ig['shares'].tolist()
ig_comments = ig['comments'].tolist()
ig_reach = ig['reach'].tolist()

fb = df[df['platform'] == 'Facebook']
fb_likes = fb['likes'].tolist()
fb_shares = fb['shares'].tolist()
fb_comments = fb['comments'].tolist()
fb_reach = fb['reach'].tolist()

twt = df[df['platform'] == 'Twitter']
twt_likes = twt['likes'].tolist()
twt_shares = twt['shares'].tolist()
twt_comments = twt['comments'].tolist()
twt_reach = twt['reach'].tolist()

img = df[df['content_type'] == 'Image']
img_likes = img['likes'].tolist()
img_shares = img['shares'].tolist()
img_comments = img['comments'].tolist()
img_reach = img['reach'].tolist()

vid = df[df['content_type'] == 'Video']
vid_likes = vid['likes'].tolist()
vid_shares = vid['shares'].tolist()
vid_comments = vid['comments'].tolist()
vid_reach = vid['reach'].tolist()

txt = df[df['content_type'] == 'Text']
txt_likes = txt['likes'].tolist()
txt_shares = txt['shares'].tolist()
txt_comments = txt['comments'].tolist()
txt_reach = txt['reach'].tolist()

link_likes = df[df['content_type'] == 'Link']['likes'].values[0]
link_shares = df[df['content_type'] == 'Link']['shares'].values[0]
link_comments = df[df['content_type'] == 'Link']['comments'].values[0]
link_reach = df[df['content_type'] == 'Link']['reach'].values[0]

reel_likes = df[df['content_type'] == 'Reel']['likes'].values[0]
reel_shares = df[df['content_type'] == 'Reel']['shares'].values[0]
reel_comments = df[df['content_type'] == 'Reel']['comments'].values[0]
reel_reach = df[df['content_type'] == 'Reel']['reach'].values[0]

carousel_likes = df[df['content_type'] == 'Carousel']['likes'].values[0]
carousel_shares = df[df['content_type'] == 'Carousel']['shares'].values[0]
carousel_comments = df[df['content_type'] == 'Carousel']['comments'].values[0]
carousel_reach = df[df['content_type'] == 'Carousel']['reach'].values[0]
while True:
    select = input("Select option (number): ")
    if select == '1':
        print(df.to_string())
    elif select == '2':
        print("a. Platform | b. Content Type | c. Weighted Score | d. Engagement by Time | e. Weekday vs Weekend")
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            data = {'platform': ['Instagram', 'Facebook', 'Twitter'],
                    'likes': [sum(ig_likes), sum(fb_likes), sum(twt_likes)],
                    'shares': [sum(ig_shares), sum(fb_shares), sum(twt_shares)],
                    'comments': [sum(ig_comments), sum(fb_comments), sum(twt_comments)]}
            engage_pl = pd.DataFrame(data)
            print(engage_pl.to_string())
        elif choice == 'b':
            data = {'content_type': ['Image', 'Video', 'Text', 'Link', 'Reel', 'Carousel'],
                    'likes': [sum(img_likes), sum(vid_likes), sum(txt_likes), link_likes, reel_likes, carousel_likes],
                    'shares': [sum(img_shares), sum(vid_shares), sum(txt_shares), link_shares, reel_shares,
                               carousel_shares],
                    'comments': [sum(img_comments), sum(vid_comments), sum(txt_comments), link_comments, reel_comments,
                                 carousel_comments]}
            engage_ct = pd.DataFrame(data)
            print(engage_ct.to_string())
        elif choice == 'c':
            post_id = df['post_id'].tolist()
            for post in post_id:
                likes = df[df['post_id'] == post]['likes'].values[0]
                shares = df[df['post_id'] == post]['shares'].values[0]
                comments = df[df['post_id'] == post]['comments'].values[0]
                scores = np.array([likes, shares, comments])
                weights = np.array([0.2, 0.3, 0.5])
                weighted_score = np.average(scores, weights=weights)
                print(f"Post ID: {post}, Weighted Score: {weighted_score}")
        elif choice == 'd':
            time_list = df['post_time'].tolist()
            new_list = []
            for time in time_list:
                if time[0] == '0':
                    new_time = f'{time[1]}{time[3]}{time[4]}'
                    new_list.append(int(new_time))
                else:
                    new_time = f'{time[0]}{time[1]}{time[3]}{time[4]}'
                    new_list.append(int(new_time))
            new_list.sort()
            final_list = []
            for time in new_list:
                time = str(time)
                if len(time) == 3:
                    final_time = f'0{time[0]}:{time[1]}{time[2]}'
                    final_list.append(final_time)
                elif len(time) > 3:
                    final_time = f'{time[0]}{time[1]}:{time[2]}{time[3]}'
                    final_list.append(final_time)
            engagements = []
            for item in final_list:
                if final_list.count(item) > 1:
                    hour = df[df['post_time'] == item]
                    likes = hour['likes'].tolist()
                    shares = hour['shares'].tolist()
                    comments = hour['comments'].tolist()
                    total = likes + shares + comments
                    engagements.append(total)
                elif final_list.count(item) == 1:
                    likes = df[df['post_time'] == item]['likes'].values[0]
                    shares = df[df['post_time'] == item]['shares'].values[0]
                    comments = df[df['post_time'] == item]['comments'].values[0]
                    total = likes + shares + comments
                    engagements.append(total)
            plt.bar(final_list, engagements, color='skyblue')
            plt.xlabel('Time')
            plt.ylabel('Engagements')
            plt.title('Engagement by Time')
            plt.show()
        elif choice == 'e':
            pass
        else:
            print("Choice not available")
    elif select == '3':
        print("a. Platform | b. Content Type")
        choice = input("Choose stat (letter): ")
        if choice == 'a':
            data = {'platform': ['Instagram', 'Facebook', 'Twitter'],
                    'reach': [sum(ig_reach), sum(fb_reach), sum(twt_reach)]}
            reach_pl = pd.DataFrame(data)
            print(reach_pl.to_string())
        elif choice == 'b':
            data = {'content_type': ['Image', 'Video', 'Text', 'Link', 'Reel', 'Carousel'],
                    'reach': [sum(img_reach), sum(vid_reach), sum(txt_reach), link_reach, reel_reach, carousel_reach]}
            reach_ct = pd.DataFrame(data)
            print(reach_ct.to_string())
        else:
            print("Choice not available")
    elif select == '4':
        pass
    elif select == '5':
        print("Program closed")
        break
    else:
        print("Option not available")

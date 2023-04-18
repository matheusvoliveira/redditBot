import praw
import config
import time
import os
import requests


def bot_login():
    print('logging in...')
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Deaf comment bot v0.1")
    print('logged in!')

    return r


def run_bot(r, comments_replied_to):
    print('Obtaining comments...')

    for comment in r.subreddit('all').stream.comments(skip_existing=True):
        if 'dog' in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            response = response.json()
            dog_pic = response['message']

            comment.reply('I like dogs too! [Here]({}) is a picture!'.format(dog_pic))

            print("Replied to comment\n" + comment.body)

            comments_replied_to.append(comment.id)

        with open("comments_replied_to.txt", 'a') as f:
            f.write(comment.id + "\n")

    print("Sleeping...")
    time.sleep(1)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
# print (comments_replied_to)

while True:
    run_bot(r, comments_replied_to)

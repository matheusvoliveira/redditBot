import os.path

import praw
import config
import time


def bot_login() :
    print('Logging in...')
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Tricky_Calendar8130's dog comment responder v.01")
    print('Logged in...')
    return r


def run_bot(r, comment_replied_to):
    print('obtaining 25 comments...')

    for comment in r.subreddit('test').comments(limit=10):
        if 'dog' in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print('string with dog found in comment ' + comment.id)
            comment.reply(
                "I also love dogs [Here](https://imgur.com/t/dogs/eGW8k7B) is a image of one!")
            print('Replied to comment ' + comment.id)

            comments_replied_to.append(comment.id)

            with open("comments_replied_to.txt", "a"):
                f.write(comment.id + "\n")
      # print('Sleeping for 10 seconds')
        # sleep for ten seconds
       # time.sleep(10) ya quisere


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")

    return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)
while True:
    run_bot(r, comments_replied_to)

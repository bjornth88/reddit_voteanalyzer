import praw

#https://www.reddit.com/r/news/comments/66vktb/california_doctors_pharmacists_charged_in_40/.json

redditPraw = praw.Reddit(client_id='q7T2U9MmTN7Hhg',client_secret="tHlNFNeHxXNI37te4JAI4MqsAhA",password='jingerpen',user_agent="testbot by Bjorn /u/bot_bear",username='bot_bear')
for submission in redditPraw.subreddit('TrueReddit').hot(limit=10):
    print(submission.title)
    print(submission.score)
    print(submission.author)
    print(submission.created)
    print(submission.url)
    print('upvotes: ' + str(submission.ups))
    print('downvotes: ' + str(submission.downs))
    #print('upvote ratio: ' + str(submission.upvote_ratio))

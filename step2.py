import twitter_pb2
from operator import itemgetter

tweets = twitter_pb2.Tweets()
f = open("twitter.pb", "rb")
tweets.ParseFromString(f.read())
f.close()

deleted_count = 0
reply_count = 0
top5 = {}
for tweet in tweets.tweets:
    if tweet.is_delete == True:
        deleted_count += 1
    if tweet.insert.reply_to != 0:
        reply_count += 1
    uid = tweet.insert.uid
    if uid in top5:
        top5[uid] += 1
    elif uid == 0:
        continue
    else:
        top5[uid] = 1

# Question 1 - Find the number of deleted messages in the dataset.
print "Q1: Deleted message count: ", deleted_count
# Answer: Q1: Deleted message count:  1554

# Question 2 - Find the number of tweets that are replies to another tweet.
print "Q2: Reply message count: ", reply_count
# Answer: Q2: Reply message count:  2531

# Question 3 - Find the five user IDs (field name: uid) that have tweeted the most.
print dict(sorted(top5.iteritems(), key=itemgetter(1), reverse=True)[:5])
# Answer: {1471774728L: 2, 424808364L: 3, 392695315L: 4, 1269521828L: 5, 1706901902L: 3}
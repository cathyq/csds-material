-- Q1. Find the number of deleted messages in the dataset.
select count (*) from tweets where is_delete=1;
-- Find the number of tweets that are replies to another tweet.
select count(*) from tweets where reply_to !=0 and reply_to NOT NULL;
-- Find the five user IDs (field name: uid) that have tweeted the most.
select uid, count(*) from tweets where is_delete = 0 group by uid order by count(*) desc limit 5;

// Q1. Find the number of deleted messages in the dataset.
db.tweets.count({ "delete" : {$exists: true, $ne: null }})

// Q2. Find the number of tweets that are replies to another tweet.
db.tweets.count({ "in_reply_to_status_id" : {$exists: true, $ne: null}})

// Q3. Find the five user IDs (field name: uid) that have tweeted the most.
db.tweets.aggregate([
	{ $project: {user_id: "$user.id"}},
   	{ $group: {_id: "$user_id", count: { $sum: 1}}},
    { $sort: {count: -1}},
    { $match: {_id: {$ne: null}}},
    { $limit: 5}
]);

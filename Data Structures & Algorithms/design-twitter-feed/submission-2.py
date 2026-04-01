class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweet_map[userId][:]
        for followee_id in self.follow_map[userId]:
            feed.extend(self.tweet_map[followee_id])
        feed.sort(key=lambda x:-x[0])
        return [tweet_id for _,tweet_id in feed[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        

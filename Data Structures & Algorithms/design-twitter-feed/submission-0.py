import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.userFollowing = {}
        self.userTweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        self.userTweets[userId].append((self.time, tweetId))
        self.time = self.time + 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # ADDED: the people whose tweets we want = who we follow + ourselves
        people = set(self.userFollowing.get(userId, set()))
        people.add(userId)

        news = []
        for f in people:                                    # CHANGED: loop over `people`
            if f in self.userTweets:                        # CHANGED: added the missing colon
                idx = len(self.userTweets[f]) - 1           # CHANGED: index of their newest tweet
                count, tweetId = self.userTweets[f][idx]
                # CHANGED: one tuple inside append(...), negative time for a min-heap
                news.append((-count, tweetId, f, idx))

        heapq.heapify(news)
        res = []

        while news and len(res) < 10:                       # CHANGED: was `for i in range(10)`
            negCount, tweetId, followeeId, idx = heapq.heappop(news)
            res.append(tweetId)

            # CHANGED: push this person's next OLDER tweet, only if one exists
            if idx - 1 >= 0:
                t, nextTweetId = self.userTweets[followeeId][idx - 1]
                heapq.heappush(news, (-t, nextTweetId, followeeId, idx - 1))

        return res                                          # ADDED: was missing

    def follow(self, followerId, followeeId):
        if followerId not in self.userFollowing:
            self.userFollowing[followerId] = set()
        self.userFollowing[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.userFollowing:
            self.userFollowing[followerId].discard(followeeId)   # CHANGED: discard, not remove
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


reddit = praw.Reddit(
    client_id='...',
    client_secret='...',
    user_agent='...',
)


subreddit = reddit.subreddit('SubName')


sia = SentimentIntensityAnalyzer()


comments = subreddit.comments(limit=1000)


positive_count = 0
negative_count = 0
neutral_count = 0


for comment in comments:
    sentiment_score = sia.polarity_scores(comment.body)
    if sentiment_score['compound'] > 0.05: 
        positive_count += 1
    elif sentiment_score['compound'] < -0.05: 
        negative_count += 1
    else: 
        neutral_count += 1


labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive_count, negative_count, neutral_count]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0) 

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title(f'Sentiment Distribution in r/{subreddit.display_name}')
plt.show()

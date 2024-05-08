import praw
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id='...',
    client_secret='...',
    user_agent='...',
)

subreddit = reddit.subreddit('SubName')

comments = subreddit.comments(limit=1000)

text = ""
for comment in comments:
    text += comment.body + " "

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

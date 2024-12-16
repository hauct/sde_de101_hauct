# social_etl.py
# for complete code check out https://github.com/josephmachado/socialetl
import praw
import os
import sqlite3

REDDIT_CLIENT_ID=''
REDDIT_CLIENT_SECRET=''
REDDIT_USER_AGENT=''

def extract():
    client = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
    )
    subreddit = client.subreddit('dataengineering')
    top_subreddit = subreddit.hot(limit=100)
    data = []
    for submission in top_subreddit:
        data.append(
            {
                'title': submission.title,
                'score': submission.score,
                'id': submission.id,
                'url': submission.url,
                'comments': submission.num_comments,
                'created': submission.created,
                'text': submission.selftext,
            }
        )
    return data


def transform(data):
    """
    Function to only keep outliers.
    Outliers are based on num of comments > 2 standard deviations from mean
    """
    num_comments = [post.get('comments') for post in data]

    mean_num_comments = sum(num_comments) / len(num_comments)
    std_num_comments = (
        sum([(x - mean_num_comments) ** 2 for x in num_comments])
        / len(num_comments)
    ) ** 0.5
    return [
        post
        for post in data
        if post.get('comments') > mean_num_comments + 2 * std_num_comments
    ]


def load(data):
    # create a db connection
    if not os.path.exists('./data'):
        os.makedirs('./data')  # Tạo thư mục nếu chưa tồn tại
    conn = sqlite3.connect('./data/socialetl.db')
    cur = conn.cursor()
    try:
        # create table if it doesn't exist
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS social_posts (
                id TEXT PRIMARY KEY,
                score INTEGER,
                social_data TEXT
            )
            """
        )
        # insert data into DB
        for post in data:
            cur.execute(
                """
                    INSERT INTO social_posts (
                        id, score, social_data
                    ) VALUES (
                        :id, :score, :social_data
                    )
                    """,
                {
                    'id': post.get('id'),
                    'score': post.get('score'),
                    'social_data': str(
                        {
                            'title': post.get('title'),
                            'url': post.get('url'),
                            'comments': post.get('comments'),  # sửa từ num_comments thành comments
                            'created': post.get('created'),
                            'text': post.get('text'),  # sửa từ selftext thành text
                        }
                    ),
                },
            )
    finally:
        conn.commit()
        conn.close()


def main():
    # pull data from Reddit
    data = extract()
    # transform reddit data
    transformed_data = transform(data)
    # load data into database
    load(transformed_data)
    
if __name__ == '__main__':
    main()
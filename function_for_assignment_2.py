"""Template code from the assignment."""

# Imports
import csv
from datetime import datetime

# Read the data from CSV file
replika_comments = []
with open('r-replika-comment.csv', encoding='utf-8') as csvfile:
    reddit_comment_reader = csv.DictReader(csvfile)
    for comment in reddit_comment_reader:
        creation_timestamp = int(comment['created_utc'])
        comment['created'] = datetime.fromtimestamp(creation_timestamp)
        replika_comments.append(comment)

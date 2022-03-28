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

def group_comments(comments):
    """Group comments by their OP."""
    grouping = {}
    for comment in comments:
        permalink_split = comment['permalink'].split('/')
        op_title = permalink_split[5]
        if op_title in grouping:
            grouping[op_title].append(comment)
        else:
            grouping[op_title] = [comment]
    return grouping

def count_comments(comments):
    groupings = group_comments(comments)
    counts = groupings.copy()
    for op_title in groupings:
        counts[op_title] = len(counts[op_title])
    return counts

def weekend_comments(comments):
    """Return list of comments posted during the weekend."""
    we_comments = []
    for comment in comments:
        if comment['created'].weekday() >= 5:
            we_comments.append(comment)
    return we_comments

def print_comment_bodies(comments):
    for comment in comments:
        body = comment['body'].replace('\n', ' ')
        print(f"💬 {body}")

print_comment_bodies(replika_comments)

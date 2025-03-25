
# Fetch data from multiple API endpoints 

# (https://jsonplaceholder.typicode.com/users, 
#  https://jsonplaceholder.typicode.com/posts, and 
#  https://jsonplaceholder.typicode.com/comments). 
# For each user, calculate the total number of comments on their posts and output the result.


import requests
 
users_url = "https://jsonplaceholder.typicode.com/users"
posts_url = "https://jsonplaceholder.typicode.com/posts" 
comments_url = "https://jsonplaceholder.typicode.com/comments" 

users = requests.get(users_url).json() 
posts = requests.get(posts_url).json() 
comments = requests.get(comments_url).json() 

user_dict = {user["id"]: user["name"] for user in users} 
 
post_user_map = {post["id"]: post["userId"] for post in posts} 

user_comment_count = {user["id"]: 0 for user in users} 
for comment in comments: 
    post_id = comment["postId"] 
    if post_id in post_user_map: 
        user_id = post_user_map[post_id] 
        user_comment_count[user_id] += 1 


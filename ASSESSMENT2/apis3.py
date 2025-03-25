import requests

posts_url = 'https://jsonplaceholder.typicode.com/posts'
posts_response = requests.get(posts_url) 
posts = posts_response.json()

for post in posts: 
    post_id = post['id'] 
    post_title = post['title'] 
    
    comments_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    comments_response = requests.get(comments_url) 
    comments = comments_response.json() 
    commenter_names = [comment['name'] for comment in comments] 
    print(f"Post ID: {post_id}, Title: {post_title}") 
    print("Commenter Names:") 
    for name in commenter_names: 
        print(f"- {name}") 
        print("\n")
import requests

# GET Request
get_response = requests.get("https://jsonplaceholder.typicode.com/posts")
print("GET Response:")
print(get_response.json())  # This should print a list of posts
# GET Request
get_response = requests.get("https://jsonplaceholder.typicode.com/posts")
print("GET Response:")
print(get_response.json())  # This should print a list of posts

# POST Request
# post_data = {"title": "foo", "body": "bar", "userId": 1}
# post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
# print("\nPOST Response:")
# print(post_response.json())  # This should print the newly created post


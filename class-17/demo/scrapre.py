import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.reddit.com/'

page = requests.get(URL)
# print(page)
# print(page.content)

# conver from byte tp html
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

all_posts = soup.find_all('div', class_='_1oQyIsiPHYt6nx7VOmd1sz')
# print(all_posts)

posts_list = []
# for post in all_posts:

#     title = post.find('h3',class_='_eYtD2XCVieq6emjKBH3m').text.strip()
#     comments = post.find('span',class_='FHCV02u6Cp2zYL0fhQPsO').text.strip()
#     votes = post.find('div',class_='_1rZYMD_4xY3gRcSS3p8ODO').text.strip()

#     post_obj = {
#         'title' : title,
#         'comments' : comments,
#         'votes' : votes
#     }

#     posts_list.append(post_obj)

# print(posts_list)

def cleaner(post):

    title = post.find('h3',class_='_eYtD2XCVieq6emjKBH3m').text.strip()
    comments = post.find('span',class_='FHCV02u6Cp2zYL0fhQPsO').text.strip()
    votes = post.find('div',class_='_1rZYMD_4xY3gRcSS3p8ODO').text.strip()

    return {
        'title' : title,
        'comments' : comments,
        'votes' : votes
    }

# list comprehension
posts_list = [cleaner(post) for post in all_posts]



# convert to json
json_posts = json.dumps(posts_list)

with open('posts.json', 'w') as file:
    file.write(json_posts)




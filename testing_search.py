# import requests
# import os
# import json
# from dotenv import load_dotenv


# load_dotenv()
# SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
# GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']


# # def background():
# search_query = "dogs"

# url = "https://www.googleapis.com/customsearch/v1"

# params = {
#     "q": search_query,
#     "key": GOOGLE_API_KEY,
#     "cx": SEARCH_ENGINE_ID,
#     "searchType": "image"
# }

# response = requests.get(url, params=params)
# # print(response.text)
# # data = response.json()

# data = response.json()['items']
# # if data['total_results'] > 0:
# #     return data['photos'][0]['src']['original']

# # print(data)

# if data:
#     print(data[0]['link'])
# # for item in data:
# #     print(item['link'])
# # if "items" in data:
# #     print(data['items'][0]['link'])  


# # print(background())
# # background()
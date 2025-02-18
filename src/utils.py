import requests #import requests module to call API

# Set up API authentification to be able to make API calls
BEARER_TOKEN = "YOUR_BEARER_TOKEN"

#urls to fetch user data and tweets from twitter
USER_LOOKUP_URL = "https://api.twitter.com/2/users/by/username/{}?user.fields=id"
TWEETS_URL = "https://api.twitter.com/2/users/{}/tweets?tweet.fields=public_metrics,entities"

def get_user_id(username):
    #Fetches the Twitter user ID for a given username
    url = USER_LOOKUP_URL.format(username)
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    #make API request
    response = requests.get(url, headers=headers)
    
    #check if API request was successful
    if response.status_code == 200:
        return response.json().get("data", {}).get("id")
    else:
        print("Error fetching user ID:", response.status_code, response.text)
        return None #if not successful stop executing

def get_tweets(user_id):
    #Fetches recent tweets from a Twitter user by ID
    url = TWEETS_URL.format(user_id)
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

    response = requests.get(url, headers=headers) #make API request

    if response.status_code == 200: #check if request was successful 
        return response.json().get("data", []) #return list of tweets
    else: #print error message if request is unsuccessful
        print("Error fetching tweets:", response.status_code, response.text)
        return []

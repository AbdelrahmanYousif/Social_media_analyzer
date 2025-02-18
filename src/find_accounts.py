from utils import get_user_id, get_tweets #import necessary functions from utils.py to fetch user id and tweets

# Predefined top accounts for different industries
INDUSTRY_ACCOUNTS = {
    "marketing": "HubSpot",
    "restaurants": "McDonalds",
    "fitness": "Nike"
}

def get_best_tweet(industry):
    """Finds the best-performing tweet for a given industry."""
    if industry not in INDUSTRY_ACCOUNTS:
        print(f"No accounts found for industry: {industry}")
        return None #check if industry is in our dictionary if it isn't stop execution

    username = INDUSTRY_ACCOUNTS[industry] #get industry twitter username
    user_id = get_user_id(username) #fetch user ID
    
    if not user_id:
        print(f"Could not retrieve user ID for {username}")
        return None #if user id is not found stop execution

    tweets = get_tweets(user_id) #check if there are recent tweets on user ID

    if not tweets:
        print(f"No tweets found for {username}")
        return None #if no tweets are found stop execution

    # Find the tweet with the most likes
    best_tweet = max(tweets, key=lambda t: t.get("public_metrics", {}).get("like_count", 0))

    return best_tweet #return tweet with best best engagement

if __name__ == "__main__": #run code only if ran directly 
    industry = input("Enter an industry (marketing/restaurants/fitness): ").lower() #ask user for industry
    best_tweet = get_best_tweet(industry) #call function to find best performing tweets

    if best_tweet: #display tweet if found
        print(f"Best tweet: {best_tweet['text']}")
        print(f"Likes: {best_tweet['public_metrics']['like_count']}")

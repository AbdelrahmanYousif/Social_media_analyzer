from utils import get_user_id, get_tweets #import necessary modules from utils.py file

def analyze_engagement(industry):
    """Analyzes the engagement (likes, retweets, replies) of an industry's top account."""
    user_id = get_user_id(industry) #get Twitter user id from given industry
    
    if not user_id:
        print("Could not retrieve user ID.")
        return None #stop execution if user ID is not found

    tweets = get_tweets(user_id) #fetch recent tweets from user ID

    if not tweets:
        print("No tweets found.")
        return None #stop executing if no tweets are found

    #Calculate engagement
    total_likes = sum(tweet["public_metrics"].get("like_count", 0) for tweet in tweets)
    total_retweets = sum(tweet["public_metrics"].get("retweet_count", 0) for tweet in tweets)
    total_replies = sum(tweet["public_metrics"].get("reply_count", 0) for tweet in tweets)

    #Present engagement
    print(f"Engagement analysis for {industry}:")
    print(f"- Total Likes: {total_likes}")
    print(f"- Total Retweets: {total_retweets}")
    print(f"- Total Replies: {total_replies}")

    #Return engagement data as a dictionary, useful for further analysis
    return {"likes": total_likes, "retweets": total_retweets, "replies": total_replies}

if __name__ == "__main__": #onle execute script if it is ran directly
    industry = input("Enter an industry: ").lower() #ask user for an industry
    analyze_engagement(industry) #call function to analyze engagement

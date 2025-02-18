# 📊 Social Media Analyzer

## Overview
Social Media Analyzer is a Python application designed to analyze Twitter engagement.  
It performs the following tasks:
- **Fetches top competitor tweets** for specific industries (marketing, restaurants, fitness).
- **Identifies the best-performing tweet** based on engagement metrics (likes, retweets, replies).
- **Analyzes overall engagement** across tweets from the selected industry account.

This project demonstrates key course topics such as API integration, JSON handling, error handling, file organization, unit testing, and version control.

---

## Dependencies
This project requires:
- **Python 3.x**
- External libraries: `requests` and `pytest`

These dependencies are listed in the `requirements.txt` file.

To install the dependencies, run:
```bash
pip install -r requirements.txt
## 🚀 How to Run the Application

### 1️⃣ **Set Up Twitter API Access**
- Go to the [Twitter Developer Portal](https://developer.twitter.com/) and create an API key.
- Open the file **`src/utils.py`** and replace `"YOUR_BEARER_TOKEN"` with your actual API token.

---

### 2️⃣ **Run the Application**
This project has **two main functionalities:**

#### 🔹 **Find the Best-Performing Tweet**
- This functionality retrieves recent tweets from a competitor's account and finds the tweet with the most likes.  
- To run it, use:
  ```bash
  python src/find_accounts.py

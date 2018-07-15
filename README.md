# Lazy100
![Logo](/Images/Logo.png)

A CLI to automate **#100DaysOfX Challenges** that will `commit` your work to your github account and also `tweet` your progress to your twitter account. <br>


There are two mode of it's operation:
- Automatic


![Lazy100-Auto](https://raw.githubusercontent.com/bksahu/Lazy100/master/Images/lazy100DemoAuto.gif)

**NOTE:** Your progress must be saved in a directory named in this form: `Day. LessonName`. Example: `1. Linear Regression`

- Manual


![Lazy100-Auto](https://raw.githubusercontent.com/bksahu/Lazy100/master/Images/Lazy100DemoManual.gif)


## Installation

1. Run this command to install required modules:
  `pip install -r requirements.txt`

2. Put `Lazy100.py` in your **100DaysOfX** directory.

3. Add `Lazy100.py` to .gitignore (optional)

## Create your Twitter app

This repo uses [tweepy](https://github.com/tweepy/tweepy) to interact with Twitter. To use it, you will need to create a new Twitter app and insert those credentials into `Lazy100.py`.

1. Log into twitter
1. Browse to [https://apps.twitter.com/](https://apps.twitter.com/)
1. Click the `Create New App` button and define your new app. Here are some example values:
    * **Name**: `Lazy100 - <your name>`
    * **Description**: `I'm Lazy`
    * **Website**: `<link to your repo>`
    * **Callback URLs**: `` <= blank
1. Check the **Developer Agreement** and click the `Create your Twitter application` button.
1. In the application details page, Select the "Keys and Access Tokens" tab.
1. Under "Your Access Token", click the `Create my access token` button.

See the [tweepy tutorial](http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html) for more information, if needed.

## Insert your credentials
Open `Lazy100.py` and insert your credentials:

```python
##############################################################
link_to_repo = '' # Set your github repo name

## Check README.md to learn how to acquire your Twitter keys
consumer_key = '' # Put your twitter consumer key
consumer_secret = '' # Put your twitter consumer secret
access_token = '' # Put your twitter access token
access_token_secret = '' # Put your twitter access token secret
###############################################################
```
## Running

Execute in either ways:<br>
    - Automatic: `python Lazy100.py`<br>
    - Manual: `python Lazy100.py -c="Your git commit message" -t="Your tweet message"`<br>
    
**NOTE 1:** If `$ git push` asks for both username & password every time then, check out [this](https://stackoverflow.com/questions/11403407/git-asks-for-username-every-time-i-push) tutorial.<br>
**NOTE 2:** If you are using automatic way then, your progress must be saved in a directory named in this form: `Day. LessonName`.<br> Example: `1. Linear Regression`

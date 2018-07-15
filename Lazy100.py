'''


 ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄    ▄▄▄▄      ▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌ ▄█░░░░▌    ▐░░░░░░░░░▌  ▐░░░░░░░░░▌
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░░▌▐░░▌   ▐░█░█▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌          ▐░▌▐░▌       ▐░▌ ▀▀ ▐░░▌   ▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌    ▐░░▌   ▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▌   ▐░▌
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌    ▐░░▌   ▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌
▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀     ▐░░▌   ▐░▌   ▐░▌ ▐░▌▐░▌   ▐░▌ ▐░▌
▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌         ▐░░▌   ▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▄▄▄▄█░░█▄▄▄▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄█░█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░▌  ▐░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀      ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀

A CLI to automate #100DaysOfX Challenges.

Author: bksahu <bablusahoo16@gmail.com>
'''
print(__doc__)

import subprocess
import inspect, glob
import os, re
import tweepy
import time, argparse

##############################################################
link_to_repo = '' # Set your github repo name

## Check README.md to learn how to acquire your Twitter keys
consumer_key = '' # Put your twitter consumer key
consumer_secret = '' # Put your twitter consumer secret
access_token = '' # Put your twitter access token
access_token_secret = '' # Put your twitter access token secret
###############################################################


def get_cwd():
    """Return the pathname of the Git Repository.
       Make sure this script is kept in same git repo.
    """
    # get this script's name
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    # get it's path
    path = os.path.dirname(os.path.abspath(filename))
    return path

def execute(*arg):
    """Return the stdout_data and executes the command.

     Example
     -------
     >>> sys.stdout.write(execute('git', 'status'))
     On branch master
     Your branch is up to date with 'origin/master'.

     Changes not staged for commit:
       (use "git add/rm <file>..." to update what will be committed)
       (use "git checkout -- <file>..." to discard changes in working directory)
     ...
    """
    PIPE = subprocess.PIPE

    try:
        status = subprocess.Popen([*arg], stdout=PIPE, stderr=PIPE)
        stdout_data, stderr_data = status.communicate()
    except subprocess.CalledProcessError as e:
        print(e.output)

    return stdout_data

def get_message(link_to_repo=''):
    """Return the commit message and tweet
    [Note]: To this work the dir name must be in the form of `Day. LessonName`. Example: `1. Linear Regression`
    """
    # get the name of second latest dir created. (First latest dir being created is .git)
    latestDir = sorted(glob.glob(os.path.join('.', '*/')), key=os.path.getmtime)[-1]

    # get the day
    day = re.split(r'\W+', latestDir)[1]

    # get the lesson name
    lessonName = ''
    for idx, word in enumerate(re.split(r'\W+', latestDir)):
        if idx > 1:
            lessonName += word + ' '

    # Set git commit message. Eg: Day 1 - Linear Regression added
    commitMessage = 'Day ' + day + ' - ' + lessonName + 'added'
    # Set git tweet message. Eg: Day 1 - Linear Regression completed of #100daysofMLcode www.yourRepoLink.com
    tweetMessage = 'Day ' + day + ' - ' + lessonName + 'completed of #100DaysOfMLcode ' + link_to_repo

    return commitMessage, tweetMessage

def git_operation(commitMessage):
    """Return status and execute git operations in order.
    """
    # Check if it is a git repo or not. If not then exit script
    status = execute('git', 'status')
    if status == b'':
        print('fatal: not a git repository (or any of the parent directories): .git\nPut this script inside your Repo')
        # Delay for 2 sec
        time.sleep(2)
        quit()

    # git pull
    print('Executing git pull...', end=' ')
    execute('git', 'pull')
    print('Done')

    # git add *
    print('Executing git add --all...', end=' ')
    execute('git', 'add', '.')
    print('Done')

    # git commit
    print('Executing git commit -m...', end=' ')
    execute('git', 'commit', '-m', commitMessage)
    print('Done')

    # git push
    print('Executing git push...', end=' ')
    execute('git', 'push')
    print('Done')

def tweet(tweetMessage):
    """Return status and tweet
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print('Tweeting...', end=' ')
    api = tweepy.API(auth)
    api.update_status(status = tweetMessage)
    print('Done')

if __name__ == "__main__":

    # Set path to repo
    os.chdir(get_cwd())

    # Define argparse
    parser = argparse.ArgumentParser(description='A CLI tool to automate #100DaysOfX challenge.')
    parser.add_argument('-m','--commit', help='Commit message', required=False)
    parser.add_argument('-t','--tweet', help='Tweet message', required=False)
    args = vars(parser.parse_args())

    if args['commit'] and args['tweet'] is not None:
        print('Commit Message: ', args['commit'])
        print('Tweet Message: ', args['tweet'])
        choice = input("Is it correct [y/n] ?\n>> ")
        if choice == 'y':
            # retrive the commit message and tweet from args
            commitMessage = args['commit']
            tweetMessage = args['tweet']
        else:
            commitMessage = input('Commit Message: ')
            tweetMessage = input('Commit Message: ')
    else:
        commitMessage, tweetMessage = get_message(link_to_repo)

    # Do the git operation
    git_operation(commitMessage)

    # Tweet
    tweet(tweetMessage)

    # Delay for 2 sec
    time.sleep(2)

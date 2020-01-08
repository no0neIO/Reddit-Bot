import praw

# reddit api login put your details here
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    password='',
    username='',
    user_agent='')

print(reddit.user.me())

# the subreddit(s) the bot live
subreddit = reddit.subreddit('')

# phrase to activate the bot
keyphrase = '!onelineof '

# look for phrase and reply appropriately
for comment in subreddit.stream.comments(skip_existing=True):
    if (keyphrase in comment.body) and (comment.author.name != 'yournamehere'):
        word = comment.body.replace(keyphrase, '')
        print(word)
        try:
            if word == 'contact':
                # get meaning as object, get the index of a sentence and
                reply = 'https://onelineof.me'
                comment.reply(word + ': ' + reply)
                print(' POSTED: ' + word)
            elif word == 'help':
                reply = '!onelineof command\n\n\'contact\' : epistrefei ta stoixeia epikoinwnias mou\n\n\'help\' : diathesimes entoles'
                comment.reply(reply)
                print(reply)
            else:
                reply = 'den anagnwrizete i entoli'+word
                comment.reply(reply)
                print('POSTED den anagnwrisa entoli' + word)
        except:
            print('to frequent')

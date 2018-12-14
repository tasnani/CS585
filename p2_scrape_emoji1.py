import emoji
import os 

#Input One tweet file
#Output emoji tweet file and label file
input_directory = './app_data/topic_tweets'
output_directory = './app_data/tweets_emojis'
filename = 'ireland_tweets.txt'

positiveEmojis = ['👍','😊','😆','😄','⭐','😁', '😇','♥', '🙏','💖','😃','😆','🤑','🥂', '😛','👍', '👋', '😍','💖','🌚','🙌', '🗳', '🙋','👏','💜','😊','❤', '😀', '💕', '✅', '☘',
                 '💚', '✨','💘', '😉', '👐','🤗', '😂','🤣','🤗', '😏','💓', '💝', '💟','👼', '🎶', '🌈', '🐣', '✌', '👌',
                 '😃','🎉','🤝', '🖤','😘','🖐', '❣', '😙', '💃','😄','😆','💙','😎','😁','💞','💛', '💗',
                 '🤓','😋', '😜','🙂','✔','🌻','☺', '🤙','🌸','🌺','☘','🌟','😺','😌','😹','🎈', '😚','👯','💍', '👰',
                 '😻','😇','☝', '🐥', '🍻', '🥇','💸','🎓','😛', '😝', '🌷','😸','🌼', '🎂', '🎁','🏆','🏅','💐', '🤸',
                 '🍾', '😳','🍺','💌','🌝','🤕','🤒','😺','💯','😋','🍻','😻']
negativeEmojis = ['😠', '😦','😔','😐','😑','😨','😖','🚫','😩','☹','😪','😣','😦','🤐','😾','😒','😫','😟', '💔','🙁','😧','👹','🚨','🙃','🙄','😱','😡', '😢','😥','🤦','😞','☠', '💀','😬','😣','😭', '😑','😠','😓',
                 '😷', '👎', '🖐','😕','😖','😔', '😯','😶','🙀', '😨','☹', '🖕','🔥','😤','😲','😰','😕', '✋',
                 '👹', '⬇', '🤚','❎','🤢','😐','👿','😈','🤐','😪','✖','🙁', '😵','🤧','🤥', '😮', '👺','⚠', '😟','🤕',
                 '😫','🤒','🐍','💣','😿', '🎊','🥀','😷','😶']

def text_has_emoji(file, input_directory, output_directory):
    #Get tweets
    with open(input_directory + "/" + file, encoding="utf-8") as f:
        content = f.readlines()
        content = [x.strip() for x in content]  
    data_file = open(output_directory + '/' + file.split('.')[0] + ' Emoji.txt', "w+", encoding="utf-8")
    label_file = open(output_directory + '_labels/' + file.split('.')[0] + ' Labels.txt', "w+", encoding="utf-8")
    #Looking each line/tweet in content  
    for text in content:
        sentiment_count=0
        #Sum positive/negative emojis for sentiment label
        for character in text:
            if character in positiveEmojis:
                sentiment_count += 1
            if character in negativeEmojis:
                sentiment_count -=1
        #Write to Data/Label files if sentimental tweet
        if(sentiment_count > 0):
            data_file.write(text+"\n")
            label_file.write('Positive\n')
        elif(sentiment_count < 0):
            data_file.write(text+"\n")
            label_file.write('Negative\n')
    return str(file)

text_has_emoji(filename, input_directory, output_directory)










'''
emojiLabels={}

notEmojis = ['\U0001f9d0','\U0001f92e','\U0001f92f','\U0001f9e1','\U0001f92c','\U0001f92a','\U0001f91f','\U0001f928',
               '\U0001f92b','\U0001f929','\U0001f931','\U0001f6f8','\U0001f92d','\U0001f9da','\U0001f995','\U0001f9e0',
               '\U0001f9d1','\U0001f9d8', '\U0001f96a', '\U0001f96b','\U0001f9d9','\U0001f9d5','\U0001f9dd','\U0001f996']

#Write to /...tweetsCopy.txt only if in emoji.UNICODE and not in notEmoji
def text_has_emoji(text):
    emojiExists=False
    #emojiLabels dictionary with keys as emojis found    
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            if character not in notEmojis:
                emojiExists=True
                if character not in emojiLabels:
                    emojiLabels[character]=''
    if(emojiExists==True):
        d.write(text)
        d.write('\n')
    return emojiLabels
 
d = open(output_tweet_file, "w+",  encoding="utf-8")
with open(input_tweet_file,  encoding="utf-8") as f:
    content = f.readlines()
content = [x.strip() for x in content]     
    
for c in content:
    text_has_emoji(c)

 
positiveEmojis = ['👍','😊','😆','😄','⭐','😁', '😇','♥', '🙏','💖','😃','😆','🤑','🥂', '😛','👍', '👋', '😍','💖','🌚','🙌', '🗳', '🙋','👏','💜','😊','❤', '😀', '💕', '✅', '☘',
                 '💚', '✨','💘', '😉', '👐','🤗', '😂','🤣','🤗', '😏','💓', '💝', '💟','👼', '🎶', '🌈', '🐣', '✌', '👌',
                 '😃','🎉','🤝', '🖤','😘','🖐', '❣', '😙', '💃','😄','😆','💙','😎','😁','💞','💛', '💗',
                 '🤓','😋', '😜','🙂','✔','🌻','☺', '🤙','🌸','🌺','☘','🌟','😺','😌','😹','🎈', '😚','👯','💍', '👰',
                 '😻','😇','☝', '🐥', '🍻', '🥇','💸','🎓','😛', '😝', '🌷','😸','🌼', '🎂', '🎁','🏆','🏅','💐', '🤸',
                 '🍾', '😳','🍺','💌','🌝','🤕','🤒','😺','💯','😋','🍻','😻']
negativeEmojis = ['😠', '😦','😔','😐','😑','😨','😖','🚫','😩','☹','😪','😣','😦','🤐','😾','😒','😫','😟', '💔','🙁','😧','👹','🚨','🙃','🙄','😱','😡', '😢','😥','🤦','😞','☠', '💀','😬','😣','😭', '😑','😠','😓',
                 '😷', '👎', '🖐','😕','😖','😔', '😯','😶','🙀', '😨','☹', '🖕','🔥','😤','😲','😰','😕', '✋',
                 '👹', '⬇', '🤚','❎','🤢','😐','👿','😈','🤐','😪','✖','🙁', '😵','🤧','🤥', '😮', '👺','⚠', '😟','🤕',
                 '😫','🤒','🐍','💣','😿', '🎊','🥀','😷','😶']


#emojiLabels: Keys are emojis found, values are corresponding sentiment
for key in emojiLabels.keys():
    if key in positiveEmojis:
        emojiLabels[key]='Positive'
    elif key in negativeEmojis:
        emojiLabels[key]='Negative'

#tweetAndLabel: Keys are document/tweet strings, values are corresponding label
with open(output_tweet_file,  encoding="utf-8") as m:
        content = m.readlines()
content = [x.strip() for x in content]

tweetAndLabel={}

#Only assign tweets with negative/positive emojis to tweetAndLabel
for c in content:
    for character in c:
        if character in emoji.UNICODE_EMOJI:
            if character not in notEmojis:
                if emojiLabels[character]=='Positive':
                    tweetAndLabel[c]='Positive'
                elif emojiLabels[character]=='Negative':
                    tweetAndLabel[c]='Negative'

n = open('./app_data/brexit/brexit_labels.txt', "w+",  encoding="utf-8")
z = open('./app_data/brexit/brexit_data.txt', "w+",  encoding="utf-8")

for x in tweetAndLabel:
    n.write(tweetAndLabel[x] + "\n")
    z.write(x + "\n")
'''
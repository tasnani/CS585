import emoji
import os 

#Take all tweet files in input directory
#Make emoji tweet files in output directory
#Make emoji label files in output directory2

input_directory = './app_data/tweets'
output_directory = './app_data/tweets_emojis'

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

for filename in os.listdir(input_directory):
    if filename.endswith(".txt"): 
        text_has_emoji(filename, input_directory, output_directory)

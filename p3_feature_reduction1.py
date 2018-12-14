import emoji
import re
import os

##### Description
# Input: Directory containing one tweet emoji files
# Purpose: Use regex matching to replace query terms, emojis, repeated letters, usernames, and URLs 
# Output: Generates one processed tweet emoji file
# Settings: query term


#Directory Paths
filename = "ireland_tweets data.txt"
input_directory = './app_data/tweets_emojis'
output_directory = './app_data/tweets_emojis_processed'
#Query List. Optionally add query_list =  ['\S*{}\S*'.format(query) for query in query_list]
query_list  = ["ireland"]
#Emoji List
emoji_list = emoji.UNICODE_EMOJI.keys()
emoji_list = sorted(emoji_list, key=len, reverse=True)
emoji_list = map(re.escape, emoji_list)

#\S: nonwhitespace, (): capture, \1: match first capture, *: 0 or more prev element, +: 1 or more prev element, []: shorthand OR, {2,}: repeat prev 2 or more, \w: any letter
url_reg = re.compile(r'\S*(https|www)\S*', re.IGNORECASE)
username_reg = re.compile(r'\S*@\S+')
repeat_reg = re.compile(r'(\w)\1{2,}')
#Create Emoji/Query regex, re.escape function to match string literally, even if contains regex. 'string'.join(list) to concatenate 'string' between every element. (?: is for noncapturing group
query_reg = re.compile(r'({})'.format('|'.join(query_list)), re.IGNORECASE)
emoji_reg = re.compile(r'({})'.format('|'.join(emoji_list)))


def feature_reduction(_filename, _input_directory, _output_directory):
    #Full intput/output filepaths
    input_file = _input_directory + "/" + _filename
    output_file = _output_directory + "/" + _filename.split('.')[0] + "2.txt"
    #Load in entire file as single string
    with open(input_file, encoding="utf-8") as f:
        content = f.read()
    #Use regex objects to substitute terms
    content = emoji_reg.sub('', content)
    content = query_reg.sub('QUERY_TERM', content)
    content = url_reg.sub('URL_TERM', content)
    content = username_reg.sub('USERNAME_TERM', content)
    content = repeat_reg.sub(r'\1\1', content)
    #Write to processed data file
    with open(output_file, "w+",  encoding="utf-8") as f:
        f.write(content)
        
#Do only one file
feature_reduction(filename, input_directory, output_directory)



#emoji_test =  'efef👩\u200d❤️\u200d💋\u200d👨 fehiofhif feoifh 👨💋 efefef 👨\u200d👨\u200d👦\u200d👦efef \n'
#url_test = "I love you (https:/feoihfeih) https:efhioeihf www.bob.com bobbbb \n"
#query_test = "Brexit filfeBrexit bbbBrexit feoifhe brexitww\n"
#username_test = "@harmon @fefe @ fff@feoihfoie\n"
#repeat_test = 'I lOOOve pieeeeeee mmmmmmmdd\n'


import os
import re

temp_reg = re.compile(r'labels')

input_directory= './app_data/tweets_emojis_labels'
#For all tweet data files in directory
for filename in os.listdir(input_directory):
    filename2 = temp_reg.sub('Labels', filename)
    os.rename(input_directory + '/' + filename, input_directory + '/' + filename2)

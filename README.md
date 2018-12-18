To run the project: 
1) Install sci-kit learn
2) The datasets are required. Clone the repository from https://github.com/tasnani/CS585.git
3) Run load_dictionary.py from the directory folder CS585 of the cloned repository

Functions of each script:

app.py- to retrieve actual tweets based on Tweet ID using the Twitter API for political topic datasets found online

classify_main.py- Sample classifier for Brexit tweets using Naive Bayes and Bag of Words approach. 

get_timeline.py- to get tweet timelines of various politicians 

load_dictionary.py- produce all 3 sentiment classification models- logistic regression, support vector machine and naive bayes across all topics to be applied on all politicians' tweets on various topics and count a positive or negative sentiment score for each topic for each politician. Aggregate sentiment on all topics for each politician to predict if they have more liberal or conservative views(democrat vs. republican). Use DW_NOMINATE score to compare with our prediction if a politician is a democrat or republican(evaluation).

p1_app.py- to retrieve actual tweets based on Tweet ID using the Twitter API for political topic datasets found online, different version

p2_scrape_emoji1.py- scrape tweets with emojis in them and assign them a 'positive' or 'negative' sentiment label

p2_scrape_emoji2.py- scrape tweets with emojis in them and assign them a 'positive' or 'negative' sentiment label, different version

p3_feature_reduction1.py- perform feature reduction i.e reduce vocabulary: strip out usernames, URLs and keywords of the topic

p3_feature_reduction2.py- perform feature reduction i.e reduce vocabulary: strip out usernames, URLs and keywords of the topic, different version

p4_split_data.py- create test/train data splits

p5_sentiment_experiments.py- script to perform different sentiment classification experiments, i.e one classifer over all topics, each topic having its own classifier, classification over unseen topics not trained on

polititians.py- create a dictionary holding political topics as keys and all politicians' tweets on that topic as values stored in a tuple

search_tweets_by_keyword.py- retrieve tweets from Twitter on other political topics using the Twitter API

temp.py- renaming label files

app_data folder - contains datafiles for this project

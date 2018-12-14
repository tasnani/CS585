import os
import h5py as h5
import numpy as np
from sklearn.model_selection import train_test_split

dir_emoji = './app_data/tweets_emojis'
dir_emoji2 = './app_data/tweets_emojis_processed'
dir_labels = './app_data/tweets_emojis_labels'
dir_workspace = './app_data/model_workspace'
h5_path = dir_workspace + '/dataset.hdf5'

query_list = [  
    "Affirmative Action", "DACA immigration" , 
    "Assisted Suicide", "Capital punishment", 
    "labor unions", "vaccines", "concealed weapons", 
    "self-driving cars","Artificial intelligence", 
    "Donald Trump","Planned Parenthood", "Social Security", "NRA", 
    "Fracking", "Nuclear Energy", "NSA Surveillance", "Military Spending", 
    "Foreign Aid", "Dakota Access Pipeline", "Oil Drilling", "Paris Climate Agreement", 
    "Trans Pacific Partnership", "China Tariffs", "Labor Unions", 
    "Universal Basic Income", "Paid Sick Leave", "Safe Haven", "Medicaid", 
    "Edward Snowden", "Whistleblower Protection", "Armed Teachers", "Gun Control",
    "In-State Tuition", "Immigration Ban", "Border Wall", "First Amendment", 
    "Confederate Flag", "Death Penalty", "Religious Freedom Act",
    "Obamacare", "Marijuana"
    ]
query_list2 = ["brexit_tweets", "ferguson_tweets", "travel_ban_tweets", "trump_tweets", "ireland_tweets"]
query_list.extend(query_list2)


#Write train/test data/label in subgroup of hdf5 file
def write_to_h5(h5_path, X, y, test_size=0.25, shuffle=False, sub_group = None):
    assert(len(X) == len(y))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=shuffle)
    with h5.File(h5_path, "a") as f:
        dt = h5.special_dtype(vlen=bytes)
        f.create_dataset(sub_group + "/X_train", data = [n.encode("ascii", "ignore") for n in X_train], dtype = dt)
        f.create_dataset(sub_group + "/X_test", data = [n.encode("ascii", "ignore") for n in X_test], dtype=dt)
        f.create_dataset(sub_group + "/y_train", data = [n.encode("ascii", "ignore") for n in y_train] , dtype=dt)
        f.create_dataset(sub_group + "/y_test", data = [n.encode("ascii", "ignore") for n in y_test], dtype=dt)
        
#Write to new subgroup for each query_term
for query in query_list:
    data_path = (dir_emoji2 + '/' + query + ' Emoji2.txt')
    label_path = (dir_labels + '/' + query + ' Labels.txt')
    if(not(os.path.exists(data_path) and os.path.exists(data_path))):
        continue
    with open(data_path, "r",  encoding="utf-8") as f:
        data = [x.strip() for x in f.readlines()]
    with open(label_path, "r",  encoding="utf-8") as f:
        labels = [x.strip() for x in f.readlines()]
    if(len(data) == len(labels)):
        write_to_h5(h5_path, data, labels, sub_group=query)
    

#For all tweet data files in directory
#files_found = os.listdir(input_directory)
#Does any query_list 
#anymatch = lambda x: any([query in x for query in query_list])
#files_match = filter(lambda x: any( [ query_list ]))


#Experiment 1 - Separate data into topics. Train one classifier for each topic set. Test classifier on that same data set
    
'''
Brexit
Ferguson
Ireland
Donald Trump
Travel Ban

Naive Bayes
SVM
Logistic Regression
Deep Averaging Network
'''

#Experiment 2 - Combine all tweets from all topics into one set. Train one classifier over all topics. Test each classifier on data from individual topics.

'''
Brexit
Ferguson
Ireland
Donald Trump
Travel Ban
Combined Test Set

Naive Bayes
SVM
Logistic Regression
Deep Averaging Network
'''
#Experiment 3 - Use the four classifiers trained in experiment 2. Test accuracy on topics it has never seen before (tweets with topics it wasn’t trained on)

'''

Obamacare
Net Neutrality
Gay Marriage
Affirmative Action
Concealed Weapons
Combined Test Set


Naive Bayes
SVM
Logistic Regression
Deep Averaging Network
'''


#Experiment 4 - Retrain classifiers using a whole bunch of political topics in table A. Test overall accuracy on combined data set. 

'''
Accuracy on Combined Tweets

Naive Bayes
SVM
Logistic Regression
Deep Averaging NN
'''
#Experiment 5 - Using best performing sentiment classifier from experiment 4, to predict democratic politician sentiment for various topics. 
#Reported sentiment numbers are in terms of the probability of the “positive” class. 

'''
Nominate Dim1
Net Neutrality
Gay Marriage
Immigration Ban
Obamacare
Border Wall


Barack Obama
Elizabeth Warren
Hillary Clinton
Kamala Harris
Joe Biden
'''

#Experiment 6 - Using best performing sentiment classifier from experiment 4, to predict republican politician sentiment for various topics. 
#Reported sentiments are in terms of the probability of the “positive” class. 

'''
Nominate Dim1
Net Neutrality
Gay Marriage
Immigration Ban
Obamacare
Border Wall


Mike Pence
Marco Rubio
Bobby Jindal
Rand Paul
Paul Ryan
'''

#Experiment 7 - Use sentiment classifier output as features, build political classifier as democratic or republican
'''
Accuracy over test politicians


Logistic Regression
Support Vector Machine
Decision Trees
Neural Network
'''

#Experiment 8 - Using sentiment classifier output as features, predict the DW-Nominate score of politicians.

'''

Accuracy over test politicians


Logistic Regression
Linear Regression w/ logistic transformation
GLM with logistic link function
Beta Regression
Multilayer Perceptron with Sigmoid Activation
Decision Trees
'''

#Experiment 9 - Using sentiment classifier output as features, predict the DW-Nominate score of politicians.
'''
RBF Kernel
Trigonometric Kernel
3rd Degree Polynomial Basis Expansion


Logistic Regression
Linear Regression w/ logistic transformation
GLM with logistic link function
Beta Regression
'''


#Experiment 10 - Do not use the sentiment classifiers for various topics at all. Instead directly classify whether democratic or 
#republican using standard NLP techniques. Neural networks use pre-trained embeddings. Softmax layer is used at the end to predict classes. 
#Accuracies are reported as amount correct divided by total predictions. 
'''
Democrat/Republican Prediction Accuracies

Recurrent Neural Network
Deep Averaging Neural Network
Hierarchical Network
Naive Bayes
Logistic Regression
Support Vector Machines
'''

#Experiment 11 - Do not use the sentiment classifiers for various topics at all. Instead directly predict DW-Nominate scores. 
#Neural networks use pre-trained embeddings. Accuracy is reported as the expected value of 1 - (DW Score Prediction Error)

'''
DW-Nominate Accuracy

Recurrent Neural Network
Deep Averaging Neural Network
Hierarchical Network
Naive Bayes
Logistic Regression
Support Vector Machines
'''

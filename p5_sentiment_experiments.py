import h5py as h5
import numpy as np
#Transformers
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
#Classifier Models
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model.stochastic_gradient import SGDClassifier
from sklearn.neural_network import multilayer_perceptron
#Word Embeddings
#from gensim.models import Word2Vec

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
    "Confederate Flag", "Death Penalty", "Religious Freedom Act"]
query_list2 = ["brexit_tweets", "ferguson_tweets", "travel_ban_tweets", "trump_tweets", "ireland_tweets"]


pipe_nb = Pipeline([('tfid', TfidfVectorizer()),
                          ('clf', MultinomialNB())])

pipe_lr = Pipeline([('tfid', TfidfVectorizer()),
                          ('clf', LogisticRegression(solver='lbfgs', max_iter=200))])

pipe_svm = Pipeline([('tfid', TfidfVectorizer()),
                  ('clf', SVC(gamma='scale', kernel='poly'))])
pipelines = [pipe_nb, pipe_lr, pipe_svm]
pipelines = [pipe_nb, pipe_lr]
pipe_dict = {0: 'Naive Bayes', 1: 'Logistic Regression', 2: 'SVM'}

do = False
if(do):
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
    for query in query_list2:
        print("\n For query {}".format(query))
        with h5.File(h5_path, "a") as f:
            if(("/" + query) not in f): continue
            group = f["/" + query]
            X_train = list(group["X_train"])
            X_test = list(group["X_test"])
            y_train = list(group["y_train"])
            y_test = list(group["y_test"])
       
        for counter, pipe in enumerate(pipelines):
            pipe.fit(X_train, y_train)
            predicted = pipe.predict(X_test)
            accuracy = np.mean(predicted == y_test)
            accuracy = round(accuracy, 2)
            print("For clf {}, accuracy is {}".format(pipe_dict[counter],accuracy))
            counter += 1

do = True
if(do):
    #Experiment 2 - Combine all tweets from all topics into one set. Train one classifier over all topics. Test each classifier on data from individual topics.
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    for query in query_list2:
        with h5.File(h5_path, "a") as f:
            group = f[query]
            X_train.extend(list(group["X_train"]))
            X_test.extend(list(group["X_test"]))
            y_train.extend(list(group["y_train"]))
            y_test.extend(list(group["y_test"]))
    
    #Accuracy on Combined
    for counter, pipe in enumerate(pipelines):
        pipe.fit(X_train, y_train)
        predicted = pipe.predict(X_test)
        accuracy = np.mean(predicted == y_test)
        #print("For clf {}, accuracy is {}".format(pipe_dict[counter],accuracy))
    
    #Accuracy on individual topics
    for query in query_list2:
        #print("\n For query {}".format(query))
        with h5.File(h5_path, "a") as f:
            group = f[query]
            X_test_temp = list(group["X_test"])
            y_test_temp = list(group["y_test"])
        for counter, pipe in enumerate(pipelines):
            predicted = pipe.predict(X_test_temp)
            accuracy = np.mean(predicted == y_test_temp)
            #print("For clf {}, accuracy is {}".format(pipe_dict[counter],accuracy))
    
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

    
do = False
if(do):
    #Experiment 3 - Use the four classifiers trained in experiment 2. Test accuracy on topics it has never seen before (tweets with topics it wasn’t trained on)
    
    #Accuracy of prev model on different things
    q_list = ["Affirmative Action", "Artificial intelligence", "vaccines", "NRA", "Planned Parenthood", "Death Penalty", "Labor Unions"]
    q_list = ["Obamacare", "Confederate Flag", "Marijuana"]
    #Accuracy on individual topics
    for query in q_list:
        print(" \n For query {}".format(query))
        with h5.File(h5_path, "a") as f:
            group = f[query]
            X_test_temp = list(group["X_test"])
            y_test_temp = list(group["y_test"])
        for counter, pipe in enumerate(pipelines):
            predicted = pipe.predict(X_test_temp)
            accuracy = np.mean(predicted == y_test_temp)
            print("For clf {}, accuracy is {}".format(pipe_dict[counter],accuracy))
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
do = False
if(do):
    #Experiment 4 - Retrain classifiers using a whole bunch of political topics in table A. Test overall accuracy on combined data set. 
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    for query in query_list:
        with h5.File(h5_path, "a") as f:
            group = f[query]
            X_train.extend(list(group["X_train"]))
            X_test.extend(list(group["X_test"]))
            y_train.extend(list(group["y_train"]))
            y_test.extend(list(group["y_test"]))
    #Accuracy on Combined
    for counter, pipe in enumerate(pipelines):
        print("For queries combined {} \n".format(query))
        pipe.fit(X_train, y_train)
        predicted = pipe.predict(X_test)
        accuracy = np.mean(predicted == y_test)
        print("For clf {}, accuracy is {}".format(pipe_dict[counter],accuracy))

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



'''     
#Bag-of-Words Matrix using TD-IDF instead of count. Shape is [n_samples, n_features]
tf = TfidfVectorizer()
x_train_tfidf = tf.fit_transform(x_train)

#Fit naiive bayes using training matrix and class vector
text_clf = MultinomialNB().fit(x_train_tfidf, labels_train)

#Accuracy using test set
x_test_tfidf = tf.transform(x_test)
predicted = text_clf.predict(x_test_tfidf)
print(np.mean(predicted == labels_test))


text_clf2 = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=6, random_state=42)
text_clf2 = text_clf2.fit(x_train_tfidf, labels_train)
predicted2 = text_clf2.predict(x_test_tfidf)
print(np.mean(predicted2 == labels_test))
'''
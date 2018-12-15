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
import re


output_label_dict = {}
views_dict =  {"affirmative action":("liberal", "conservative"), "daca immigration" :("liberal","conservative") ,
	"assisted suicide" :("liberal","conservative"),"capital punishment" :("conservative","liberal"), 
	"labor unions" :("liberal","conservative"), "vaccines" :("liberal","conservative"), "concealed weapons":("conservative", "liberal"), 
	"self-driving cars" :("liberal","conservative"),"artificial intelligence":("liberal","conservative"), "donald trump":("conservative", "liberal"),
	"planned parenthood": ("liberal","conservative"), "social security" :("liberal","conservative"), "nra" :("conservative", "liberal"), 
	"fracking" :("liberal","conservative"), "nuclear energy":("conservative", "liberal"), "nsa surveillance" :("liberal","conservative"),
	 "military spending":("conservative", "liberal"), 
	"foreign aid" :("liberal","conservative"), "dakota access pipeline":("conservative", "liberal"), "oil drilling":("conservative", "liberal"), 
	"paris climate agreement" :("liberal","conservative"), 
	"trans pacific partnership" :("liberal","conservative"), "china tariffs":("conservative", "liberal"), "labor unions" :("liberal","conservative"), 
	"universal basic income" :("liberal","conservative"), "paid sick leave" :("liberal","conservative"), "safe haven" :("liberal","conservative"),
	 "medicaid" :("liberal","conservative"), 
	"edward snowden" :("liberal","conservative"), "whistleblower protection" :("liberal","conservative"), "armed teachers":("conservative", "liberal"),
	 "gun control" :("liberal","conservative"),
	"in-state tuition" :("liberal","conservative"), "immigration ban":("conservative", "liberal"), "border wall":("conservative", "liberal"), 
	"first amendment" :("liberal","conservative"), 
	"confederate flag":("conservative", "liberal"), "death penalty":("conservative", "liberal"), "religious freedom act" :("liberal","conservative"),
	"travel ban" :("liberal","conservative"),"obamacare" :("liberal","conservative"),"affordable care act":("liberal","conservative"),
	"gay marriage":("liberal","conservative"),"marijuana":("liberal","conservative"),"net neutrality":("liberal","conservative"),"nsa":("liberal","conservative")}

def load_dict(politicians, broken_keywords, keyword_tweet_dict, pipelines):
	
	data_list = []
	for politician in politicians:
		politician_dict = {}
		#print("Organizing "+politician+" tweets based on keywords...")
		filename = "app_data/user_timelines/"+politician+".txt" 
		file = open(filename,"r", encoding="utf-8")
		broken_keywords_keys = broken_keywords.keys()
		for keys in broken_keywords_keys:
			keys = keys.lower()
			politician_dict[keys] = 0
		for tweet in file:
			lower_tweet = tweet.lower()
			for keyword in broken_keywords_keys:
				keyword = keyword.lower()
				if keyword in lower_tweet:
					
					temp = tweet
					query_reg = re.compile(r'({})'.format(keyword), re.IGNORECASE)
					#\S: nonwhitespace, (): capture, \1: match first capture, *: 0 or more prev element, +: 1 or more prev element, []: shorthand OR, {2,}: repeat prev 2 or more, \w: any letter
					url_reg = re.compile(r'\S*(https|www)\S*', re.IGNORECASE)
					username_reg = re.compile(r'\S*@\S+')
					repeat_reg = re.compile(r'(\w)\1{2,}')
					
					temp = query_reg.sub('QUERY_TERM', temp)
					temp = url_reg.sub('URL_TERM', temp)
					temp = username_reg.sub('USERNAME_TERM', temp)
					temp = repeat_reg.sub(r'\1\1', temp)
				
					#updated_tuple = keyword_tweet_dict[keyword]+(politician+":"+tweet,)
					#keyword_tweet_dict[keyword] = updated_tuple
					#prediction = clf.predict(tweet)
					prediction = pipelines[0].predict([temp])[0].decode("utf-8") 
					# print(keyword)
					# print(temp)
					# print(prediction)
					if(prediction == 'Positive'):
						politician_dict[keyword] += 1
					elif(prediction == 'Negative'): 
						politician_dict[keyword] -= 1 
					break
		data_list.append(politician_dict)				
	#output_dict = keyword_tweet_dict
	#return output_dict
	return data_list

def break_down(keywords):
	broken_keywords = {}
	for keyword in keywords: 
		splitted_keyword = keyword.lower().split()
		broken_keywords[keyword] = tuple(splitted_keyword)
	return broken_keywords

def init_dict(keywords):
	keyword_tweet_dict = {}
	for keyword in keywords:
		keyword_tweet_dict[keyword] = ()
	return keyword_tweet_dict

def print_output(politicians,output):
	for i in range(0,len(politicians)):
		print(politicians[i])
		print(output[i])
		print("\n")



def get_classifier_output(politician_output_dict,politician_names):
	idx = 0
	for politician in politician_names:
		print(politician)
		views = []
		topics = politician_output_dict[idx].keys()
		for topic in topics:
			view = decide_view(topic,politician_output_dict[idx][topic])
			views.append(view)
		output_label_dict[politician] = label_politician(views)
		idx = idx+1

def evaluate(actual_dw_nominate,politician_output_dict,politician_names):
	get_classifier_output(politician_output_dict,politician_names)
	correct = 0
	number_of_politicians = len(politician_names)
	for politician in politician_names:
		print(politician)
		actual_label = translate_dw_nominate_score(actual_dw_nominate[politician])
		print("True party: "+actual_label)
		output_label = output_label_dict[politician]
		print("Predicted party: "+output_label)
		if actual_label == output_label:
			correct +=1
	acc = (correct/number_of_politicians)* 100
	print("accuracy of party prediction: "+str(acc)+"%")


def translate_dw_nominate_score(value):
	if value <0:
		return "democrat"
	elif value>0:
		return "republican"


def decide_view(topic,score):
	topic = topic.strip()
	if score>0:
		return views_dict[topic][0]
	elif score<0:
		return views_dict[topic][1]



def label_politician(views):
	liberal_count = 0
	conservative_count = 0

	for view in views:
		if view == "liberal":
			liberal_count += 1
		elif view == "conservative":
			conservative_count += 1
	print(liberal_count)
	print(conservative_count)
	if liberal_count > conservative_count:
		return "democrat"
	elif conservative_count > liberal_count:
		return "republican"
	else:
	 return "centrist"
	


def main():
	dir_workspace = './app_data/model_workspace'
	h5_path = dir_workspace + '/dataset.hdf5'
	query_list2 = ["brexit_tweets", "ferguson_tweets", "travel_ban_tweets"] #"ireland_tweets" #"trump_tweets"
	
	pipe_nb = Pipeline([('tfid', TfidfVectorizer()),
	                          ('clf', MultinomialNB())])
	
	pipe_lr = Pipeline([('tfid', TfidfVectorizer()),
	                          ('clf', LogisticRegression(solver='lbfgs', max_iter=200))])
	
	pipe_svm = Pipeline([('tfid', TfidfVectorizer()),
	                  ('clf', SVC(gamma='scale', kernel='poly'))])
	#pipelines = [pipe_nb, pipe_lr, pipe_svm]
	pipelines = [pipe_lr]
	pipe_dict = {0: 'Naive Bayes', 1: 'Logistic Regression', 2: 'SVM'}
	
	
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
	    
	    
	    
	    
	keywords = ["Travel Ban", "Obamacare", "Affordable care act", 
	"Marijuana", "Net Neutrality", "Gay Marriage", 
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
	"Confederate Flag", "Death Penalty", "Religious Freedom Act", "NSA", "Donald Trump"]

	politicians = ["SenFeinstein","SenKamalaHarris","SenSanders" ,"HillaryClinton",
	"BarackObama","timkaine","JoeBiden","SenWarren","SenBooker","SenGillibrand",
	"SenatorHeitkamp","BobbyJindal","VP","GrahamBlog" ,"JeffFlake","JohnCornyn",
	"MikeCrapo","marcorubio"]
	
	politicians_dict = {"SenFeinstein": -0.27
				,"SenKamalaHarris": -0.694
,"SenSanders": -0.521
,"HillaryClinton": -0.367
,"BarackObama": -0.343
,"timkaine": -0.234
,"JoeBiden": -0.314
,"SenWarren": -0.758
,"SenBooker": -0.612
,"SenGillibrand": -0.412
,"SenatorHeitkamp": -0.122
,"BobbyJindal": 0.388,"VP": 0.655
,"GrahamBlog": 0.408
 ,"JeffFlake": 0.855
,"JohnCornyn": 0.495,
"MikeCrapo": 0.509,"marcorubio": 0.576}
	
	

	keyword_tweet_dict = init_dict(keywords)
	
	broken_keywords = break_down(keywords)

	output_dict = load_dict(politicians,broken_keywords,keyword_tweet_dict, pipelines)

	evaluate(politicians_dict,output_dict,politicians)
	



if __name__ == "__main__":
	main()

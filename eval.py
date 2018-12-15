
output_label_dict = {}
views_dict =  {"Affirmative Action":("democrat", "republican"), "DACA immigration" :("democrat","republican") ,
	"Assisted Suicide" :("democrat","republican") "Capital punishment" :("republican","democrat"), 
	"labor unions" :("democrat","republican"), "vaccines" :("democrat","republican"), "concealed weapons":("republican", "democrat"), 
	"self-driving cars" :("democrat","republican"),"Artificial intelligence":("democrat","republican"), "Donald Trump":("republican", "democrat"),
	"Planned Parenthood": ("democrat","republican"), "Social Security" :("democrat","republican"), "NRA" :("republican", "democrat"), 
	"Fracking" :("democrat","republican"), "Nuclear Energy":("republican", "democrat"), "NSA Surveillance" :("democrat","republican"),
	 "Military Spending":("republican", "democrat"), 
	"Foreign Aid" :("democrat","republican"), "Dakota Access Pipeline":("republican", "democrat"), "Oil Drilling":("republican", "democrat"), 
	"Paris Climate Agreement" :("democrat","republican"), 
	"Trans Pacific Partnership" :("democrat","republican"), "China Tariffs":("republican", "democrat"), "Labor Unions" :("democrat","republican"), 
	"Universal Basic Income" :("democrat","republican"), "Paid Sick Leave" :("democrat","republican"), "Safe Haven" :("democrat","republican"),
	 "Medicaid" :("democrat","republican"), 
	"Edward Snowden" :("democrat","republican"), "Whistleblower Protection" :("democrat","republican"), "Armed Teachers":("republican", "democrat"),
	 "Gun Control" :("democrat","republican"),
	"In-State Tuition" :("democrat","republican"), "Immigration Ban":("republican", "democrat"), "Border Wall":("republican", "democrat"), 
	"First Amendment" :("democrat","republican"), 
	"Confederate Flag":("republican", "democrat"), "Death Penalty":("republican", "democrat"), "Religious Freedom Act" :("democrat","republican")}



def get_classifier_output(politician_output_dict,politician_names):
	for politician in politician_names:
		topics = politician_output_dict.keys()
		views = []
		for topic in topics:
			view = decide_view(topic,politician_output_dict[topic])
			views.append(view)
		output_label_dict[politician] = label_politician(views)

def evaluate(actual_dw_nominate,politician_output_dict,politician_names):
	get_classifier_output(politician_output_dict,politician_names)
	correct = 0
	number_of_politicians = len(politician_names)
	for politician in politician_names:
		actual_label = translate_dw_nominate_score(actual_dw_nominate[politician])
		output_label = output_label_dict[politician]
		if actual_label == output_label:
			correct +=1
	acc = (correct/number_of_politicians)* 100
	print("accuracy of party prediction: "+acc+"%")


def translate_dw_nominate_score(value):
	if value <0:
		return "democrat"
	else if value>0:
		return "republican"
	else:
		return "centrist"

def decide_view(topic,score):
	if score>=0:
		return views_dict[topic][0]
	else:
		return views_dict[topic][1]



def label_politician(views):
	liberal_count = 0
	conservative_count = 0

	for view in views:
		if view == "liberal":
			liberal_count += 1
		else if view == "conservative":
			conservative_count += 1

	if liberal_count > conservative_count:
		return "democrat"
	else if conservative_count > liberal_count:
		return "republican"
	else:
		return "centrist"

		
def main():
	actual_dw_nominate = 
	politician_output_dict = 
	politician_names = 

	evaluate(actual_dw_nominate,politician_output_dict,politician_names)


if __name__ == "__main__":
	main()
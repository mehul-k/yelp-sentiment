import pandas as pd
from textblob import TextBlob

def read_data():
    df = pd.read_json('reviewSelected100.json', encoding = "ISO-8859-1", lines=True)
    return df

def mine_data(df):
    print("Mining Data! Please Wait ....")
    df['sentiment'] = df['text'].apply(lambda review: TextBlob(review).sentiment)
    df['polarity'] = df['sentiment'].apply(lambda sentiment: sentiment.polarity)
    df['subjectivity'] = df['sentiment'].apply(lambda sentiment: sentiment.subjectivity)
    df = df.drop(columns=['sentiment'])
    print("Polarity and Subjectivity of Data Calculated!")
    print("----")
    return df

def analyse_sentence():
    print("----")
    print("SENTENCE ANALYSER")
    print("----")
    while True:
        sentence = input("Enter your sentence here: ")
        print("Calculating ....")
        sentiment = TextBlob(sentence).sentiment
        print("Polarity: {}".format(sentiment.polarity))
        print("Subjectivity: {}".format(sentiment.subjectivity))
        print("")
        print("Please choose an option from below to continue!")
        print("1. Analyse another sentence.")
        print("2. Go back to main menu.")
        print("")
        option_selected = input("Enter your selection index here (1,2): ")
        if option_selected == '2':
            break

def get_sentences(df, num_sentences, positive: bool, negative: bool, subjective: bool, objectivity: bool, top: bool):
    if positive and top:
        positive_statements = df[df['polarity']==1]
        sentences = positive_statements.sample(n=num_sentences)
        return sentences
    elif positive:
        positive_statements = df[df['polarity']>0]
        sentences = positive_statements.sample(n=num_sentences)
        return sentences
    elif negative and top:
        negative_statements = df[df['polarity']==-1]
        sentences = negative_statements.sample(n=num_sentences)
        return sentences
    elif negative:
        negative_statements = df[df['polarity']<0]
        sentences = negative_statements.sample(n=num_sentences)
        return sentences
    elif subjective:
        subjective_statements = df[df['subjectivity']>0.5]
        sentences = subjective_statements.sample(n=num_sentences)
        return sentences
    elif objectivity:
        objective_statements = df[df['subjectivity']<=0.5]
        sentences = objective_statements.sample(n=num_sentences)
        return sentences

def get_analysis(mined_data):
    print("----")
    print("YELP REVIEWS ANALYSIS")
    print("----")
    while True:
        print("Please choose an option from below to continue, comma separated with number of sentence you wish to view (1-10) e.g. - 2,5")
        print("1. View random positive reviews.")
        print("2. View top positive reviews.")
        print("3. View random negative reviews.")
        print("4. View top negative reviews.")
        print("5. View subjective reviews.")
        print("6. View objective reviews.")
        print("7. Go back to main menu.")
        print("")
        option_selected = input("Enter your selection index here [(1-7),(1-10)]: ").split(",")
        if option_selected[0] == '7':
            break
        if option_selected[0] == '1':
            sentences = get_sentences(mined_data, option_selected[1], True, False, False, False, False)
        elif option_selected[0] == '2':
            sentences = get_sentences(mined_data, option_selected[1], True, False, False, False, True)
        elif option_selected[0] == '3':
            sentences = get_sentences(mined_data, option_selected[1], False, True, False, False, False)
        elif option_selected[0] == '4':
            sentences = get_sentences(mined_data, option_selected[1], False, True, False, False, True)
        elif option_selected[0] == '5':
            sentences = get_sentences(mined_data, option_selected[1], False, False, True, False, False)
        elif option_selected[0] == '6':
            sentences = get_sentences(mined_data, option_selected[1], False, False, False, True, False)
        
        
def app_loop(mined_data):
    while True:
        print("Please choose an option from below to continue!")
        print("1. Get analysis on the Yelp Dataset.")
        print("2. Analyse the sentiment of your own sentence.")
        print("3. Exit")
        print("")
        option_selected = input("Enter your selection index here (1,2,3): ")
        if option_selected == '3':
            break
        if option_selected == '1':
            get_analysis(mined_data)
        elif option_selected == '2':
            analyse_sentence()
        

if __name__=="__main__":
    data = read_data()
    #mined_data = mine_data(data)
    app_loop(data)

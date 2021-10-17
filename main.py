import pandas as pd
from textblob import TextBlob
from sentence_analyser import analyse_sentence
from yelp_data_viewer import get_analysis

# read the json data
def read_data():
    df = pd.read_json('reviewSelected100.json', encoding = "ISO-8859-1", lines=True)
    return df

# calculate the polarity and subjectivity of each sentence
def mine_data(df):
    print("Mining Data! Please Wait ....")
    df['sentiment'] = df['text'].apply(lambda review: TextBlob(review).sentiment)
    df['polarity'] = df['sentiment'].apply(lambda sentiment: sentiment.polarity)
    df['subjectivity'] = df['sentiment'].apply(lambda sentiment: sentiment.subjectivity)
    df = df.drop(columns=['sentiment'])
    print("Polarity and Subjectivity of Data Calculated!")
    print("----")
    return df

# main user menu
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
            get_analysis(mined_data) # view yelp data 
        elif option_selected == '2':
            analyse_sentence() # analyse your own sentence
        

if __name__=="__main__":
    data = read_data()
    mined_data = mine_data(data)
    app_loop(mined_data)

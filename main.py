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

def app_loop(mined_data):
    print("Please choose ")

if __name__=="__main__":
    data = read_data()
    mined_data = mine_data(data)

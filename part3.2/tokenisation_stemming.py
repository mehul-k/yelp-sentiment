import pandas as pd
import nltk
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import string
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

def tokenise_reviews(df):
    df['tokenised_reviews'] = df.apply(lambda row:word_tokenize(row['text']), axis = 1)
    return df

def porter_stem_reviews(tokenised_df):
    ps = PorterStemmer()
    tokenised_df['stemmed_text'] = tokenised_df.apply(lambda row : [ps.stem(str(word)) for word in row['tokenised_reviews']], axis = 1)
    return tokenised_df

def snowball_stem_reviews(tokenised_df):
    stemmer = SnowballStemmer(language='english')
    tokenised_df['stemmed_text'] = tokenised_df.apply(lambda row : [stemmer.stem(str(word)) for word in row['tokenised_reviews']], axis = 1)
    return tokenised_df

def get_word_frequency(stemmed_df):
    remove_these = set(stopwords.words('english') + list(string.punctuation) + list(string.digits))
    tokenised = []
    stemmed = []

    for index, row in stemmed_df.iterrows():
        tokenised.extend(row['tokenised_reviews'])
        stemmed.extend(row['stemmed_text'])

    filtered_text_tokenised = [w for w in tokenised if not w in remove_these]
    fdist_tokenised = nltk.FreqDist(filtered_text_tokenised)

    filtered_text_stemmed = [w for w in stemmed if not w in remove_these]
    fdist_stemmed = nltk.FreqDist(filtered_text_stemmed)

    return fdist_stemmed, fdist_tokenised 

def run_tokenization_stemming():
    df = pd.read_json('reviewSelected100.json', encoding = "ISO-8859-1", lines=True)

    # Business B1
    df_b1 = df.loc[df['business_id'] == 'ApeTrSttf8f4KUrBVtcKgw']
    df_b1_tokenised = tokenise_reviews(df_b1)
    df_b1_stemmed_porter = porter_stem_reviews(df_b1_tokenised)
    porter_stemmed_b1, tokenised_b1 = get_word_frequency(df_b1_stemmed_porter)
    df_b1_stemmed_snowball = snowball_stem_reviews(df_b1_tokenised)
    snowball_stemmed_b1, tokenised_b1 = get_word_frequency(df_b1_stemmed_snowball)

    # Business B2
    df_b2 = df.loc[df['business_id'] == 'ZBE-H_aUlicix_9vUGQPIQ']
    df_b2_tokenised = tokenise_reviews(df_b2)
    df_b2_stemmed_porter = porter_stem_reviews(df_b2_tokenised)
    porter_stemmed_b2, tokenised_b2 = get_word_frequency(df_b2_stemmed_porter)
    df_b2_stemmed_snowball = snowball_stem_reviews(df_b2_tokenised)
    snowball_stemmed_b2, tokenised_b2 = get_word_frequency(df_b2_stemmed_snowball)

    while True:
        print("B1 ID: ApeTrSttf8f4KUrBVtcKgw")
        print("B2 ID: ZBE-H_aUlicix_9vUGQPIQ")
        print("")
        print("Please choose an option from below to continue!")
        print("1. Get top 10 tokens for B1.")
        print("2. Get top 10 Porter's stemmed tokens for B1.")
        print("3. Get top 10 Snowball's stemmed tokens for B1.")
        print("4. Get top 10 tokens for B2.")
        print("5. Get top 10 Porter's stemmed tokens for B2.")
        print("6. Get top 10 Snowball's stemmed tokens for B2.")
        print("7. Go back")
        print("")
        option_selected = input("Enter your selection index here (1-7): ")
        if option_selected == "7":
            break
        elif option_selected == "1":
            print("10 most common: {words}".format(words=tokenised_b1.most_common(10)))
            print("")
            print("Close the plot window to continue!")
            tokenised_b1.plot(30,title='30 most common tokens in B1 reviews (excluding stopwords and punctuation)')
        elif option_selected == "2":
            print("10 most common: {words}".format(words=porter_stemmed_b1.most_common(10)))
            print("")
            print("Close the plot window to continue!")
            porter_stemmed_b1.plot(30,title='30 most common porters stemmed tokens in B1 reviews (excluding stopwords and punctuation)')
        elif option_selected == "3":
            print("10 most common: {words}".format(words=snowball_stemmed_b1.most_common(10)))
            print("")
            print("Close the plot window to continue!")
            snowball_stemmed_b1.plot(30,title='30 most common snowball stemmed tokens in B1 reviews (excluding stopwords and punctuation)')
        elif option_selected == "4":
            print("10 most common: {words}".format(words=tokenised_b2.most_common(10)))
            print("")
            print("Close the plot window to continue!")
            tokenised_b2.plot(30,title='30 most common tokens in B2 reviews (excluding stopwords and punctuation)')
        elif option_selected == "5":
            print("10 most common: {words}".format(words=porter_stemmed_b2.most_common(10)))
            print("")
            print("Close the plot window to continue!")
            porter_stemmed_b2.plot(30,title='30 most common porters stemmed tokens in B2 reviews (excluding stopwords and punctuation)')
        elif option_selected == "6":
            print("10 most common: {words}".format(words=snowball_stemmed_b2.most_common(10)))
            print("")
            print("Close the plot window to continue!")
            snowball_stemmed_b2.plot(30,title='30 most common snowball stemmed tokens in B2 reviews (excluding stopwords and punctuation)')
        else:
            print("Invalid Input! Please enter a number between 1-7")




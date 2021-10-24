import pandas as pd
import numpy as np
import en_core_web_sm
nlp = en_core_web_sm.load()

# Noun-Adjective pairs for each review
def lineN_Pr(text):
    """find and return all (Noun,Adjective) pairs in a list 
    this uses POS tagger from SpaCy library.
    Parameter: Text in 'String' form"""
    line=nlp(text)                                           #processing given text
    noun_adj_pairs = []                                      #list of (Noun,Adjective) pairs will be stored here
    for i,token in enumerate(line):
        if token.pos_ not in ('NOUN','PROPN'):
            continue

        if i==0:
          start_check=i
        else:
          start_check=i#-1

        for j in range(start_check,len(line)):                  #begin search for adjectives one word before specified noun 
            if line[j].pos_ == 'ADJ':                           # to account for Adjective-Noun pairs i.e. "Good Food"
                noun_adj_pairs.append((token.text,line[j].text))
                continue
            if line[j].text in ('.','!','?'):                   #Stop search for adjectives that describe noun when stopping punctuation is observed
                break
    return noun_adj_pairs

# Accumulates all N-Adj pairs from a dataframe of reviews
def df_txtN_Pr(dataframe):
    """a specific dataframe instead"""
    noun_adj_pairs = []
    for  index,row in dataframe.iterrows():
        N_Pr=lineN_Pr(row['text'].lower())
        noun_adj_pairs.extend(N_Pr)
      
    pairCnt={}
    for p in noun_adj_pairs:
        if (p in pairCnt):
            pairCnt[p]+=1
        else:
            pairCnt[p]=1
    out = pd.DataFrame(pairCnt.items(), columns=['Noun,Adj.', 'Frequency']) 
    return pairCnt

def sample20(stars, df):
  star= df.loc[df['stars'] == stars]   #change number of stars here
  rd=star.groupby('business_id').sample(n=1)
  rd=rd.sample(n=20)

  starPairs=pd.DataFrame(df_txtN_Pr(rd).items(), columns=['Noun,Adj.', 'Frequency']) 

  #Sorting
  top=starPairs.sort_values(by='Frequency',ascending=False)
  top=top.reset_index(drop=True)
  return top

def run_noun_adj_pair():
    df = pd.read_json('reviewSelected100.json', encoding = "ISO-8859-1", lines=True)

    # Obtain random sample of 1* reviews
    Onestar= df.loc[df['stars'] == 1]
    rdOne=Onestar.groupby('business_id').sample(n=1)
    rdOne=rdOne.sample(n=50)

    onestarPairs=pd.DataFrame(df_txtN_Pr(rdOne).items(), columns=['Noun,Adj.', 'Frequency']) 
    #Sorting
    top=onestarPairs.sort_values(by='Frequency',ascending=False)
    top=top.reset_index(drop=True)

    while True:
        print("View Star-Wise Noun-Adj Pairs")
        print("")
        print("Please choose an option from below to continue!")
        print("1. View top 10 pairs from 1-star reviews from sample of 50.")
        print("2. View top 10 pairs from 2-star reviews from sample of 20.")
        print("3. View top 10 pairs from 3-star reviews from sample of 20.")
        print("4. View top 10 pairs from 4-star reviews from sample of 20.")
        print("5. View top 10 pairs from 5-star reviews from sample of 20.")
        print("6. Go back.")
        option_selected = input("Enter your selection index here (1-6): ")
        print("")
        if option_selected == "6":
            break
        elif option_selected == "1":
            print("Top 10 pairs from 1-star reviews from sample of 50.")
            print("")
            print(top.head(10))
        elif option_selected == "2":
            print("Top 10 pairs from 2-star reviews from sample of 20.")
            print("")
            rdtwostar=sample20(2, df)
            print(rdtwostar.head(10))
        elif option_selected == "3":
            print("Top 10 pairs from 3-star reviews from sample of 20.")
            print("")
            rdthreestar=sample20(3, df)
            print(rdthreestar.head(10))
        elif option_selected == "4":
            print("Top 10 pairs from 4-star reviews from sample of 20.")
            print("")
            rdfourstar=sample20(4, df)
            print(rdfourstar.head(10))
        elif option_selected == "5":
            print("Top 10 pairs from 5-star reviews from sample of 20.")
            print("")
            rdfivestar=sample20(5, df)
            print(rdfivestar.head(10))
        else:
            print("Invalid Input! Please input a number between 1-6")



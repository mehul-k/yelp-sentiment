from textblob import TextBlob
from print_description import analysis_description

def analyse_sentence():
    print("----")
    print("SENTENCE ANALYSER")
    print("----")
    while True:
        sentence = input("Enter your sentence here: ")
        print("Calculating ....")
        sentiment = TextBlob(sentence).sentiment
        polar=sentiment.polarity
        subjvty=sentiment.subjectivity
        print("Polarity: {0:.3f}".format(polar), end="\t\t")
        print("Subjectivity: {0:.3f}".format(subjvty))
        
        print("")
        analysis_description(polar,subjvty)
        print("Please choose an option from below to continue!")
        print("1. Analyse another sentence.")
        print("2. Go back to main menu.")
        print("")
        option_selected = input("Enter your selection index here (1,2): ")
        if option_selected == '2':
            break
    
        

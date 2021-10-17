from textblob import TextBlob

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
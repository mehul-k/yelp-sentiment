from textblob import TextBlob

def analyse_sentence():
    print("----")
    print("SENTENCE ANALYSER")
    print("----")
    while True:
        print("Ensure the sentence is of proper spelling.")
        sentence = input("Enter your sentence here: ")
        print("Calculating ....")
        sentiment = TextBlob(sentence).sentiment
        polar=sentiment.polarity
        subjvty=sentiment.subjectivity
        print("Polarity: {0:.3f}".format(polar), end="\t\t")
        print("Subjectivity: {0:.3f}".format(subjvty))
        
        print("")
        print("The sentence is",end=" ")
        offmid=0
        if polar>.6:
            print("highly positive",end="")
            offmid=1
        elif polar<-.6:
            print("highly negative",end="")
            offmid=1
        elif polar>.1:
            print("positive",end="")
            offmid=0
        elif polar<-.1:
            print("negative",end="")
            offmid=0
        else:
            print("neutral/balanced",end="")
            offmid=0
            
        if subjvty>.5:
            if offmid==1:
                print(" and",end=" ")
            else:print(" , but",end=" ")
            print("is very opinionated/subjective.",end=" ")
        elif subjvty>.1:
            print(" and might be an opinion.")
        else:
            if offmid==1:
                print(", even though",end=" ")
            else:print(" and",end=" ")
            print("it is likely factual.")
        
        print("")
        print("Please choose an option from below to continue!")
        print("1. Analyse another sentence.")
        print("2. Go back to main menu.")
        print("")
        option_selected = input("Enter your selection index here (1,2): ")
        if option_selected == '2':
            break
    
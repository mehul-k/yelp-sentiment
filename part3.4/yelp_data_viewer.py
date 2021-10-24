import pandas as pd
from print_description import analysis_description

def get_sentences(df, num_sentences, positive: bool, negative: bool, subjective: bool, objectivity: bool, top: bool):
    num_sentences = int(num_sentences)
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
        print("----")
        if option_selected[0] == '7':
            break
        if len(option_selected) == 1:
            print("Please enter the number of desired review! (Comma Separated)")
            print("----")
            continue
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

        i = 1
        for index, row in sentences.iterrows():
            print("SENTENCE {}: ".format(i))
            print(row['text'])
            print("")
            print("Stars: {}".format(row['stars']))
            polar=row['polarity']
            subjvty=row['subjectivity']
            print("Polarity: {0:.3f}".format(polar), end="\t\t")
            print("Subjectivity: {0:.3f}".format(subjvty))
            print("")
            
            analysis_description(polar,subjvty)
            
            print("----")
            i+=1

import pandas as pd
import nltk
import spacy
import json
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# nltk
def nltk_pos_tagging(tokenized_sentence):
  try:
    tagged_sentence = []
    for i in tokenized_sentence:
      words = nltk.word_tokenize(i)
      tagged_sentence.append(nltk.pos_tag(words))
    return tagged_sentence
            
  except Exception as e:
    print(str(e))

# spaCy POS Tagging
def spacy_pos_tagging(sentence):
  try:
    tagged_sentence = []
    for i in sentence:
      if i.pos_ == 'SPACE':
        continue
      else:
        tagged_sentence.append([(str(i),i.pos_)])
    return tagged_sentence
            
  except Exception as e:
    print(str(e))

def run_pos_tagging():

    sample = []
    for line in open('reviewSelected100.json', encoding = "ISO-8859-1"):
        sample.append(json.loads(line))

    pos_sample = sample[0:5]

    # NLTK POS Tagging
    tokenized_sample = []
    for i in range(0,5):
        sample_text= pos_sample[i].get('text')
        tokenized_sample_text = nltk.word_tokenize(sample_text)
        tokenized_sample.append(tokenized_sample_text)
    
    nltk_pos_tag_list = []
    for i in tokenized_sample:
        nltk_pos_tag_list.append(nltk_pos_tagging(i))

    # spaCy POS Tagging
    sp = spacy.load('en_core_web_sm')

    spacy_pos_sample = []
    for i in range(0,5):
        spacy_pos_sample.append(sp(pos_sample[i].get('text')))
    spacy_pos_tag_list = []
    for i in spacy_pos_sample:
        spacy_pos_tag_list.append(spacy_pos_tagging(i))
    

    while True:
        print("")
        print("NLTK and spaCy toolkits used for POS Tagging.")
        print("Slightly diffrent results, for example NLTK: [('first', 'RB')] spaCy: [('first', 'ADJ')]")
        print("")
        print("Please choose an option from below to continue!")
        print("1. View NLTK POS Tagging.")
        print("2. View SpaCy POS Tagging")
        print("3. Go back.")
        option_selected = input("Enter your selection index here (1-3): ")
        if option_selected == "3":
            break
        elif option_selected == "1":
            print("Printing NLTK POS Tagging Results: ")
            print("")
            for el in nltk_pos_tag_list:
                print(el)
        elif option_selected == "2":
            print("Printing SPACY POS Tagging Results: ")
            print("")
            for i in spacy_pos_tag_list:
                print(i)
        else:
            print("Invalid Input! Please input a number between 1-3")
        

            

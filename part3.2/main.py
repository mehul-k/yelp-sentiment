from noun_adj_pair import run_noun_adj_pair
from pos_tagging import run_pos_tagging
from tokenisation_stemming import run_tokenization_stemming

if __name__ == "__main__":
    while True:
        print("Welcome to NLP Assignment 1 Part-3.2")
        print("")
        print("Please choose an option from below to continue!")
        print("1. View Tokenization and Stemming Results.")
        print("2. View POS Tagging Results.")
        print("3. View Noun-Adj Pairs Star Rating Wise of Reviews.")
        print("4. Quit.")
        option_selected = input("Enter your selection index here (1-4): ")
        if option_selected == "4":
            break
        elif option_selected == "1":
            run_tokenization_stemming()
        elif option_selected == "2":
            run_pos_tagging()
        elif option_selected == "3":
            run_noun_adj_pair()
        else:
            print("Invalid Input! Pease enter a number between 1-4")
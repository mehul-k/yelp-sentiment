Source Code for CZ4045 (NLP) Assignment-1
- By Group 42
Submitted on 25 October 2021

The repository has been divided into 3 folders - part3.2, part3.3, part3.4 according to the Assignment requirements.

Most of the code has been written as .py (Python3) files, apart from Writing Style (3.2.3) and Extraction of Indicative Phrases (3.3).
These 2 files are present as .ipynb files which can be opened and viewed using Jupyter Notebook.
This is due to the nature of these tasks which are best presented in a python notebook.

To run the .py files in parts 3.2 and 3.4, go to the respective directory and execute the following commands:
> pip3 install -r requirements.txt (to the depedency libraries)
> python3 main.py (to run the application)

After running the main.py, you'll see an interative menu, where you can select the desired option to continue.

For Example:
After running main.py in part 3.4, you'll see:

> (tf) Mehuls-MacBook-Pro:part3.4 mehulkumar$ python3 main.py 
> Mining Data! Please Wait ....
> Polarity and Subjectivity of Data Calculated!
> ----
> Please choose an option from below to continue!
> 1. Get analysis on the Yelp Dataset.
> 2. Analyse the sentiment of your own sentence.
> 3. Exit
> 
> Enter your selection index here (1,2,3): 

Here, if you enter 1, this is the application flow you'll follow:
> ----
> YELP REVIEWS ANALYSIS
> ----
> Please choose an option from below to continue, comma separated with number of sentence you wish to view (1-10) e.g. - 2,5
> 1. View random positive reviews.
> 2. View top positive reviews.
> 3. View random negative reviews.
> 4. View top negative reviews.
> 5. View subjective reviews.
> 6. View objective reviews.
> 7. Go back to main menu.
> 
> Enter your selection index here [(1-7),(1-10)]: 2,1
> ----
> SENTENCE 1: 
> Excellent food and service. Had the Ribeye end cap and it was delish!
> 
> Stars: 5
> Polarity: 1.0
> Subjectivity: 1.0
> ----

Similarly, here is an example flow of application for part3.2:

> (tf) Mehuls-MacBook-Pro:part3.2 mehulkumar$ python3 main.py
> Welcome to NLP Assignment 1 Part-3.2
> 
> Please choose an option from below to continue!
> 1. View Tokenization and Stemming Results.
> 2. View POS Tagging Results.
> 3. View Noun-Adj Pairs Star Rating Wise of Reviews.
> 4. Quit.
> Enter your selection index here (1-4): 3
> View Star-Wise Noun-Adj Pairs
> 
> Please choose an option from below to continue!
> 1. View top 10 pairs from 1-star reviews from sample of 50.
> 2. View top 10 pairs from 2-star reviews from sample of 20.
> 3. View top 10 pairs from 3-star reviews from sample of 20.
> 4. View top 10 pairs from 4-star reviews from sample of 20.
> 5. View top 10 pairs from 5-star reviews from sample of 20.
> 6. Go back.
> Enter your selection index here (1-6): 2
> 
> Top 10 pairs from 2-star reviews from sample of 20.
> 
>           Noun,Adj.  Frequency
> 0  (service, great)          4
> 1      (feet, same)          2
> 2   (rating, touch)          2
> 3    (po'boy, good)          2
> 4   (nacho, shitty)          2
> 5  (cheese, shitty)          2
> 6   (service, much)          2
> 7      (food, much)          2
> 8      (side, same)          2
> 9    (water, brown)          2
> View Star-Wise Noun-Adj Pairs
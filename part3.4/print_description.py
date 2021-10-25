# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:14:03 2021

@author: Jun Wei
"""

def analysis_description(polar,subjvty):
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
        print("it is likely factual in nature.")
    
    print("")
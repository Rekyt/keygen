# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:51:52 2013

@author: mgrenie

Create a password generator using textfiles.
"""
import random as r

def filelen(filename):
    """
    DESCRIPTION:\n
    
    Return the length of a text file  
    
    USAGE:\n
    filename - the name of a text file
    """
    with open(filename,'r') as f:
        i = 0
        for line in f.readlines():
            i += 1
    return i

def randline(tot,num):
    """
    DESCRIPTION:\n
    
    Generate a number of samples equals to num, from a range going from 1 to tot
    """
    lines = range(1,tot)
    samp = r.sample(lines,num) #extract number from total number of line
    return samp

def fetch(filename,samp):
    """
    Go fetch the words at positions samp in filename
    
    USAGE:\n
    filename - name of a file\n
    samp - list of integer giving the number of lines
    """
    chosen = list()
    with open(filename,'r') as f:
        i = 0
        for line in f.readlines():
            i += 1
            if i in samp:
                chosen.append(line.strip())
    r.shuffle(chosen) #shuffle the list of chosen words
    return chosen

def specchar(num):
    """
    Returns a list of num special characters in random order
    """
    spec = "$&!@#/:;.,?*()[]" #list of special char
    c = r.sample(spec,num)
    r.shuffle(c)
    return c

def join(spec,chosen):
    """
    Takes a list of special character and a list of words and associate them randomly
    """
    j = ""
    for w in chosen:
        j += w
        j += "".join(r.sample(spec,1))
    for c in spec:
        j.rstrip(c)
    return j
    
if __name__ == "__main__":
    #Fonction générale
    name = "dic.txt"
    l = filelen(name)
    print "le fichier %s fait %d lignes" % (name,l)
    samp = randline(l,5)
    
    chosen = fetch(name,samp)

    n = raw_input("How many spec char do you want? ")
    
    c = specchar(int(n))
    
    j = join(c,chosen)
    
    print "generated password: %s" % j
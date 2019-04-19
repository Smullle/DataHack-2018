import pandas as pd
import numpy as np

lang = pd.read_csv("/Users/Shane/Desktop/DataHack2018/datasets/language/language.csv",encoding="utf8")
lang.set_index('id',inplace=True)

##set language column to ENGLISH,FRENCH....

const = ["ENGLISH","FRENCH","GERMAN","ITALIAN","PORTUGUESE","SPANISH","JAPANESE"]
three = ["ENG","FRA","GER","ITA","POR","SPA","JAP"]
two = ["EN","FR","DE","IT","PT","ES","JA"]

d3 = {"ENG": "ENGLISH"}
d2 = {"EN": "ENGLISH"}

for x in range(0,len(const)):
    d3.update({three[x]:const[x]})
    d2.update({two[x]:const[x]})

lang["language"].replace(d2,inplace=True)
lang["language"].replace(d3,inplace=True)



#isLangueage functions, used to test if a string is a given langueage by checking them against unique characters associated with each langueage eg: ß in German

def isJapanese(text):
    latinAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ä","ë","ï","ö","ü","ß","æ","á","é","í","ó","ú","à","è","ì","ò","ù","â","ê","î","ô","û","ç","Ç","ñ","¿","¡","Á","À","Ä","É","È","Ë","Í","Ì","Ï","Ñ","Ó","Ò","Ö","Ú","Ù","Â","â","Ê","ê","Î","î","Ô","ô","Û","û","Õ","õ"]
    count = 0
    for i in range(0,len(text)):
        if text[i] not in latinAlphabet:
            count += 1
    if count > len(text)*0.75:
        return True
    return False

def isGerman(text):
    uniqueGRM = ["ä","ö","ß","Ä","Ö"]
    for i in range(0,len(text)):
        if text[i] in uniqueGRM:
            return True
            break
    return False

def isSpanish(text):
    uniqueSPA = ["Ñ","ñ","¿","¡"]
    for i in range(0,len(text)):
        if text[i] in uniqueSPA:
            return True
            break
    return False

def isPort(text):
    uniquePRT = ["Õ","õ"]
    for i in range(0,len(text)):
        if text[i] in uniquePRT:
            return True
            break
    return False

def isFrench(text):
    uniqueFRA = ["Î","î","Û","û"]
    for i in range(0,len(text)):
        if text[i] in uniqueFRA:
            return True
            break
    return False

def isItaly(text):
    uniqueITY = ["ì","Ì"]
    for i in range(0,len(text)):
        if text[i] in uniqueITY:
            return True
            break
    return False

def lanCounter(text):
    #lists of top ten words accross all languages
    mcGERMAN = ["ich","sie","das","ist","du","nicht","die","und","es","der",0,"GERMANY"]
    mcITALIAN = ["non","e","che","di","la","è","il","un","per","a",0,"ITALY"]
    mcFRENCH = ["je","de","est","pas","le","vous","la","tu","il","un",0,"FRENCH"]
    mcPORT = ["que","o","não","de","é","você","e","eu","um","se",0,"PORTUGAL"]
    mcSPANISH = ["de","que","no","la","el","y","es","en","lo","un",0,"SPAIN"]
    mcENGLISH = ["the","be","to","of","and","a","in","that","have","i",0,"ENGLISH"]
    mcWorldwide = [mcGERMAN,mcITALIAN,mcFRENCH,mcPORT,mcSPANISH,mcENGLISH]

    text = text.split()
    #frequency counter for most common words in each langieage
    for x in range(0,len(text)):
        if x in mcGERMAN:
            mcGERMAN[10] +=1
        if x in mcITALIAN:
            mcITALIAN[10] +=1
        if x in mcFRENCH:
            mcFRENCH[10] +=1
        if x in mcPORT:
            mcPORT[10] +=1
        if x in mcSPANISH:
            mcSPANISH[10] +=1
        if x in mcENGLISH:
            mcENGLISH[10] +=1

    mcWorldwide = sorted(mcWorldwide, key = lambda x: x[11], reverse = True)
    return mcWorldwide[0][11]

##add column for correct match

##lang.add(lang,axis="correct",fill_value=0)
# lang.fillna(0,inplace=True)
lang["correct"]="NO"

##testing for match using functions from above

for x in range(0,len(lang)):
    if isJapanese(lang.loc[x,"text"]):
        lang.set_value(x,"correct","JAPANESE")
    if isGerman(lang.loc[x,"text"]):
        lang.set_value(x,"correct","GERMAN")
    if isSpanish(lang.loc[x,"text"]):
        lang.set_value(x,"correct","SPANISH")
    if isPort(lang.loc[x,"text"]):
        lang.set_value(x,"correct","PORTUGUESE")
    if isFrench(lang.loc[x,"text"]):
        lang.set_value(x,"correct","FRENCH")
    if isItaly(lang.loc[x,"text"]):
        lang.set_value(x,"correct","ITALIAN")


for x in range(0,len(lang)):
    if(lang.loc[x,"correct"]=="NO"):
        s = lanCounter(lang.loc[x,"text"])
        lang.set_value(x,"correct",s)

print(lang)

print(lang["correct"].value_counts())

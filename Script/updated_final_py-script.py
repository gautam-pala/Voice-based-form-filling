# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:16:09 2020

@author: Gautam Pala
"""

#URL = 'https://form.jotform.me/93325521458458' 
#https://form.jotform.me/200580949889069

import tkinter as tk
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from gtts import gTTS 
import os
import threading
import time
from googletrans import Translator
from PIL import ImageTk,Image
import webbrowser
import csv
langs = {
    'auto': 'Automatic',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese Simplified',
    'zh-tw': 'Chinese Traditional',
    'co': 'Corsican',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ma': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
}
langs = dict(map(reversed, langs.items())) 

translator = Translator()

global text
global URL
global j
l2=[]
URL=input("please enter the Url of your form : ")


temp=input("please enter the preffered langauge : ")
temp = temp.capitalize()
language = langs[temp]
def fun1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(translator.translate("Speak :", dest=language).text)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text1=translator.translate(text).text
            print(translator.translate("You said : {}".format(text1), dest=language).text)
            return text1
        except:
                print(translator.translate("Sorry could not recognize what you said",dest=language).text)
                fun1()
                #return "Sorry could not recognize what you said"
def fun2(j):
        text = "please enter the " + name[j] 
        #language = 'en'
        speech=translator.translate(text, dest=language).text
        speech = gTTS(text = speech, lang = language, slow = False)
        speech.save("text"+str(j)+".mp3")
        os.system("start text"+str(j)+".mp3")
        j=j+1           

#def fun3():
#    URL=e1.get()
    
#master=tk.Tk()         
#k.Label(master, text='Enter the URL for form').grid(row=0)
#e1 = tk.Entry(master)
#B0 = tk.Button(master, text="Submit", command=fun3,width=20  ,height=3, activebackground = "Blue" ,font=('times', 15, ' bold '))
#B0.place(x=100, y=300)
#URL=e1.get()
#URL = URL[1:len(URL)-1]
#e1.grid(row=0, column=1)
#B1 = tk.Button(master, text="Start", command=fun1,width=20  ,height=3, activebackground = "Blue" ,font=('times', 15, ' bold '))
#B1.place(x=200, y=500)
#B2 = tk.Button(master, text="Close", command=master.destroy,width=20  ,height=3, activebackground = "Blue" ,font=('times', 15, ' bold '))
#B2.place(x=600, y=500)

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
ip =soup.find_all("input")
label = soup.find_all("label")
print("-------------------------------")
name = []
ids = []
for i in ip:
    if i["type"] != "hidden" and i["name"] != "website":
        for j in label:
            if i["id"] == j["for"]:
                ids.append(i["name"])
                name.append(j.text)
                break
print(name)

j=0
ans = []
for i in range(len(name)):
        time.sleep(1)
        fun2(j)
        time.sleep(4)
        ans.append(fun1())
        j=j+1
print(ans)
l = name    
#print(l2)
print(URL)


for i in range(len(ans)):
    temp = ans.pop(i)
    temp = temp.split(" ")
    string = ""
    for j in range(len(temp)):
        if j != len(temp)-1:
            string += temp[j] + "+"
        else:
            string += temp[j]
    ans.insert(i, string)
#print(ans)

output = ""
for i in range(len(ids)):
    if i != len(ids)-1:
        output += ids[i] + "=" + ans[i] + "&"
    else:
        output += ids[i] + "=" + ans[i]
        
# https://submit.jotform.me/submit/93325521458458?q6_name=rushabh+patel&q4_university4=pandit+deendayal+petroleum+university&q5_branch=computer
#print(output)
url = "https://submit.jotform.me/submit/" + URL.split("/")[-1] + "?" + output
webbrowser.open(url)
'''
time.sleep(2)
master=tk.Tk()
master.geometry('1920x1080')
master.configure(background="gray")
text=tk.Label(master,text=l[0]).grid(row=0)
e1=tk.Entry(master)
e1.insert(20,l2[0])
e1.grid(row=0,column=1)
text1=tk.Label(master,text=l[1]).grid(row=1)
e2=tk.Entry(master)
e2.insert(20,l2[1])
e2.grid(row=1,column=1)
text2=tk.Label(master,text=l[2]).grid(row=3)
e3=tk.Entry(master)
e3.insert(20,l2[2])
e3.grid(row=3,column=1)
img=ImageTk.PhotoImage(Image.open("ty_final.png"))
imglabel = tk.Label(master,image=img).grid(row=6,column=10)
master.mainloop()

   '''

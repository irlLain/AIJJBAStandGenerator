import tkinter as tk
from tkinter import ttk
import random
import tkinter
from tkinter import *
import webbrowser
import csv
from random import *
import urllib.request
from openai import OpenAI
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from PIL import Image, ImageTk

#Sets API key
client = OpenAI(
    api_key = "sk-proj-dsScvMSZZjd7XBJbOV9eT3BlbkFJIMXuVbFxJ1taJ5Bbcfm7",
)


###################
##NAME GENERATION##
###################

global letter_count
letter_count = 0
global name1

#Identifies features of each letter, to ensure letters such as a uppercase isn't added to the code
class letter():
    def __init__(self, lowerchar, upperchar, is_vowel, is_consonant):
        global letter_count
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.is_vowel = is_vowel
        self.is_consonant = is_consonant
        self.num = letter_count
        letter_count += 1


def normalize(prob):
    global alphabet
    new_prob = prob
    for i in range(0, len(alphabet)):
        total = sum(prob[i])
        if total != 0:
            for j in range(0, len(alphabet)):
                new_prob[i][j] = prob[i][j] / total
        else:
            equal_prob = 1.0 / len(alphabet)
            for j in range(0, len(alphabet)):
                new_prob[i][j] = equal_prob
    return new_prob


#Defines the alphabet
global alphabet
alphabet = [letter('a', 'A', True, False),
            letter('b', 'B', False, True),
            letter('c', 'C', False, True),
            letter('d', 'D', False, True),
            letter('e', 'E', True, False),
            letter('f', 'F', False, True),
            letter('g', 'G', False, True),
            letter('h', 'H', False, True),
            letter('i', 'I', True, False),
            letter('j', 'J', False, True),
            letter('k', 'K', False, True),
            letter('l', 'L', False, True),
            letter('m', 'M', False, True),
            letter('n', 'N', False, True),
            letter('o', 'O', True, False),
            letter('p', 'P', False, True),
            letter('q', 'Q', False, True),
            letter('r', 'R', False, True),
            letter('s', 'S', False, True),
            letter('t', 'T', False, True),
            letter('u', 'U', True, False),
            letter('v', 'V', False, True),
            letter('w', 'W', False, True),
            letter('x', 'X', False, True),
            letter('y', 'Y', True, True),
            letter('z', 'Z', False, True)
            ]
#Reads the current probabilities of letters appearing next to each other and records these probabilities for future use
global prob
file_name = 'default prob.csv'
prob = [[0] * len(alphabet) for _ in range(len(alphabet))] 
with open(file_name, newline='') as csvfile:
    prob_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in prob_reader:
        for i in range(len(row)):
            prob[len(prob) - 1][i] = float(row[i])
            

#Everytime the code runs it checks the file incase any updates have been made and will slightly adjust the probability based on ALL values
file_name = 'stand names.csv'
with open(file_name, newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for names in name_reader:
        name = names[0]
        for i in range(0, len(name) - 1):
            letter1 = name[i]
            letter2 = name[i + 1]
            num1 = 0
            num2 = 0
            for i in range(0, len(alphabet)):
                if (letter1 == alphabet[i].lowerchar or letter1 == alphabet[i].upperchar):
                    num1 = alphabet[i].num
                if (letter2 == alphabet[i].lowerchar or letter2 == alphabet[i].upperchar):
                    num2 = alphabet[i].num
            prob[num1][num2] += 1

prob = normalize(prob)
file_name = 'stand names.csv'  
for i in range(0, len(alphabet)):
    total = 0
    for j in range(0, len(alphabet)):
        total += prob[i][j]
    for j in range(0, len(alphabet)):
        prob[i][j] /= total

def rand_int(x1, x2):
    r = int(int(x1) + random() * (int(x2) - int(x1)))
    return r


#Generates a name based on these probabilities
def make_name():
    name_length = rand_int(2, 15)

    my_name = ""

    prev_vowel = False
    prev_consonant = False
    prev2_vowel = False
    prev2_consonant = False
    prev_num = 0

    for i in range(0, name_length):
        if (i == 0):
            a = alphabet[rand_int(0, 25)]
            my_name = my_name + a.upperchar
        else:
            a = get_letter(prev_num, prev2_vowel, prev2_consonant)
            my_name = my_name + a.lowerchar
        prev2_vowel = (a.is_vowel and prev_vowel)
        prev2_consonant = (a.is_consonant and prev_consonant)
        prev_vowel = a.is_vowel
        prev_consonant = a.is_consonant
        prev_num = a.num
    return my_name

def get_letter(prev_num, need_consonant, need_vowel):
    global alphabet
    done = False
    while (not done):
        a = pick_letter(prev_num)
        if ((need_consonant and a.is_vowel) or (need_vowel and a.is_consonant)):
            done = False
        else:
            done = True
    return a

def pick_letter(i):
    global prob
    r = random()
    total = 0
    for j in range(0, len(alphabet)):
        total += prob[i][j]
        if (r <= total or j == len(alphabet)):
            return alphabet[j]
    print("problem!")
    return alphabet(25)

name1 = make_name()


import csv

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_pairs = {letter1 + letter2: 0 for letter1 in alphabet for letter2 in alphabet}

file_name = 'stand names.csv'
with open(file_name, newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for names in name_reader:
        name = names[0]
        for i in range(0, len(name) - 1):
            letter1 = name[i].lower()
            letter2 = name[i + 1].lower()
            if letter1 + letter2 in letter_pairs:
                letter_pairs[letter1 + letter2] += 1

total_counts = sum(letter_pairs.values())

letter_pair_probabilities = {pair: count / total_counts for pair, count in letter_pairs.items()}


import csv

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_pairs = {letter1 + letter2: 0 for letter1 in alphabet for letter2 in alphabet}

file_name = 'stand names.csv'
with open(file_name, newline='') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for names in name_reader:
        name = names[0]
        for i in range(0, len(name) - 1):
            letter1 = name[i].lower()
            letter2 = name[i + 1].lower()
            if letter1 + letter2 in letter_pairs:
                letter_pairs[letter1 + letter2] += 1

total_counts = sum(letter_pairs.values())

letter_pair_probabilities = {pair: count / total_counts for pair, count in letter_pairs.items()}

probabilities_file = 'default prob.csv'
with open(probabilities_file, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for letter1 in alphabet:
        row = []
        for letter2 in alphabet:
            pair = letter1 + letter2
            row.append(letter_pair_probabilities.get(pair, 0))
        writer.writerow(row)




#################
##BUTTON ACTION##
#################

def generate_stand():
    
    name_label.config(text=f"Generated Name: {name1} ")
    prompt_text = prompt_entry.get()
    if prompt_text != "":
        name2=prompt_text
        name_label.config(text=f"Generated Name: {name2} ")
        

    
    ####################
    ##SKILL GENERATION##
    ####################
    
    if prompt_text != "":
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Create a list of 3 unique abilities for a Jojo's Bizarre Adventure stand called " +name2}
                        ]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Create a list of 3 unique abilities for a Jojo's Bizarre Adventure stand called " +name1}
                        ]
        )
        
    
    skills = response.choices[0].message.content
    skill_label.config(text=f"Generated Skills: {skills}")
    
    
    ####################
    ##IMAGE GENERATION##
    ####################
    #Generates an AI image of the stand and opens within a web browser using OpenAI dall-e 3
    
    if prompt_text != "":
        response = client.images.generate(
              model="dall-e-3",
              prompt="A stand called " + name2 + "in the style of Jojo's Bizarre adventure",
              size="1024x1024",
              quality="standard",
              n=1,
            )
    else:
        response = client.images.generate(
              model="dall-e-3",
              prompt="A stand called " + name1 + "in the style of Jojo's Bizarre adventure",
              size="1024x1024",
              quality="standard",
              n=1,
            )
        

    image_url = response.data[0].url

    
    urllib.request.urlretrieve(image_url, "stand.png")
    

    ####################
    ##CHART GENERATION##
    ####################

    categories = ['Destructive Power', 'Speed', 'Range', 'Stamina', 'Precision', 'Development Potential']

    fig = go.Figure()

    power = randint(0,5)
    speed = randint(0,5)
    srange = randint(0,6)
    stamina = randint(0,6)
    precision = randint(0,5)
    potential = randint(0,6)

    fig.add_trace(go.Scatterpolar(r=[power,speed,srange,stamina,precision,potential], theta=categories, fill='toself', name='A'))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True, range=[0,6]
            )),
        showlegend=False
    )
    fig.write_image("figure.png")
    display_image()

    
#################
##DISPLAY IMAGE##
#################

def display_image():
    figureimage_path = "figure.png" 
    figureimage = Image.open(figureimage_path)
    # Resize the images to fit
    figureimage = figureimage.resize((300, 300), Image.BILINEAR)
    figurephoto = ImageTk.PhotoImage(figureimage)
    
    # Set the image on the label
    figureimage_label.config(image=figurephoto)
    figureimage_label.image = figurephoto 
    
    standimage_path = "stand.png" 
    standimage = Image.open(standimage_path)
    # Resize the images to fit
    standimage = standimage.resize((200, 200), Image.BILINEAR)
    standphoto = ImageTk.PhotoImage(standimage)
    
    # Set the image on the label
    standimage_label.config(image=standphoto)
    standimage_label.image = standphoto  

###############
##GUI PORTION##
###############

root = tk.Tk()
root.title("JJBA Stand Generator")
window_width = 900
window_height = 800
root.geometry(f"{window_width}x{window_height}")
root.configure(bg="#d8bfd8")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="#ffffff", background="#4b0082", font=('Arial', 12, 'bold'))
style.map("TButton", foreground=[('active', '#ffffff')], background=[('active', '#5a1c8b')])

#Frame
frame = ttk.Frame(root, padding="20", style='Custom.TFrame')
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
style.configure('Custom.TFrame', background="#d8bfd8")




#Title
title_label = ttk.Label(frame, text="Jojo's Bizarre Stand Generator", font=('Arial', 18, 'bold'), background="#d8bfd8", foreground="#4b0082")
title_label.grid(row=0, column=0, pady=10)

prompt_entry = ttk.Entry(frame)
prompt_entry.grid(row=2, column=0, padx=(0, 10), pady=10)


#Button
generate_button = ttk.Button(frame, text="Generate Stand", command=generate_stand)
generate_button.grid(row=3, column=0, pady=10)

#Labels
name_label = ttk.Label(frame, text="Stand Name: ", wraplength=700)
name_label.grid(row=4, column=0)
name_label.configure(background="#d8bfd8", foreground="#4b0082")

skill_label = ttk.Label(frame, text="Stand Skills: ", wraplength=900)
skill_label.grid(row=6, column=0)
skill_label.configure(background="#d8bfd8", foreground="#4b0082")

#Images
figureimage_label = ttk.Label(frame)
figureimage_label.grid(row=7, column=0, columnspan=2)

standimage_label = ttk.Label(frame)
standimage_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
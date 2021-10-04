from tkinter import *
from requests_html import HTML, HTMLSession
import tkinter as tk
import validators
from tkinter.messagebox import *
root = tk.Tk()
root.geometry("500x500")
country_name = tk.StringVar()
root.title("Covid-19 Tracker")


def extract_info(country_name):
    country_print = str(country_name.get())
    session = HTMLSession()
    url = 'https://www.worldometers.info//coronavirus/country/'
    url_con = url+country_print
    valid = validators.url(url_con)
    if valid == True:
        print("Hello true")
        r = session.get(url_con)
        body = r.html.find('body')
        article = r.html.find('.content-inner', first=True).text
        lines = (line.strip() for line in article.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        text1 = text.splitlines()
        label_heading = Label(text=text1[5], font=('arial', 10, 'bold'))
        label_heading.place(x=240, y=125)
        label_heading = Label(text=text1[7], font=('arial', 10, 'bold'))
        label_heading.place(x=240, y=145)
        label_heading = Label(text=text1[9], font=('arial', 10, 'bold'))
        label_heading.place(x=240, y=165)
    else:
        print("Hello false")
        #showinfo("notification", "Enter the valid country!!!")


label_heading = Label(text='Enter the country name', font=('arial', 16, 'bold'))
label_heading.place(x=140, y=15)
country_entry = tk.Entry(root, textvariable=country_name, font=('calibre', 12, 'normal'))
country_entry.place(x=160, y=55)
btn = tk.Button(root, text='Submit', font=('arial', 12, 'bold'), command=lambda: extract_info(country_name))
btn.place(x=200, y=85)
label_heading = Label(text='Cases:', font=('arial', 10, 'bold'))
label_heading.place(x=170, y=125)
label_heading = Label(text='Death:', font=('arial', 10, 'bold'))
label_heading.place(x=170, y=145)
label_heading = Label(text='Recovery:', font=('arial', 10, 'bold'))
label_heading.place(x=170, y=165)
root.mainloop()
from tkinter import *
from tkinter import ttk#for combo box
import requests
from PIL import Image, ImageTk
import random

weather_quotes = {
    "sunny": [
        "The sun is shining, the birds are singing!",
        "It's a beautiful day! Enjoy the sunshine!",
        "Let the sunshine fill your soul!"
    ],
    "rainy": [
        "Rain, rain, go away, come back another day!",
        "The rain brings new growth to the earth.",
        "After the rain comes the rainbow!"
    ],
    "cloudy": [
        "The sky is cloudy, but the weather is still nice.",
        "Clouds may hide the sun, but they can't hide the beauty!",
        "Sometimes, the clouds just want a little break."
    ],
    "snow": [
        "Let it snow, let it snow, let it snow!",
        "Snowflakes are the butterflies of winter.",
        "Every snowflake is a kiss on the cheek of winter."
    ],
    "clear": [
        "Clear skies ahead, enjoy the view!",

        "What a perfect, clear sky to gaze ."
    ],
}

def data_get():
    city=city_name.get()#city name
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c357c27a11412d1c65b44a721dfcb5a5").json()
    weather_main = data["weather"][0]["main"].lower() 
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    t_label1.config(text=str(data["main"]["temp"]-273.15))
    p_label1.config(text=data["main"]["pressure"])
    show_weather_quote(weather_main)

def show_weather_quote(weather):
    # Get a random quote based on weather
    quotes = weather_quotes.get(weather, ["Have a nice day!"])  # Default to a neutral message if no quotes found
    quote = random.choice(quotes)
    quote_label.config(text=quote) 


win=Tk()#object of win
win.title("weather_app")#title
win.geometry("700x700")#size of box

background_image = Image.open("C:\\Users\\Sanmati Tighare\\politicans project\\bg1 (1).jpeg")  
background_image = background_image.resize((700, 700))  # Resize the image to fit the window
bg_img = ImageTk.PhotoImage(background_image)

# Create a canvas to hold the background image
canvas = Canvas(win, width=700, height=700)
canvas.create_image(0, 0, anchor=NW, image=bg_img)
canvas.pack()

label_name=Label(win,text="WeatherSphere",font=("Roboto",50,"bold"),bg="white")
label_name.place(x="50",y="50",height="75",width='600')

city_name=StringVar()
list_name= [
    "Agra", "Ahmedabad", "Bangalore", "Bhopal", "Chandigarh",
    "Chennai", "Coimbatore", "Faridabad", "Ghaziabad", "Guwahati",
    "Hyderabad", "Indore", "Jaipur", "Jabalpur", "Kochi",
    "Kolhapur", "Kolkata", "Lucknow", "Madurai", "Meerut",
    "Mumbai", "Nagpur", "Navi Mumbai", "Patna", "Pune",
    "Raipur", "Ranchi", "Surat", "Vadodara", "Vijayawada",
    "Visakhapatnam"



]
com=ttk.Combobox(win,text="WeatherSphere",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x="100",y="175",height="50",width="500")



w_label=Label(win,text="Weather climate",font=("Time New Roman",25),bg="light blue")
w_label.place(x="25",y="360",height="50",width="300")
w_label1=Label(win,text="",font=("Time New Roman",25),bg="light blue")
w_label1.place(x="375",y="360",height="50",width="300")

wd_label=Label(win,text="Weather description ",font=("Time New Roman",25),bg="light blue")
wd_label.place(x="25",y="430",height="50",width="300")
wd_label1=Label(win,text=" ",font=("Time New Roman",25),bg="light blue")
wd_label1.place(x="375",y="430",height="50",width="300")


t_label=Label(win,text="Temperature ",font=("Time New Roman",25),bg="light blue")
t_label.place(x="25",y="500",height="50",width="300")
t_label1=Label(win,text="",font=("Time New Roman",25),bg="light blue")
t_label1.place(x="375",y="500",height="50",width="300")


p_label=Label(win,text="Pressure ",font=("Time New Roman",25),bg="light blue")
p_label.place(x="25",y="570",height="50",width="300")
p_label1=Label(win,text="",font=("Time New Roman",25),bg="light blue")
p_label1.place(x="375",y="570",height="50",width="300")


quote_label = Label(win, text="", font=("Time New Roman", 18), wraplength=600, justify="center", fg="black",bg="grey")
quote_label.place(x=50, y=640, height=35, width=600)

done_button=Button(win,text="Done",font=("Times New Roman",10,"bold"),command=data_get)
done_button.place(x="300",y="250",height="30",width="100")

win.mainloop()
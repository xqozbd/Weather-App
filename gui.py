#Import the necessary libraries
import tkinter as tk
import backend

#Configure the GUI
gui = tk.Tk()
gui.title("Weather App")
gui.geometry("350x200")
gui.configure(bg="#e8e8e8")

# Ask user for city and state
def weather_grab():
    city = city_entry.get()
    state = state_entry.get()
    weather_data = backend.get_weather_data(city, state)
    if weather_data:
        #Grab the current weather data
        tempature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_mph']
        #Convert metric to imperial
        tempature = tempature * 9/5 + 32
        wind_speed = wind_speed * 0.621371
        wind_speed = round(wind_speed, 2)
        tempature = round(tempature)
        #Give user the weather data
        print(f"Temperature: {tempature}°F")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind_speed} mp/h")

        #Concatenate the weather data
        displayedData = f"Temperature: {tempature}°F\nCondition: {condition}\nHumidity: {humidity}%\nWind: {wind_speed} mp/h"
        result_label.config(text=displayedData)


# Make city text entry
tk.Label(gui, text="Enter city name:").pack()
city_entry = tk.Entry(gui)
city_entry.pack()
# Make state text entry
tk.Label(gui, text="Enter state name abbreviation:").pack()
state_entry = tk.Entry(gui)
state_entry.pack()

# Make submit button
tk.Button(gui, text="Submit", command=weather_grab).pack()

result_label = tk.Label(gui, text="", font=("Helvetica", 16), justify="left")
result_label.pack()

# Display the GUI
gui.mainloop()
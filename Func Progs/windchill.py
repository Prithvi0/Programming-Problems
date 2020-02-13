"""Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be: 
35.74 + 0.625 * t + (0.4275 * t - 35.75) * (v**0.16)"""

def wc(temperature,windspeed):
    
    try:

        # program runs until its true
        while True:
            
            # the formula is not valid if abs(t) > 50 or if v > 120 < 3
            if (abs(temperature) > 0 and windspeed > 3 and windspeed < 120):
                return "temperature:",temperature,"windspeed:",windspeed,"windchill:",windchill
    
            else:
                return "Please Enter valid temperature and windspeed"
    
    except ValueError:
        return "Invalid input"

temperature = int(input("Enter the temperature between 0 to 50:"))
windspeed = int(input("Enter the windspeed between 0 to 120:"))
windchill = float(35.74 + 0.625 * temperature + (0.4275 * temperature - 35.75) * (windspeed**0.16))

print(wc(temperature,windspeed))
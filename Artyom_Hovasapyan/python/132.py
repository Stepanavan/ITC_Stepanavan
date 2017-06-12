import pyown
owm = pyowm.OWM('f87220e17fe2a94a658a040f2d98a517')
observation = owm.weather_at_place('London')
w = observation.get_weather()
print(w)

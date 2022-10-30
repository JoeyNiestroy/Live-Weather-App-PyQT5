from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys
import requests, json

"""Hard Coded Vars for Weather API, api_key has been removed"""
api_key = "api_key_for_weathermap"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "District of Columbia"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name


"""Conversion Function for K to F"""
def k_to_f(k):
    return 1.8*(k-273) + 32


"""Returns string value for live weather data"""
def return_live_weather():
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        data = data["main"]
        y = data['temp']
        current_temperature = y
        return str(round(k_to_f(current_temperature)))+"°"
    else:
        return("Live Weather Failure")

"""Setting up PyQT5 App Class"""
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
    """Button Update Function, calls API Function"""
    def button_clicked(self):
        self.label.setText(return_live_weather())
    
    def initUI(self):
        self.setGeometry(600, 600, 400, 400)
        self.setWindowTitle("Live Weather!")

        """Creates and modifys label for degree"""
        self.label = QtWidgets.QLabel("Arial Font",self)
        self.label.setText(return_live_weather())
        self.label.setFont(QFont("Arial", 30))
        self.label.move(145,80)
        self.label.resize(150, 150)
        """Creates and modifys PushButton Widget"""
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Update Weather")
        self.b1.move(135,250)
        self.b1.resize(120,50)
        self.b1.clicked.connect(self.button_clicked)


"""Function to start App"""
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()

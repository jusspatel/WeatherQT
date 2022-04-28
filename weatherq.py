
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('weather.png'))
        MainWindow.resize(398, 71)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 237, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("\n"
"QLineEdit {\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
" border: 2px solid gray;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 141, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 13pt \"Segoe UI Semilight\";\n"
"background-color: rgb(0, 72, 216);\n"
"color: rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::Pressed{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 54, 161);\n"
"font: 13pt \"Segoe UI Semilight\";\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{background-color: rgb(0, 0, 255);}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 51))
        self.label.setStyleSheet("font: 63 36pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 53, 47, 21))
        self.label_2.setStyleSheet("font: 25 14pt \"Segoe UI Light\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 83, 47, 21))
        self.label_3.setStyleSheet("font: 25 14pt \"Segoe UI Light\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 50, 111, 26))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Light\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 50, 31, 26))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Light\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 80, 151, 26))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 13pt \"Segoe UI Light\";")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(305, 50, 81, 52))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../01d@4x.png"))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 111, 144, 21))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 144, 141, 21))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 209, 141, 21))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(146, 111, 47, 21))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(152, 142, 47, 25))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(148, 209, 41, 21))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 178, 141, 21))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(148, 178, 41, 21))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 241, 141, 21))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(147, 244, 41, 21))
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(205, 111, 106, 21))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(315, 112, 47, 21))
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(205, 144, 106, 21))
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(315, 144, 47, 21))
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(205, 178, 91, 21))
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(300, 178, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(205, 210, 61, 21))
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(270, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(205, 244, 61, 21))
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI Semilight\";")
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(270, 244, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "27"))
        self.label_2.setText(_translate("MainWindow", "28"))
        self.label_3.setText(_translate("MainWindow", "25"))
        self.label_4.setText(_translate("MainWindow", "Kanpur"))
        self.label_5.setText(_translate("MainWindow", "IN"))
        self.label_7.setText(_translate("MainWindow", "2021-06-02 21:54:02"))
        self.label_8.setText(_translate("MainWindow", "Visibilty (m):"))
        self.label_9.setText(_translate("MainWindow", "Wind Speed (km/h):"))
        self.label_10.setText(_translate("MainWindow", "Feels like (C) :"))
        self.label_11.setText(_translate("MainWindow", "3000"))
        self.label_12.setText(_translate("MainWindow", "3000"))
        self.label_13.setText(_translate("MainWindow", "28"))
        self.label_14.setText(_translate("MainWindow", "Wind Direction :"))
        self.label_15.setText(_translate("MainWindow", "W"))
        self.label_16.setText(_translate("MainWindow", "AQI :"))
        self.label_17.setText(_translate("MainWindow", "211"))
        self.label_18.setText(_translate("MainWindow", "Pressure (hPa):"))
        self.label_19.setText(_translate("MainWindow", "3000"))
        self.label_20.setText(_translate("MainWindow", "Humidity (%)"))
        self.label_21.setText(_translate("MainWindow", "10"))
        self.label_22.setText(_translate("MainWindow", "Description :"))
        self.label_23.setText(_translate("MainWindow", "clear sky"))
        self.label_24.setText(_translate("MainWindow", "Sunrise :"))
        self.label_25.setText(_translate("MainWindow", "ae"))
        self.label_26.setText(_translate("MainWindow", "Sunset :"))
        self.label_27.setText(_translate("MainWindow", "ae"))
        self.pushButton.clicked.connect(self.getInput)
        import geocoder
        g = geocoder.ip('me')
        city = g.city
        API = "http://api.openweathermap.org/data/2.5/weather?appid=YOURAPIKEYHERE&q={}".format(city)
        response = requests.get(API)
        x = response.json()
        self.label_4.setText(x["name"])
        self.label_5.setText(x["sys"]["country"])
        value = datetime.datetime.fromtimestamp(x["dt"])
        self.label_7.setText(value.strftime('%Y-%m-%d %H:%M:%S'))
        self.label_11.setText(str(x["visibility"]))
        self.label_12.setText(str(x["wind"]["speed"]))
        mainTemp = int(x["main"]["temp"]) - 273
        self.label.setText(str(mainTemp))
        maxTemp = int(x["main"]["temp_max"]) - 273
        self.label_2.setText(str(maxTemp))
        minTemp = int(x["main"]["temp_min"]) - 273
        self.label_3.setText(str(minTemp))
        def degToCompass(num):
                val=int((num/22.5)+.5)
                arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
                return arr[(val % 16)]
        self.label_15.setText(degToCompass(x["wind"]["deg"]))
        FeelsLike = int(x["main"]["feels_like"]) - 273
        self.label_13.setText(str(FeelsLike))
        aqi = "https://api.waqi.info/feed/"+city+"/?token=YOURAPIKEYHERE"
        response1 = requests.get(aqi)
        y = response1.json()
        self.label_17.setText(str(y["data"]["aqi"]))
        self.label_19.setText(str(x["main"]["pressure"]))
        self.label_21.setText(str(x["main"]["humidity"]))
        self.label_23.setText(str(x["weather"][0]["main"]))
        sunrise = datetime.datetime.fromtimestamp(x["sys"]["sunrise"])
        self.label_25.setText(sunrise.strftime('%H:%M:%S'))
        sunset = datetime.datetime.fromtimestamp(x["sys"]["sunset"])
        self.label_27.setText(sunset.strftime('%H:%M:%S'))
        icon = x["weather"][0]["icon"]
        url = "http://openweathermap.org/img/wn/"+icon+"@2x.png"
        response2 = requests.get(url)
        z = response2.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(z)
        self.label_6.setPixmap(pixmap)
        MainWindow.resize(398,290)
        MainWindow.setFixedSize(398,290)


    def getInput(self):
        
        city = self.lineEdit.text()
        API = "http://api.openweathermap.org/data/2.5/weather?appid=YOURAPIKEYHERE&q={}".format(city)
        response = requests.get(API)
        x = response.json()
        self.label_4.setText(x["name"])
        self.label_5.setText(x["sys"]["country"])
        value = datetime.datetime.fromtimestamp(x["dt"])
        self.label_7.setText(value.strftime('%Y-%m-%d %H:%M:%S'))
        self.label_11.setText(str(x["visibility"]))
        self.label_12.setText(str(x["wind"]["speed"]))
        mainTemp = int(x["main"]["temp"]) - 273
        self.label.setText(str(mainTemp))
        maxTemp = int(x["main"]["temp_max"]) - 273
        self.label_2.setText(str(maxTemp))
        minTemp = int(x["main"]["temp_min"]) - 273
        self.label_3.setText(str(minTemp))
        def degToCompass(num):
                val=int((num/22.5)+.5)
                arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
                return arr[(val % 16)]
        self.label_15.setText(degToCompass(x["wind"]["deg"]))
        FeelsLike = int(x["main"]["feels_like"]) - 273
        self.label_13.setText(str(FeelsLike))
        aqi = "https://api.waqi.info/feed/"+city+"/?token=YOURAPIKEYHERE"
        response1 = requests.get(aqi)
        y = response1.json()
        self.label_17.setText(str(y["data"]["aqi"]))
        self.label_19.setText(str(x["main"]["pressure"]))
        self.label_21.setText(str(x["main"]["humidity"]))
        self.label_23.setText(str(x["weather"][0]["main"]))
        sunrise = datetime.datetime.fromtimestamp(x["sys"]["sunrise"])
        self.label_25.setText(sunrise.strftime('%H:%M:%S'))
        sunset = datetime.datetime.fromtimestamp(x["sys"]["sunset"])
        self.label_27.setText(sunset.strftime('%H:%M:%S'))
        icon = x["weather"][0]["icon"]
        url = "http://openweathermap.org/img/wn/"+icon+"@2x.png"
        response2 = requests.get(url)
        z = response2.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(z)
        self.label_6.setPixmap(pixmap)
        MainWindow.resize(398,290)
        MainWindow.setFixedSize(398,290)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#Jackson's Code

import json
import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *



# this part will also return a field called place_id, which can be inputted into a place_details request to return specific data about the location such as consumer reviews


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ begin UI Code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# the only package ya gotta download is PyQt! https://riverbankcomputing.com/software/pyqt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~SETUP NONSENSE~~~~~~~~~~~~~~~~~~~~~~~~~~~#



#makes a new app
app = QApplication(sys.argv)
#the default widget QWidget makes a window
window = QWidget()
window.setWindowTitle('Bad Yelp')

#just for kicks(and best practices/changeability!)
xWinSize = 1200
yWinSize = 600
#position on screen x & y , size x & y
window.setGeometry(0, 0, xWinSize, yWinSize)

#~~~~~~~~~~~~~~~~~~~~~~~~~~WIDGETS, LABELS, ETC~~~~~~~~~~~~~~~~~~~~~~~~~#
#OUTPUT:
#Whatever is typed in the box
#INPUT:
#The index numbers of the top 5 results for that search term



logoImage = QPixmap("C:/Users/Noahc/OneDrive/Pictures/Saved Pictures/rainbow.png")
logoLabel = QLabel(parent=window)
logoLabel.setPixmap(logoImage)
logoLabel.setFixedSize(500,200)

grayImage = QPixmap("C:/Users/Noahc/OneDrive/Pictures/Saved Pictures/gray.png")
gray = QLabel(parent=window)
gray.setPixmap(grayImage)
gray.setFixedSize(50,600)

topImage = QPixmap("C:/Users/Noahc/OneDrive/Pictures/Saved Pictures/reasonhasabandonedus.png")
topLabel = QLabel(parent=window)
topLabel.setPixmap(topImage)
topLabel.setFixedSize(500,170)



#display1 = ( " "  )
contentDisp1 = QLabel(parent=window)
contentDisp1.setWordWrap(True)
#contentDisp1.move(780,0)
contentDisp1.setFixedWidth(700)
#contentDisp1.setText(display1)
contentDisp1.setStyleSheet("border: 2px solid black;")
contentDisp1.setFont(QFont('Times', 20))

#display2 = ( "  "  )
contentDisp2 = QLabel(parent=window)
contentDisp2.setWordWrap(True)
#contentDisp2.move(780,160)
contentDisp2.setFixedWidth(700)
#contentDisp2.setText(display2)
contentDisp2.setStyleSheet("border: 2px solid black;")
contentDisp2.setFont(QFont('Times', 20))


#display3 = ( "  "  )
contentDisp3 = QLabel(parent=window)
contentDisp3.setWordWrap(True)
#contentDisp3.move(780,320)
contentDisp3.setFixedWidth(700)
#contentDisp3.setText(display3)
contentDisp3.setStyleSheet("border: 2px solid black;")
contentDisp3.setFont(QFont('Times', 20))


#display4 = ( " "  )
contentDisp4 = QLabel(parent=window)
contentDisp4.setWordWrap(True)
#contentDisp4.move(780,480)
contentDisp4.setFixedWidth(700)
#contentDisp4.setText(display4)
contentDisp4.setStyleSheet("border: 2px solid black;")
contentDisp4.setFont(QFont('Times', 20))


#display5 = ( " "  )
contentDisp5 = QLabel(parent=window)
contentDisp5.setWordWrap(True)
#contentDisp5.move(780,640)
contentDisp5.setFixedWidth(700)
#contentDisp5.setText(display5)
contentDisp5.setStyleSheet("border: 2px solid black;")
contentDisp5.setFont(QFont('Times', 20))

pageTitle = QLabel('<h1>NIGHTMARENIGHTMARENIGHTMARE</h1>')
subHeading = QLabel('<h2>Which factors do you want to consider?</h2>')
c1 = QCheckBox("Rating ")
c1.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }");
c2 = QCheckBox("Distance")
c2.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }");
c3 = QCheckBox("Popularity")
c3.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }");
c4 = QCheckBox("Cost")
c4.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }");
c5 = QCheckBox("Open")
c5.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }");

in1 = QLineEdit()
in1.setFixedWidth(500)


search = QPushButton("Search")
search.setFixedWidth(500)
search.setCheckable(True)
search.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')





#	in1.clear()
#searchOut = in1.text()



#random = QLabel("Random")
#space = QLabel('___________________________________________________________________________________________________________________________________', parent=window)
#space2 = QLabel('___________________________________________________________________________________________________________________________________', parent=window)

#out1 = QLabel("                                     place oneeeeeeeeeeeeeeeeee")


#USING A 36 x 72 GRID

checkLayout = QGridLayout()
checkLayout.addWidget(topLabel,0,0,8,28)              #pageTitle,0,0,8,28)
checkLayout.addWidget(subHeading,10,0,2,28)
checkLayout.addWidget(c1,12,0,2,28)
checkLayout.addWidget(c2,14,0,2,28)
checkLayout.addWidget(c3,16,0,2,28)
checkLayout.addWidget(c4,18,0,2,28)
checkLayout.addWidget(c5,20,0,2,28)
checkLayout.addWidget(in1,22,0,2,28)
#checkLayout.addWidget(space,7,1,)
checkLayout.addWidget(search,24,0,2,28)
checkLayout.addWidget(logoLabel,26,0,12,28)
checkLayout.addWidget(gray,0,30,36,4)

checkLayout.addWidget(contentDisp1,1,34,7,38)
checkLayout.addWidget(contentDisp2,8,34,7,38)
checkLayout.addWidget(contentDisp3,15,34,7,38)
checkLayout.addWidget(contentDisp4,22,34,7,38)
checkLayout.addWidget(contentDisp5,29,34,7,38)
#checkLayout.addWidget(space2,8,1)

window.setLayout(checkLayout)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXECUTION STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~API STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def go():
    searchOut = in1.text()
    print("Your search query was: " + searchOut)
    in1.clear()

    keyword = searchOut
    # accepted types: https://developers.google.com/maps/documentation/places/web-service/supported_types
    radius = '10000'
    coord1 = '39.5481' #lattitude
    coord2 = '-104.9739' #longitude
    location = coord1 + '%2C' + coord2 #compiles coordinate into usable
    API_KEY = 'AIzaSyCmvD0GGssDQbaKG6U6xscR7p81FqRGmr8' #API access key
    url1 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + "location=" + location + "&radius=" + radius  + "&keyword=" + keyword + "&key=" + API_KEY

    payload={}
    headers = {}

    response = requests.request("GET", url1, headers=headers, data=payload)
    data = json.loads(response.text)
    #this will place the data in a names json file in the same directory as the python file
    fileName = 'fblaStoredData.json' #replace me!
    file = open(fileName, "w")
    json.dump(data, file)
    file.close()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RESULT PROCESSING STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



    #assigns boolean truth values to variables to represent which factors are being considered
    # creates a dictionary of all the possible factors
    #(GIVE THESE IF STATEMENTS TO SET THEM TO TRUE OR FALSE DEPENDING ON WHAT THE UI PASSES IN
    rating = True
    distance = True #will have to be determined by finding the diff. between a result's lat & long and coord1 & coord2
    popularity = True #number of reviews
    isOpen = True
    factors = {'rating': rating , 'distance': distance , 'popularity': popularity, 'isOpen' : isOpen }

    #reads the .json file from the API
    #( FILEPATH WILL NEED TO BE UPDATED)
    with open("C:/Users/Jackson Star/Desktop/Projects/FBLA Test/fblaStoredData.json", 'r') as inFile:
        input0 = inFile.read()
    #Converts the .json file into a dictionary. THIS RETURN IS A DICTIONARY OF LISTS OF DICTIONARIES.
    dict0 = json.loads(input0)

    #Loops for every potential boolean factor and adds to the selection value of the top five in each category
    #CHANGE TO A FOR LOOP THAT ONLY ITERATES FOR THE SELECTED NUMBER OF FACTORS (LOW PRIORITY)

    #for i in range (len(dict0['results'])):
    # if(  ((dict0['results'])[i])[] == 'true' ):
    #  print(((dict0['results'])[i])[ ('opening_hours') ]     )

    #  print(i)
    #   print((dict0['results'])[i])
    #  print ( ((dict0['results'])[i])['business_status'] )


    #creates a dictionary to keep track of how desirable each result is (its selection value)

    #removes all but the top 5 entries in the selection value dictionary
    #returns desired info on each entry into a text box in the UI

    #for i in range(5):
    #print( ((dict0['results'])[i])['name'])

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RETURNS TO API~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    display1 = ( "<h5> <font size='-1'>" + ((dict0['results'])[0])['name']  + "</h5> <lb> <p> <font size='-1'>"  + ((dict0['results'])[0])['vicinity'] + "</p>"  )
    print(display1)
    contentDisp1.setText(display1)

    display2 = ( "<h5> <font size='-1'>" + ((dict0['results'])[1])['name']  + "</h5> <lb> <p> <font size='-1'>" + ((dict0['results'])[1])['vicinity'] + "</p>"  )
    print(display2)
    contentDisp2.setText(display2)

    display3 = ( "<h5> <font size='-1'>" + ((dict0['results'])[2])['name']  + "</h5> <lb> <p> <font size='-1'>" + ((dict0['results'])[2])['vicinity'] + "</p>"  )
    print(display3)
    contentDisp3.setText(display3)

    display4 = ( "<h5> <font size='-1'>" + ((dict0['results'])[3])['name']  + "</h5> <lb> <p> <font size='-1'>" + ((dict0['results'])[3])['vicinity'] + "</p>"  )
    print(display4)
    contentDisp4.setText(display4)

    display5 = ( "<h5> <font size='-1'>" + ((dict0['results'])[4])['name']  + "</h5> <lb> <p> <font size='-1'>" + ((dict0['results'])[4])['vicinity'] + "</p>"  )
    print(display5)
    contentDisp5.setText(display5)

search.clicked.connect(go)

window.show()

#runs the main loop for the app
sys.exit(app.exec_())
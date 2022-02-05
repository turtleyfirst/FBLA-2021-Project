#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ begin UI Code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# the only package ya gotta download is PyQt! https://riverbankcomputing.com/software/pyqt

#~~~~~~~~~~~~~~~~~~~~~~~~~~~SETUP NONSENSE~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *




#makes a new app
app = QApplication(sys.argv)
#the default widget QWidget makes a window
window = QWidget()
window.setWindowTitle('Bad Yelp')

#just for kicks(and best practices/changeability!)
xWinSize = 1200
yWinSize = 800
#position on screen x & y , size x & y
window.setGeometry(0, 0, xWinSize, yWinSize)

#~~~~~~~~~~~~~~~~~~~~~~~~~~WIDGETS, LABELS, ETC~~~~~~~~~~~~~~~~~~~~~~~~~#
#go mad with this!
#sets a label to an image
logoImage = QPixmap("C:/Users/turtl/Desktop/close.png")
logoLabel = QLabel(parent=window)
logoLabel.setPixmap(logoImage)


display1 = ""
contentDisp1 = QLabel(parent=window)
contentDisp1.setWordWrap(True)
contentDisp1.move(780,0)
contentDisp1.setFixedWidth(400)
contentDisp1.setText(display1)
contentDisp1.setStyleSheet("border: 2px solid black;")
contentDisp1.setFont(QFont('Arial', 20))


display2 = ""
contentDisp2 = QLabel(parent=window)
contentDisp2.setWordWrap(True)
contentDisp2.move(780,160)
contentDisp2.setFixedWidth(400)
contentDisp2.setText(display2)
contentDisp2.setStyleSheet("border: 2px solid black;")
contentDisp2.setFont(QFont('Arial', 20))


display3 = ""
contentDisp3 = QLabel(parent=window)
contentDisp3.setWordWrap(True)
contentDisp3.move(780,320)
contentDisp3.setFixedWidth(400)
contentDisp3.setText(display3)
contentDisp3.setStyleSheet("border: 2px solid black;")
contentDisp3.setFont(QFont('Arial', 20))


display4 = ""
contentDisp4 = QLabel(parent=window)
contentDisp4.setWordWrap(True)
contentDisp4.move(780,480)
contentDisp4.setFixedWidth(400)
contentDisp4.setText(display4)
contentDisp4.setStyleSheet("border: 2px solid black;")
contentDisp4.setFont(QFont('Arial', 20))


display5 = ""
contentDisp5 = QLabel(parent=window)
contentDisp5.setWordWrap(True)
contentDisp5.move(780,640)
contentDisp5.setFixedWidth(400)
contentDisp5.setText(display5)
contentDisp5.setStyleSheet("border: 2px solid black;")
contentDisp5.setFont(QFont('Arial', 20))


#creates a grid to put goodies on
imageGrid = QGridLayout()
imageGrid.addWidget(logoLabel,1,1)



#adds a text box (QLabel(HTML text, parent) as a child to the window
#basically everything we do should have the window as a parent
pageTitle = QLabel('<h1>Bad Yelp Screen 1</h1>', parent=window)
#you can move any window or widget with .move(coords)
pageTitle.move(20, 10)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXECUTION STUFF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

window.show()

#runs the main loop for the app
sys.exit(app.exec_())
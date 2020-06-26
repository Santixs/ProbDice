import random
import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QSlider
from matplotlib import pyplot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import PercentFormatter

import interactFiles
from scrollLabel import ScrollLabel


class Ui_MainWindow(object):
    history = []
    minValue = 0
    maxValue = 10

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 670)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 40, 800, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.times = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.times.setObjectName("times")
        self.gridLayout.addWidget(self.times, 3, 1, 1, 1)
        self.times.setText("1")
        self.onlyInt = QIntValidator()
        self.onlyInt.setBottom(1)
        self.times.setValidator((self.onlyInt))

        self.sp = QSlider(Qt.Horizontal)
        self.sp.setMinimum(1)
        self.sp.setMaximum(50)
        self.sp.setValue(1)
        self.gridLayout.addWidget(self.sp, 4, 0, 2, 2)
        self.sp.valueChanged.connect(self.sliderD)

        self.sliderLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sliderLabel.setFont(font)
        self.sliderLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sliderLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.sliderLabel.setObjectName("sliderLabel")
        self.gridLayout.addWidget(self.sliderLabel, 4, 0, 1, 1)
        self.sliderLabel.setText("Number of dice thrown at once: 1")

        self.numFaces = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.numFaces.setObjectName("numFaces")
        self.gridLayout.addWidget(self.numFaces, 3, 0, 1, 1)
        self.numFaces.setText("6")
        self.numFaces.setValidator((self.onlyInt))

        self.generateButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(self.generate)
        self.gridLayout.addWidget(self.generateButton, 0, 0, 1, 1)

        self.loadFileButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loadFileButton.setObjectName("loadFileButton")
        self.loadFileButton.clicked.connect(self.load)
        self.loadFileButton.setText("Load file")
        self.gridLayout.addWidget(self.loadFileButton, 13, 1, 1, 1)

        self.saveFileButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveFileButton.setObjectName("saveFileButton")
        self.saveFileButton.clicked.connect(self.save)
        self.saveFileButton.setText("Save data")
        self.gridLayout.addWidget(self.saveFileButton, 13, 0, 1, 1)

        self.showHistoryButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.showHistoryButton.setObjectName("showHistoryButton")
        self.showHistoryButton.clicked.connect(self.showHistory)
        self.gridLayout.addWidget(self.showHistoryButton, 7, 0, 1, 0)

        self.numFacesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.numFacesLabel.setFont(font)
        self.numFacesLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.numFacesLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.numFacesLabel.setObjectName("numFacesLabel")
        self.gridLayout.addWidget(self.numFacesLabel, 2, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.clearButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 0, 1, 1, 1)
        self.clearButton.clicked.connect(self.reset)

        self.timesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        self.timesLabel.setFont(font)
        self.timesLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.timesLabel.setObjectName("timesLabel")
        self.gridLayout.addWidget(self.timesLabel, 2, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)
        self.label_3.setText("Last random number:  - ")
        self.label_3.setStyleSheet("color: black;")

        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.figure = pyplot.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, MainWindow)

        self.gridLayout.addWidget(self.toolbar, 9, 0, 1, 2)
        self.gridLayout.addWidget(self.canvas, 11, 0, 2, 2)

        self.label = ScrollLabel(MainWindow)
        self.gridLayout.addWidget(self.label, 8, 0, 1, 2)

        self.showHistoryButton.setText("Show history")
        self.showHistoryButton.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ProbDice"))
        self.generateButton.setText(_translate("MainWindow", "Throw the dice"))
        self.numFacesLabel.setText(_translate("MainWindow", "Number of faces"))
        self.clearButton.setText(_translate("MainWindow", "Reset"))
        self.timesLabel.setText(_translate("MainWindow", "Times"))

    def showHistory(self):

        self.label.setText(self.history)
        self.label.show()

    def sliderD(self):
        self.sliderLabel.setText("Number of dice thrown at once: " + str(self.sp.value()))

    def generate(self):

        if not (self.times.hasAcceptableInput() and self.numFaces.hasAcceptableInput()):
            self.label_3.setText("You can only enter integers greater than 0")
            self.label_3.setStyleSheet("color: red;")
        else:

            i = 0
            j = 0
            # Since times.text() is always greater or equal than 1, num, always has a value
            while i < int(self.times.text()):
                num = 0
                while j < self.sp.value():
                    num += random.randint(1, int(self.numFaces.text()))
                    j = j + 1
                self.history.append(num)
                j = 0
                i = i + 1

            self.label_3.setStyleSheet("color: black;")
            self.label_3.setText("Last random number:  " + str(num))
            self.plot()

            if len(self.history) < 100000:
                self.showHistory()
            else:
                self.label.setTextW(
                    "For large data sets it may take some time to generate the history, (the histogram is always updated)")
                self.label.show()
                self.showHistoryButton.show()

    def reset(self):
        self.label_3.setStyleSheet("color: black;")
        self.history.clear()
        self.label_3.setText("Last random number:  - ")
        self.figure.clear()
        self.canvas.draw()
        self.label.clear()
        self.showHistoryButton.hide()

    def plot(self):
        self.figure.clear()
        self.figure.add_subplot()
        pyplot.hist(self.history, bins=np.arange(1, int(self.numFaces.text()) * self.sp.value() + 2) - 0.5, ec="w",
                    weights=np.ones(len(self.history)) / len(self.history))
        pyplot.gca().yaxis.set_major_formatter(PercentFormatter(1))
        self.canvas.draw()

    def load(self):
        try:
            self.history = interactFiles.load(self.history)
            self.showHistoryButton.show()
            self.plot()
        except:
            self.label_3.setText("The file selected has not the proper format or data")
            self.label_3.setStyleSheet("color: red;")
            self.label.setTextW(
                "In the file there can only be numbers, they can be placed with a space between them (1 2 3), with commas (1,2,3) or (1, 2, 3) or place a number per line")
            self.label.show()

    def save(self):
        try:
            interactFiles.save(self.history)
            self.label_3.setText("The file has been saved correctly")
            self.label_3.setStyleSheet("color: black;")
        except:
            self.label_3.setText("The file has not been saved correctly")
            self.label_3.setStyleSheet("color: red;")


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

"""
ABAPi
View (GUI) Module
Version 1.0
Targets python 3.2, Qt 4.8, and PySide
Originally wirtten by: Justin Gordon and Tyler Ramasco
--------------------------------------------------------------------
This file is part of ABAPi.

ABAPi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ABAPi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

from PySide import QtCore, QtGui
import sys


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("ABAPi")
        # File required: logo.png
        self.setWindowIcon(QtGui.QIcon("icons/logo.png"))
        self.showMaximized()
        # We can also show fullscreen with self.showFullscreen()

    # Initiates the top frame and content area
    def initUi(self):
        self.topTitle = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(22)
        self.topTitle.setFont(font)

        # Initiating layouts
        self.verticalLayout = QtGui.QVBoxLayout()
        horizontalLayout = QtGui.QHBoxLayout()
        self.stackedForLayout = QtGui.QStackedWidget()
        topFrame = QtGui.QFrame()
        self.stackedForBack = QtGui.QStackedWidget()
        # self.stackedForBack.setMaximumHeight(50)
        self.backButton = QtGui.QPushButton("Back")
        self.stackedForBack.addWidget(QtGui.QFrame())
        self.stackedForBack.addWidget(self.backButton)

        # Adding widgets
        self.verticalLayout.addWidget(topFrame)
        self.verticalLayout.addWidget(self.stackedForLayout)
        horizontalLayout.addWidget(self.stackedForBack)
        horizontalLayout.addWidget(self.topTitle)
        horizontalLayout.addStretch()

        # Configuring layout
        topFrame.setMaximumHeight(50)
        self.backButton.setMaximumWidth(100)

        # Setting layouts
        topFrame.setLayout(horizontalLayout)
        self.setLayout(self.verticalLayout)

       # Adding all GUIs
        self.splashId = self.addLayout(self.initSplash())
        self.practiceId = self.addLayout(self.initPractice())
        self.examId = self.addLayout(self.initExam())
        self.passwordId = self.addLayout(self.initPassword())
        self.rightId = self.addLayout(self.initRight())
        self.wrongId = self.addLayout(self.initWrong())


    # Adds the given layout to the stack of layouts for the content area
    # Returns ID of the layout in the stack just added
    def addLayout(self, layout):
        # One does not simply just add layouts to QStackedWidgets
        contentFrame = QtGui.QFrame()
        contentFrame.setLayout(layout)
        id = self.stackedForLayout.addWidget(contentFrame)
        self.stackedForLayout.setCurrentWidget(contentFrame)
        return id

    # Sets the title in the top frame to given text
    def setTitle(self, title):
        self.topTitle.setText(title)

    def setBackButton(self, button):
        self.stackedForBack.addWidget(button)
        self.stackedForBack.setCurrentWidget(button)


    def hideBackButton(self):
        self.stackedForBack.setCurrentIndex(0)

    def showBackButton(self):
        self.stackedForBack.setCurrentIndex(1)

    # Function that draws the landing screen/splash screen
    def initSplash(self):
        print("Drawing splash screen...")

        self.hideBackButton()
        gridLayout = QtGui.QGridLayout()

        # Setting up widgets (lables, buttons,...)
        font = QtGui.QFont()
        font.setPointSize(96)
        self.setTitle("Hello, ")
        self.splashPracticeButton = QtGui.QPushButton("Practice")
        self.splashPracticeButton.setFont(font)
        self.splashExamButton = QtGui.QPushButton("Exam")
        font.setPointSize(48)
        self.splashExamButton.setFont(font)

        # Adding widgets to layout
        gridLayout.addWidget(self.splashPracticeButton, 0, 0, 5, 1)
        gridLayout.addWidget(self.splashExamButton, 4, 1)

        # Configuring layout
        self.splashPracticeButton.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        gridLayout.setColumnStretch(0, 7)
        gridLayout.setColumnStretch(1, 1)
        gridLayout.setRowStretch(1, 2)

        # Connecting buttons to methods
        # Controller now connects buttons

        return gridLayout

    def drawSplash(self, name):
        self.setTitle("Hello, " + name)
        self.stackedForLayout.setCurrentIndex(self.splashId)
        self.hideBackButton()

    def initPractice(self):
        print("Drawing practice screen...")

        # Setting up widgets (lables, buttons,...)
        # self.setTitle("Practice")
        font = QtGui.QFont()
        font.setPointSize(96)
        self.practiceWordButton = QtGui.QPushButton()
        self.practiceWordButton.setFont(font)
        equalsLabel = QtGui.QLabel("=")
        equalsLabel.setFont(font)
        self.practicePictureButton = QtGui.QPushButton()
        self.practicePictureButton.setIconSize(QtCore.QSize(300, 300))

        # Initiating layout
        horizontalLayout = QtGui.QHBoxLayout()

        # Adding widgets to layout
        horizontalLayout.addWidget(self.practiceWordButton)
        horizontalLayout.addWidget(equalsLabel)
        horizontalLayout.addWidget(self.practicePictureButton)

        # Configuring layout
        equalsLabel.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        equalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showBackButton()

        return horizontalLayout

    def drawPractice(self, word, pictureFile):
        self.setTitle("Practice")
        self.practiceWordButton.setText(word)
        self.practicePictureButton.setIcon(QtGui.QIcon(pictureFile))

        self.stackedForLayout.setCurrentIndex(self.practiceId)
        self.hideBackButton()

    def initExam(self):
        print("Drawing exam screen...")

        # Setting up widgets (lables, buttons,...)
        self.setTitle("Exam")
        font = QtGui.QFont()
        font.setPointSize(96)
        self.examWordButton = QtGui.QPushButton()
        equalsLabel = QtGui.QLabel("=")
        equalsLabel.setFont(font)
        self.examWordButton.setFont(font)

        self.examAnswerButton1 = QtGui.QPushButton()
        self.examAnswerButton1.setIconSize(QtCore.QSize(300, 300))
        self.examAnswerButton1.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)

        self.examAnswerButton2 = QtGui.QPushButton()
        self.examAnswerButton2.setIconSize(QtCore.QSize(300, 300))
        self.examAnswerButton2.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)

        self.examAnswerButton3 = QtGui.QPushButton()
        self.examAnswerButton3.setIconSize(QtCore.QSize(300, 300))
        self.examAnswerButton3.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)

        self.examAnswerButton4 = QtGui.QPushButton()
        self.examAnswerButton4.setIconSize(QtCore.QSize(300, 300))
        self.examAnswerButton4.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)

        # Initiating layout
        horizontalLayout = QtGui.QHBoxLayout()
        gridLayout = QtGui.QGridLayout()

        # Adding widgets to layout
        horizontalLayout.addWidget(self.examWordButton)
        horizontalLayout.addWidget(equalsLabel, 0, QtCore.Qt.AlignCenter)
        gridLayout.addWidget(self.examAnswerButton1, 0, 0)
        gridLayout.addWidget(self.examAnswerButton2, 0, 1)
        gridLayout.addWidget(self.examAnswerButton3, 1, 0)
        gridLayout.addWidget(self.examAnswerButton4, 1, 1)
        horizontalLayout.addLayout(gridLayout)

        # Configuring layout
        self.showBackButton()
        equalsLabel.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        equalsLabel.setAlignment(QtCore.Qt.AlignCenter)

        return horizontalLayout

    def drawExam(self, word, button1PictureFile, button2PictureFile, button3PictureFile, button4PictureFile):
        self.setTitle("Exam")
        self.examWordButton.setText(word)

        self.examAnswerButton1.setIcon(QtGui.QIcon(button1PictureFile))
        self.examAnswerButton2.setIcon(QtGui.QIcon(button2PictureFile))
        self.examAnswerButton3.setIcon(QtGui.QIcon(button3PictureFile))
        self.examAnswerButton4.setIcon(QtGui.QIcon(button4PictureFile))

        self.stackedForLayout.setCurrentIndex(self.examId)
        self.hideBackButton()

    # Does not make any changes to the exam screen, assumes that drawExam() was called before
    def showExam(self):
        self.stackedForLayout.setCurrentIndex(self.examId)

    def initPassword(self):
        print("Drawing password screen...")

        # Setting up labels, text boxes, etc.
        label = QtGui.QLabel("Password:")
        self.passwordBox = QtGui.QLineEdit()
        self.passwordBox.setText("Enter password here")
        self.passwordOkayButton = QtGui.QPushButton("Okay")

        # Adding widgets to layout
        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(label)
        horizontalLayout.addWidget(self.passwordBox)
        horizontalLayout.addWidget(self.passwordOkayButton)

        return horizontalLayout

    def drawPassword(self):
        self.stackedForLayout.setCurrentIndex(self.passwordId)
        self.showBackButton()

    def initRight(self):
        print("Drawing right screen...")

        # Setting up labels, text boxes, etc.
        icon = QtGui.QIcon("icons/right.png")
        self.rightPictureButton = QtGui.QPushButton()
        self.rightPictureButton.setIcon(icon)
        self.rightPictureButton.setIconSize(QtCore.QSize(1014, 610))

        # Adding widgets to layout
        verticleLayout = QtGui.QVBoxLayout()
        verticleLayout.addWidget(self.rightPictureButton)

        return verticleLayout

    def drawRight(self):
        self.stackedForLayout.setCurrentIndex(self.rightId)

    def initWrong(self):
        print("Drawing wrong screen...")

        # Setting up labels, text boxes, etc.
        icon = QtGui.QIcon("icons/wrong.png")
        self.wrongPictureButton = QtGui.QPushButton()
        self.wrongPictureButton.setIcon(icon)
        self.wrongPictureButton.setIconSize(QtCore.QSize(1014, 610))

        # Adding widgets to layout
        verticalLayout = QtGui.QVBoxLayout()
        verticalLayout.addWidget(self.wrongPictureButton)

        return verticalLayout

    def drawWrong(self):
        self.stackedForLayout.setCurrentIndex(self.wrongId)

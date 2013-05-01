#bn: ABAPi
# Controller Module
# Version 0.1 ALPHA
# Targets Python 3.3
# Justin Gordon and Tyler Romasco

from PySide import QtGui, QtCore
import random
import sys
import ui_qt as View
import models as Model


class Controller(QtCore.QObject):

    def __init__(self):
        super(Controller, self).__init__()

        # Initializing GUI
        self.mainWindow = View.MainWindow()
        self.mainWindow.initUi()
        self.mainWindow.backButton.clicked.connect(self.pressedBack)

        # Connecting buttons
        self.mainWindow.splashPracticeButton.clicked.connect(self.startPractice)
        self.mainWindow.splashExamButton.clicked.connect(self.toPassword)
        self.mainWindow.passwordOkayButton.clicked.connect(self.checkPassword)
        self.mainWindow.passwordBox.returnPressed.connect(self.checkPassword)

        # Make a global exam that can be access from everywhere
        self.config = Model.Configuration()
        self.wordSet = Model.WordSet()

        self.goToSplash()


    def startExam(self):
        self.exam = Model.Exam()
        self.words = self.wordSet.getWords()
        self.pictures = self.wordSet.getPictures()
        self.attemptsAllowed = self.config.getNumTriesAllowed()
        self.attempts = 0

        self.numberQuestions = len(self.words)

        # Keeps track of the current question number
        self.currentWordIndex = 0
        # Keep track if the last question was correct or not
        self.lastAnswerCorrect = True

        self.mainWindow.examAnswerButton1.clicked.connect(self.examButton1)
        self.mainWindow.examAnswerButton2.clicked.connect(self.examButton2)
        self.mainWindow.examAnswerButton3.clicked.connect(self.examButton3)
        self.mainWindow.examAnswerButton4.clicked.connect(self.examButton4)
        self.mainWindow.rightPictureButton.clicked.connect(self.nextQuestionInExam)
        self.mainWindow.wrongPictureButton.clicked.connect(self.nextQuestionInExam)

        self.nextQuestionInExam()


    def nextQuestionInExam(self):
        if self.currentWordIndex < self.numberQuestions:
            # Checks if the last button click was correct or not.
            # If the last click was correct, then set up the next word and answers
            if self.lastAnswerCorrect is True:
                self.attempts = 0
                # Re-enables all of the buttons
                self.mainWindow.examAnswerButton1.setEnabled(True)
                self.mainWindow.examAnswerButton2.setEnabled(True)
                self.mainWindow.examAnswerButton3.setEnabled(True)
                self.mainWindow.examAnswerButton4.setEnabled(True)
                # Holds the picture file names the buttons should display
                buttonPictures = []
                # Make a set of words so we can use this to make a relatively random arrangement of pictures
                pictureList = list(self.pictures)
                # This randomly determines which button should be the correct one
                self.correctButtonIndex = random.randint(0,3)

                # Get the current word to ask
                word = self.words[self.currentWordIndex]
                # Set the button pictures
                pictureList.pop(self.currentWordIndex)
                for i in range(0, 4):
                    if i is self.correctButtonIndex:
                        # Puts the correct word into this button
                        buttonPictures.insert(i, self.pictures[self.currentWordIndex])
                    else:
                        # Picks a random word to put into this button
                        randomWordIndex = random.randint(0, len(pictureList)-1)
                        buttonPictures.insert(i, pictureList.pop(randomWordIndex))

                self.mainWindow.drawExam(word, buttonPictures[0], buttonPictures[1], buttonPictures[2], buttonPictures[3])
            else:
                # This is run if the last answer clicked was wrong
                # This checks if the student has exceeded allowed attempts,
                # and disables all wrong buttons when that is the case
                if self.attempts >= self.attemptsAllowed:
                    if self.correctButtonIndex is not 0:
                        self.mainWindow.examAnswerButton1.setDisabled(True)
                    if self.correctButtonIndex is not 1:
                        self.mainWindow.examAnswerButton2.setDisabled(True)
                    if self.correctButtonIndex is not 2:
                        self.mainWindow.examAnswerButton3.setDisabled(True)
                    if self.correctButtonIndex is not 3:
                        self.mainWindow.examAnswerButton4.setDisabled(True)
                # No changes are made to the exam screen, so the methods calls the screen back to the foreground
                self.mainWindow.showExam()
        else:
            # This will be run when all of the words have been tested
            # Disconnect all of the buttons to prevent multiple-event-connection problems
            self.mainWindow.examAnswerButton1.clicked.disconnect(self.examButton1)
            self.mainWindow.examAnswerButton2.clicked.disconnect(self.examButton2)
            self.mainWindow.examAnswerButton3.clicked.disconnect(self.examButton3)
            self.mainWindow.examAnswerButton4.clicked.disconnect(self.examButton4)
            self.mainWindow.rightPictureButton.clicked.disconnect(self.nextQuestionInExam)
            self.mainWindow.wrongPictureButton.clicked.disconnect(self.nextQuestionInExam)
            # Save results of the exam
            self.exam.save()
            self.goToSplash()

    def examButton1(self):
        print("Exam: Button 1 pressed")
        if self.correctButtonIndex is 0:
            self.currentWordIndex += 1
            self.lastAnswerCorrect = True
            self.showRight()
        else:
            self.mainWindow.examAnswerButton1.setDisabled(True)
            self.lastAnswerCorrect = False
            self.attempts += 1
            self.showWrong()

    def examButton2(self):
        print("Exam: Button 2 pressed")
        if self.correctButtonIndex is 1:
            self.currentWordIndex += 1
            self.lastAnswerCorrect = True
            self.showRight()
        else:
            self.mainWindow.examAnswerButton2.setDisabled(True)
            self.lastAnswerCorrect = False
            self.attempts += 1
            self.showWrong()

    def examButton3(self):
        print("Exam: Button 3 pressed")
        if self.correctButtonIndex is 2:
            self.currentWordIndex += 1
            self.lastAnswerCorrect = True
            self.showRight()
        else:
            self.mainWindow.examAnswerButton3.setDisabled(True)
            self.lastAnswerCorrect = False
            self.attempts += 1
            self.showWrong()

    def examButton4(self):
        print("Exam: Button 4 pressed")
        if self.correctButtonIndex is 3:
            self.currentWordIndex += 1
            self.lastAnswerCorrect = True
            self.showRight()
        else:
            self.mainWindow.examAnswerButton4.setDisabled(True)
            self.lastAnswerCorrect = False
            self.attempts += 1
            self.showWrong()

    def startPractice(self):
        self.words = self.wordSet.getWords()
        self.pictures = self.wordSet.getPictures()
        self.numberQuestions = len(self.words)

        # Keeps track of the current question number
        self.currentWordIndex = -1

        self.mainWindow.practicePictureButton.clicked.connect(self.nextQuestionInPractice)

        self.nextQuestionInPractice()

    def nextQuestionInPractice(self):
        self.currentWordIndex += 1
        if self.currentWordIndex < self.numberQuestions:
            self.mainWindow.drawPractice(self.words[self.currentWordIndex], self.pictures[self.currentWordIndex])
        else:
            # Disconnect the button to prevent multiple-connection problems
            self.mainWindow.practicePictureButton.clicked.disconnect(self.nextQuestionInPractice)
            self.goToSplash()

    def goToSplash(self):
        studentName = self.config.getName()
        self.mainWindow.drawSplash(studentName)

    def pressedBack(self):
        # We can save the state of the application here if we'd like
        self.goToSplash()

    def toPassword(self):
        self.mainWindow.drawPassword()

    def checkPassword(self):
        passwordActual = self.config.getPassword()
        passwordEntered = self.mainWindow.passwordBox.text()
        if passwordEntered == passwordActual:
            self.startExam()
        else:
            self.mainWindow.passwordBox.setText("Incorrect password, try again.")
            self.toPassword()

    def showRight(self):
        self.exam.correct(self.words[self.currentWordIndex-1])
        self.mainWindow.drawRight()

    def showWrong(self):
        self.exam.incorrect(self.words[self.currentWordIndex-1])
        self.mainWindow.drawWrong()


def main():
    # Initializing application
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("ABAPi")
    controller = Controller()

    # Application finished, exit
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

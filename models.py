"""
ABAPi
Model Module
Version 1.0
Targets python 3.2
Originally written by: Justin Gordon and Tyler Ramasco
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

import json
import datetime
import os
from collections import defaultdict

class Configuration:
    def __init__(self):
        # This is EXTREMELY hackish
        directory = os.path.abspath(__file__)
        directory, fd = os.path.split(directory)
        name = "config.json"
        path = os.path.join(directory, 'data', name)
        self.load(path)

    def load(self, path):
        if os.path.exists(path):
            fd = open(path)
            self.data = json.load(fd)
        else:
            print("Error: Configuration file not found")
            print("Creating blank file. Please edit it after closing the application.")
            fd = open(path, 'a+')
            self.data= defaultdict()
            self.data['name'] = "Unknown"
            self.data['attemptsAllowed'] = 1
            self.data['password'] = "password"
        fd.close()

    def getName(self):
        return self.data['name']

    def getNumTriesAllowed(self):
        return self.data['attemptsAllowed']

    def getPassword(self):
        return self.data['password']

class WordSet:
    def __init__(self, name="current"):
        directory = os.path.abspath(__file__)
        directory, fd = os.path.split(directory)
        name = "wordset_" + name + '.json'
        path = os.path.join(directory, 'data', name)
        self.load(path)

    def load(self, path):
        if os.path.exists(path):
            fd = open(path)
            self.data = json.load(fd)
        else:
            fd = open(path, 'a+')
            print("Error: Wordset file not found")
            print("No exam will be run")
            self.data = defaultdict()

        fd.close()

    def getData(self):
        return self.data

    def getWords(self):
        words = []
        for e in self.data:
            words.append(e['word'])

        return words

    def getPictures(self):
        pictures = []
        for e in self.data:
            pictures.append("pictures/" + e['picture'])

        return pictures


class Exam:
    def __init__(self, name=None):
        directory = os.path.abspath(__file__)
        directory, fd = os.path.split(directory)
        if name is None:
            name = str(datetime.datetime.now().date()) + '.json'
            # self.createNewData()
        else:
            # self.load()
            pass
        self.path = os.path.join(directory, 'data', name)
        self.load()
        #print(directory)

    def createNewData(self):
        self.data = defaultdict()
        self.data['date'] = str(datetime.datetime.today())
        self.data['words'] = defaultdict(None)

    def load(self):
        if os.path.exists(self.path):
            fd = open(self.path)
            self.data = json.load(fd)
        else:
            # May not ever be used
            fd = open(self.path, 'a+')
            self.data = defaultdict()
            self.data['date'] = str(datetime.datetime.today())
            self.data['words'] = defaultdict(None)
        fd.close()

    def save(self):
        fd = open(self.path, 'w')
        json.dump(self.data, fd)
        fd.close()

    def correct(self, word):
        word = str(word)
        if self.data['words'].get(word, None) == None:
            self.data['words'][word] = {'correct': 0, 'incorrect': 0}
        self.data['words'][word]['correct'] += 1

    def incorrect(self, word):
        word = str(word)
        if self.data['words'].get(word, None) == None:
            self.data['words'][word] = {'correct': 0, 'incorrect': 0}
        self.data['words'][word]['incorrect'] += 1


##def main():
##	exam1 = Exam('2013-03-07.json')
##	exam1.load()
##	words = ['chair', 'door', 'table', 'candle', 'floor']
##	for word in words:
##		exam1.correct(word)
##		exam1.incorrect(word)
##	print(exam1.data)
##	exam1.save()
##
##main()

ABAPi
=================
Last revised May 3, 2013

Repository for code and documentation for Justin Gordon's and Tyler Romasco's senior project at Widener University, known as ABAPi.

ABAPi strives to provide a learning and testing application for a subset of children with Autism. The application will assist in the learning of sight words. There are 2 modes: practice and exam. The practice mode is errorless (user cannot get the question wrong). The exam mode keeps track of which words were answered correctly and incorrectly.

This is a python program consisting of several Python files. ABAPi is developed with the MVC (model, view, controller) paradigm. It was targeted for the Raspberry Pi hardware (www.raspberrypi.org), but should work on other platforms (Windows, Mac, Linux) as well.

Dependencies:
 - Python 3.2
 - Qt 4.2
 - PySide


These packages are available for the Raspbian by searching for them with apt-get.
Once you have the dependencies installed, you can run the program by entering into the desktop with the "startx" command, open the terminal, navigate to this directory, and run the program with the command "python3 controller.py".

For more info, contact the creators:
Justin Gordon, jmgordon at mail dot widener dot edu
George Romasco, gtromasco at mail dot widener dot edu
"""
A minimal app to understand what you must have to have a pyqt app.
"""
# pylint: disable=c-extension-no-member

import sys

import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication(sys.argv)
button = PyQt5.QtWidgets.QPushButton("Button")
button.show()
sys.exit(app.exec())

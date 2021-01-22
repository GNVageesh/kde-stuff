import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QWidget, QWidgetAction

app = QApplication(sys.argv)

window = QWidget()
# main window
window.setWindowTitle('PyQt5 Learning')
window.setGeometry(100, 100, 280, 280)
window.move(60, 15)
# label
hello = QLabel('<h1>Hello vageesh</h1>', parent=window)
hello.move(60, 15)
btn = QPushButton(text='Python3', parent=window)
btn.move(60, 15)
# combo box
combo = QComboBox(parent=window)
# method 1: addItem
combo.addItem('vageesh')
combo.addItem('vageesh')
combo.addItem('vageesh')
# method 2: addItems
combo.addItems(['vageesh', 'is', 'coding here'])
# method 3: using for-loop
for x in range(10):
    combo.addItem('i am coding')

window.show()
sys.exit(app.exec_())

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QLabel


# class for scrollable label
class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)
        self.setMaximumHeight(70)

        # making qwidget object
        content = QWidget()
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)
        # the setText method

    def setText(self, textN):
        # setting text to the label
        self.auxText = " "
        for x in textN:
            self.auxText = self.auxText + str(x) + ", "

        self.label.setText(self.auxText)

    def setTextW(self, textN):
        # setting text to the label
        self.label.setText(textN)

    def append(self, textN):
        self.label.setText(self.text() + ", " + textN)

    def clear(self):
        self.label.clear()

    def text(self):
        # getting text of the label
        get_text = self.label.text()

        # return the text
        return get_text

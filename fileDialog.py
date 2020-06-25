from PyQt5.QtWidgets import QWidget, QFileDialog


class Aapp(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Select the txt file'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        pass

    # It is for opening 1 file
    def openFileNameDialog(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select the file", "",
                                                  "All Files (*);;txt Files (*.txt)", options=options)
        if fileName:
            return fileName

    # It is for opening 1 or more files at once
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;txt Files (*.txt)", options=options)
        if files:
            return files

    # It is for save a file
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save the data", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            return (fileName)

import sys
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class FriendsList(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'FriendsList'
        self.mywidgets = [[]]
        self.friendsListWidgets = [[]]
        self.y = 0
        self.friends_counter = 0
        self.left = 100
        self.top = 100
        self.width = 700
        self.height = 500
        self.pics = []
        self.picON = False
        self.path = "friends/"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: yellow")

        # Create buttons
        self.show_button = QPushButton('Show Friends', self)
        self.clear_button = QPushButton('Clear All', self)
        self.delete_button = QPushButton('Delete a Friend', self)
        self.add_button = QPushButton('Add New Friend', self)
        self.quit_button = QPushButton('Quit', self)

        # Set button styles
        self.show_button.setStyleSheet("background-color: lightblue; color: black; border-width: 4px; border-style: solid; border-color: white; width: 15px; padding: 5px;")
        self.clear_button.setStyleSheet("background-color: lightblue; color: black; border-width: 4px; border-style: solid; border-color: white; width: 15px; padding: 5px;")
        self.delete_button.setStyleSheet("background-color: lightblue; color: black; border-width: 4px; border-style: solid; border-color: white; width: 15px; padding: 5px;")
        self.add_button.setStyleSheet("background-color: lightblue; color: black; border-width: 4px; border-style: solid; border-color: white; width: 15px; padding: 5px;")
        self.quit_button.setStyleSheet("background-color: lightblue; color: black; border-width: 4px; border-style: solid; border-color: white; width: 15px; padding: 5px;")

        self.show_button.setFixedHeight(52)
        self.clear_button.setFixedHeight(52)
        self.delete_button.setFixedHeight(52)
        self.add_button.setFixedHeight(52)
        self.quit_button.setFixedHeight(52)

        self.clear_button.setDisabled(True)
        self.clear_button.setStyleSheet("background-color: white; color: black; border-width: 4px; border-style: solid; border-color: lightyellow; width: 15px; padding: 5px;")

        # Create grid layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.show_button, 0, 0)
        self.layout.addWidget(self.clear_button, 0, 1)
        self.layout.addWidget(self.delete_button, 0, 2)
        self.layout.addWidget(self.add_button, 0, 3)
        self.layout.addWidget(self.quit_button, 0, 4)

        # Connect buttons to their respective functions
        self.show_button.clicked.connect(self.show_friends)
        self.clear_button.clicked.connect(self.clear_all)
        self.delete_button.clicked.connect(self.delete_friend)
        self.add_button.clicked.connect(self.add_friend)
        self.quit_button.clicked.connect(self.quit)

        self.setLayout(self.layout)

    def quit(self):
        answer = QMessageBox.question(self, "Confirm", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.close()
        else:
            QMessageBox.information(self, "Information", "Keep Going!")

    def show_friends(self):
        self.clear_button.setEnabled(True)
        self.clear_button.setStyleSheet("background-color: lightblue; color: black; border-width: 4px; border-style: solid; border-color: white; width: 15px; padding: 5px;")
        i = 0

        file_types = ['jpg', 'png', 'gif', 'ico', 'bmp', 'svg', 'tif', 'tga', 'wbmp']
        self.done = []
        self.btns = []
        for file in os.listdir(self.path):
            self.pics.append(file)
            if file.split('.')[-1] in file_types:
                file = os.path.join(self.path, file)
                image = QPixmap(file)
                resizedImage = image.scaled(105, 90)
                photo = QLabel(self)
                photo.setPixmap(resizedImage)
                photo.setFixedHeight(90)
                btn = QPushButton(self)
                btn.setObjectName(file)
                btn.setFixedHeight(32)
                btn.clicked.connect(self.list_friend)
                btn.setText(file.split('/')[-1].split('.')[0])
                btn.setStyleSheet(
            "text-shadow: 1px 2px 2px #1C6EA4;background-color:white; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

                self.btns.append(btn)
                self.layout2 = QGridLayout()
                self.layout2.addWidget(photo, 1 + i, 1 + i)
                self.friendsListWidgets[self.friends_counter].append(photo)
                self.layout2.addWidget(btn, 2 + i, 1 + i)
                self.friendsListWidgets[self.friends_counter].append(btn)

                self.layout2.setAlignment(Qt.AlignTop)
                self.layout.setAlignment(Qt.AlignTop)
                self.layout.addLayout(self.layout2, 1, 0 + i)
                self.done.append(file)
                i += 1
                self.friendsListWidgets.append([])
                self.friends_counter += 1
        self.y = self.y + 1
        self.mywidgets.append([])

    def clear_all(self):
        for rows in self.mywidgets:
            for item in rows:
                item.hide()

        for rows in self.friendsListWidgets:
            for item in rows:
                item.hide()

        self.mywidgets = [[]]
        self.friendsListWidgets = [[]]
        self.y = 0
        self.friends_counter = 0

        self.clear_button.setDisabled(True)
        self.clear_button.setStyleSheet(
            "background-color: white; color: black; border-width: 4px; border-style: solid; border-color: lightyellow; width: 15px; padding: 5px;")
        self.layout.setAlignment(Qt.AlignVCenter)

    def delete_friend(self):
        path = None
        message = 'Are you sure you want to Delete the Image'
        path = QFileDialog.getOpenFileName(self, '\t\tDelete a Friend !', '',
                                           'All Files (*.*)')
        if path != ('', '') and path != None:
            image_path = path[0]
            choice = self.multi_choice_msgBox(image_path, message)
            if choice:
                image_path = image_path.split('/')

                image_path = '\\'.join(image_path)
                os.system(f'del "{image_path}"')
                self.clear_all()
                self.show_friends()

        else:
            print("Some Error while handling image files")

    def multi_choice_msgBox(self, link, message):
        message = QMessageBox.question(self, "Confirmation Message !", f"{message} ?\n   {link}", QMessageBox.Yes |QMessageBox.No)

        if message == QMessageBox.Yes:
            return True
        elif message == QMessageBox.No:
            return False

    def add_friend(self):
        path = None
        message = 'Are you sure you want to Add New Friend'
        path = QFileDialog.getOpenFileName(self, '\t\tDelete a Friend !', '',
                                           'All Files (*.*)')
        if path != ('', '') and path != None:
            image_path = path[0]
            message = message + f'   {image_path.split(".")[0].split("/")[-1]} '
            choice = self.multi_choice_msgBox(image_path, message)
            if choice:
                image_path = image_path.split('/')

                image_path = '\\'.join(image_path)
                os.system(f'copy "{image_path}" "{os.getcwd()}\\friends"')
                self.clear_all()
                self.show_friends()

        else:
            print("Some Error while handling image files")

    def delete_canvas(self):
        text = self.sender().objectName()
        # print(text)
        coordinates = text.split(':')[1].strip().split(',')
        y = int(coordinates[1])
        for x in range(int(coordinates[0]) + 2):
            self.mywidgets[y][x].hide()

    def list_friend(self):
        path = ' NONE '
        layout2 = QGridLayout()
        try:
            text = self.sender().objectName()
            path = text.split('.')
            dump = path.pop()
            path = ''.join(path)


            i = 0
            file_types = ['jpg', 'png', 'gif', 'ico', 'bmp', 'svg', 'tif', 'tga', 'wbmp']

            for count, file in enumerate(os.listdir(path)):
                self.pics.append(file)
                if file.split('.')[-1] in file_types:
                    file = os.path.join(path, file)
                    image = QPixmap(file)
                    resizedImage = image.scaled(105, 90)
                    photo = QLabel(self)
                    photo.setPixmap(resizedImage)
                    photo.setFixedHeight(90)

                    self.layout.addWidget(photo, self.y + 1,  i)
                    self.mywidgets[self.y].append(photo)

                    if count == len(os.listdir(path)) - 1:
                        btn = QPushButton(self)
                        btn.setObjectName(f"x,y   :   {i},{self.y}")
                        btn.setFixedHeight(34)
                        btn.setFixedWidth(34)
                        btn.clicked.connect(self.delete_canvas)
                        btn.setText('X')
                        btn.setStyleSheet(
                            "text-shadow: 1px 2px 2px #1C6EA4;background-color:white; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")

                        self.layout.addWidget(btn, 1 + self.y, 1 + i)
                        self.mywidgets[self.y].append(btn)

                    self.done.append(file)
                    i += 1


            self.y = self.y + 1
            self.mywidgets.append([])
        except:
            print(f"The folder with path   '{path}'   doesnot exist ")


App = QApplication([])
Window = FriendsList()
Window.show()

sys.exit(App.exec())

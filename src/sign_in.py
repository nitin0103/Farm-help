import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QPoint
import json
from firebase_admin import firestore
from home import Home_Page

credentials_path ='N:/Project/farm-help/assets/setup/userform-1420c-firebase-adminsdk-0lqqo-812dcde81b.json'
with open(credentials_path)as json_file:
    credentials_info = json.load(json_file)
db=firestore.Client.from_service_account_info(credentials_info)

class SigninPage(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Farm-Help")
        self.setWindowIcon(QIcon("./assets/images/logo.png"))
        self.setGeometry(250, 100, 1300, 800)
        self.setFixedSize(1300,800) #(width, height)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.sign_in_UI()
        self.user_data_dict = {}

    def sign_in_UI(self):
        
        # Background image
        self.background_image1 = QLabel(self)
        self.background_image1.setPixmap(QPixmap("./assets/images/nature_background_with_green_grass_and_blue_sky-.jpg"))
        self.background_image1.setFixedSize(1300,800)
        self.background_image1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bird_label = QLabel()
        self.bird_Movie = QMovie("assets/images/wbird.gif")
        self.bird_label.setMovie(self.bird_Movie)
        # self.bird_label.setFixedSize(125, 120)
        self.bird_Movie.start()
        # self.bird_label.move(20,0)

        self.bird_anim = QPropertyAnimation(self.bird_label, b"pos")
        self.bird_anim.setStartValue(QPoint(0, 150))
        self.bird_anim.setEndValue(QPoint(1300,0))
        self.bird_anim.setDuration(15000) # Set the duration of the bird_anim to 1 second
        self.bird_anim.start()
        
        # Text label
        self.welcome_label = QLabel("WELCOME TO FARM-HELP!!!") 
        self.welcome_label.setStyleSheet("background-color: transparent; color: GREEN; font-family: kristen itc; font-size: 50px; font-weight: bold;")  
        self.welcome_label.setFixedSize(880, 100) 
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        # self.welcome_label.move(0,0)
        self.welcome_label.setWordWrap(True)

        self.words = self.welcome_label.text().split()
        self.current_word = 0
        self.animation = QPropertyAnimation(self.welcome_label, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.Type.InBack)

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_word)
        self.timer.start(1000)

        # Login and register buttons
        self.login_button1 = QPushButton("🔒 Login", self)
        self.login_button1.setCursor(Qt.PointingHandCursor)
        self.login_button1.setStyleSheet("QPushButton"
                                         "{""background-color: #E8E8E8; color: black;font-family: comic sans ms; font-size: 30px; border-radius: 17px; min-width: 250px;min-height:50px;"
                                         "}"
                                         "QPushButton:hover"
                                         "{""background-color: #99ffcc; font-size: 33px; border-radius: 17px; min-width: 300px;min-height:60px;"
                                         "}"
                                         "QPushButton::pressed"
                                         "{"
                                         "background-color: #80e5ff;"
                                         "}"
                                         )
        self.login_button1.clicked.connect(self.open_login)

        self.register_button1 = QPushButton("📝 Register", self)
        self.register_button1.setCursor(Qt.PointingHandCursor)
        self.register_button1.setStyleSheet("QPushButton"
                                            "{""background-color: #E8E8E8; color: black;font-family: comic sans ms; font-size: 30px; border-radius: 17px; min-width: 250px; min-height:50px;""}"
                                            "QPushButton:hover"
                                            "{""background-color: #99ffcc;font-size: 33px; border-radius: 17px; min-width: 300px;min-height:60px;""}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color: #80e5ff;"
                                            "}"
                                            )
        self.register_button1.clicked.connect(self.open_register)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.bird_label)
        self.layout1.addWidget(self.welcome_label)
        self.layout1.addSpacing(40)
        self.layout1.addWidget(self.login_button1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout1.addSpacing(40)
        self.layout1.addWidget(self.register_button1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout1.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout1)   

    def next_word(self):
        if self.current_word >= len(self.words):
            self.timer.stop()
            return

        text = " ".join(self.words[:self.current_word + 1])
        self.welcome_label.setText(text)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        self.current_word += 1  
        
    def open_login(self):
        self.open_login_layout = QVBoxLayout()
        # Background image (login page)
        self.open_login_bg = QLabel()
        self.open_login_bg.setPixmap(QPixmap("./assets/images/bg_blur.png"))
        self.open_login_bg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.open_login_bg.setLayout(self.open_login_layout)

        # Text label
        self.user_login_label = QLabel("User Login ") 
        self.user_login_label.setStyleSheet("color: black ;font-family: comic sans ms; font-size: 40px; font-weight: bold;")  
        self.user_login_label.setAlignment(Qt.AlignmentFlag.AlignHCenter) 

        # Username and password fields
        self.username_label = QLabel("<b>Username :</b>", self)
        self.username_label.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 25px; font-weight: bold;")
        self.username = QLineEdit(self)
        self.username.setStyleSheet("color: black ;  font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.username.setFixedWidth(350) 
        initial_username_value = "Enter username" 
        self.username.setPlaceholderText(str(initial_username_value))

        self.password_label = QLabel("<b>Password :</b>", self)
        self.password_label.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 25px; font-weight: bold;")
        self.password = QLineEdit(self)
        self.password.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.password.setFixedWidth(350)
        self.password.setEchoMode(QLineEdit.Password)
        initial_password_value = "Enter Password"
        self.password.setPlaceholderText(str(initial_password_value))

        # Login button
        self.login_button = QPushButton("🔒 Login", self)
        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-family: comic sans ms; font-size: 30px; border-radius: 15px; min-width: 200px; min-height:50px;""}"
                                        "QPushButton:hover"
                                        "{""font-size: 32px; border-radius: 15px; min-width: 205px; min-height:51px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff;"
                                        "}")
        self.login_button.clicked.connect(self.login)

        self.back_button = QPushButton("🔙" ,self)
        self.back_button.setCursor(Qt.PointingHandCursor)
        self.back_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-size: 30px; border-radius: 15px; min-width: 110px; min-height:50px;""}"
                                        "QPushButton:hover"
                                         "{""font-size: 35px; border-radius: 15px; min-width: 115px;min-height:51px;""}"
                                        "QPushButton::pressed"
                                        "{""background-color: #80e5ff;""}")
        self.back_button.clicked.connect(self.go_back)
       
        self.open_login_layout.addSpacing(25)
        self.open_login_layout.addWidget(self.user_login_label)
        self.open_login_layout.addSpacing(25)
        self.open_login_layout.addWidget(self.username_label)
        self.open_login_layout.addSpacing(3)
        self.open_login_layout.addWidget(self.username)
        self.open_login_layout.addSpacing(25)
        self.open_login_layout.addWidget(self.password_label)
        self.open_login_layout.addSpacing(3)
        self.open_login_layout.addWidget(self.password)
        self.open_login_layout.addSpacing(25)
        self.open_login_layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.open_login_layout.setAlignment(Qt.AlignCenter)
        self.open_login_layout.addSpacing(20)
        self.open_login_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignCenter)   

        self.remove_layouts_widgets(self.layout1)
        self.layout1.addWidget(self.open_login_bg)

    def login(self):
        
        username = self.username.text() #abhi_tapare
        password = self.password.text() #Abhishek

        try:
            # Retrieve user data from the database
            user_ref = db.collection('username').document(username)
            user_data = user_ref.get()
            if user_data.exists:
                # Check if the password matches
                if user_data.to_dict()['password'] == password:
                    # QMessageBox.information(self, "Login", "Login Successful!")
                    self.user_data_dict = user_data.to_dict()
                    
                    # print("Username:", self.user_data_dict['username'])
                    # print("Email:", self.user_data_dict['email'])
                    # print("Password:", self.user_data_dict['password'])

                    self.remove_layouts_widgets(self.layout1)
                    self.home_main_layout_wid = Home_Page().home_UI()
                    self.layout1.addWidget(self.home_main_layout_wid)
                else:
                    QMessageBox.warning(self, "Login", "Login Failed. Incorrect password.")
            else:
                QMessageBox.warning(self, "Login", "Login Failed. User not found.")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Login", "Login Failed. An error occurred.")
        login_info = open("./assets/setup/Login_in.txt","w")

        for val in self.user_data_dict.values():
            str1 = val + '\n\n'
            login_info.write(str1)

    def open_register(self):
        self.open_reg_layout = QVBoxLayout()
        # Background image (login page)
        self.reg_bg = QLabel()
        self.reg_bg.setPixmap(QPixmap("./assets/images/bg_blur.png"))
        self.reg_bg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reg_bg.setLayout(self.open_reg_layout)
        
        # Text label
        self.text_label3 = QLabel("Register As New User ") 
        self.text_label3.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 40px; font-weight: bold;")  
        self.text_label3.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        
        # name, mob. no, Username, email, password, and confirm password fields
        self.name_label = QLabel("<b>Name:</b>", self)
        self.name_label.setStyleSheet("color: black; font-family: comic sans ms; font-size: 22px;  font-weight: bold;")
        self.name = QLineEdit(self)
        self.name.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.name.setFixedWidth(450)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        initial_name_value = "Enter your name"
        self.name.setPlaceholderText(str(initial_name_value))

        self.mobno_label = QLabel("<b>Mobile Number:</b>", self)
        self.mobno_label.setStyleSheet(" color: black; font-family: comic sans ms; font-size: 22px; font-weight: bold;")
        self.mobno = QLineEdit(self)
        self.mobno.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.mobno.setFixedWidth(445)
        self.mobno_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        initial_mobno_value = "Enter your Mobile number"
        self.mobno.setPlaceholderText(str(initial_mobno_value))

        self.username_label = QLabel("<b>Username:</b>", self)
        self.username_label.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 22px; font-weight: bold;")
        self.username = QLineEdit(self)
        self.username.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.username.setFixedWidth(445)
        initial_username_value = "Enter your username"
        self.username.setPlaceholderText(str(initial_username_value))

        self.email_label = QLabel("<b>Email:</b>", self)
        self.email_label.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 22px; font-weight: bold;")
        self.email = QLineEdit(self)
        self.email.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.email.setFixedWidth(445)
        initial_email = "abc@gmail.com"
        self.email.setPlaceholderText(str(initial_email))

        self.password_label = QLabel("<b>Password:</b>", self)
        self.password_label.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 22px; font-weight: bold;")
        self.password = QLineEdit(self)
        self.password.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.password.setFixedWidth(445)
        self.password.setEchoMode(QLineEdit.Password)
        initial_password = "Enter your password"
        self.password.setPlaceholderText(str(initial_password))

        self.confirm_password_label = QLabel("<b>Confirm Password:</b>", self)
        self.confirm_password_label.setStyleSheet("color: black ; font-family: comic sans ms; font-size: 22px; font-weight: bold;")
        self.confirm_password = QLineEdit(self)
        self.confirm_password.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.confirm_password.setFixedWidth(445)
        self.confirm_password.setEchoMode(QLineEdit.Password)
        initial_confirm_password = "enter password again"
        self.confirm_password.setPlaceholderText(str(initial_confirm_password))

        # Register button
        self.register_button = QPushButton("📝 Register", self)
        self.register_button.setCursor(Qt.PointingHandCursor)
        self.register_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; font-family: comic sans ms; color: black; font-size: 30px; border-radius: 15px; min-width: 200px; min-height:50px;""}"
                                        "QPushButton:hover"
                                        "{""font-size: 33px; border-radius: 15px; min-width: 205px;min-height:51px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff;"
                                        "}")
        self.register_button.clicked.connect(self.register)

        self.back_button = QPushButton("🔙" ,self)
        self.back_button.setCursor(Qt.PointingHandCursor)
        self.back_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-size: 30px; border-radius: 15px; min-width: 110px; min-height:50px;""}"
                                        "QPushButton:hover"
                                         "{""font-size: 35px; border-radius: 15px; min-width: 115px;min-height:51px;""}"
                                        "QPushButton::pressed"
                                        "{""background-color: #80e5ff;""}")
        self.back_button.clicked.connect(self.go_back)
        
        self.open_reg_layout.addWidget(self.text_label3)
        self.open_reg_layout.addSpacing(35)
        self.open_reg_layout.addWidget(self.name_label)
        self.open_reg_layout.addWidget(self.name)
        self.open_reg_layout.addWidget(self.mobno_label)
        self.open_reg_layout.addWidget(self.mobno)
        self.open_reg_layout.addWidget(self.username_label)
        self.open_reg_layout.addWidget(self.username)
        self.open_reg_layout.addWidget(self.email_label)
        self.open_reg_layout.addWidget(self.email)
        self.open_reg_layout.addWidget(self.password_label)
        self.open_reg_layout.addWidget(self.password)
        self.open_reg_layout.addWidget(self.confirm_password_label)
        self.open_reg_layout.addWidget(self.confirm_password)
        self.open_reg_layout.addSpacing(20)
        self.open_reg_layout.addWidget(self.register_button, alignment=Qt.AlignCenter)
        self.open_reg_layout.setAlignment(Qt.AlignCenter)
        self.open_reg_layout.addSpacing(20)
        self.open_reg_layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        self.remove_layouts_widgets(self.layout1)
        self.layout1.addWidget(self.reg_bg)

    def register(self):
        name = self.name.text()
        mobno = self.mobno.text()
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if password == confirm_password:
            try:
                # Check if the username already exists
                user_ref = db.collection('username').document(username)
                if user_ref.get().exists:
                    QMessageBox.warning(self, "Register", "Username already exists. Please choose a different username.")
                else:
                    # Save user data to the database
                    user_ref.set({
                        'name' : name,
                        'mobno':mobno,
                        'username': username,
                        'password': password,
                        'email': email,
                        'confirm_password':confirm_password,
                    })
                    QMessageBox.information(self, "Register", "Registration Successful!")
                    self.remove_layouts_widgets(self.layout1)
                    self.layout1.addWidget(self.welcome_label)
                    self.layout1.addWidget(self.login_button1)
                    self.layout1.addSpacing(40)
                    self.layout1.addWidget(self.register_button1)
                    self.layout1.setAlignment(Qt.AlignCenter)

            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Register", "Registration Failed. Please try again later.")
        else:
            QMessageBox.warning(self, "Register", "Passwords do not match!")

    def go_back(self):
        self.remove_layouts_widgets(self.layout1)
        self.layout1.addWidget(self.welcome_label)
        self.layout1.addSpacing(40)
        self.layout1.addWidget(self.login_button1)
        self.layout1.addSpacing(40)
        self.layout1.addWidget(self.register_button1)

    def remove_layouts_widgets(self, tempLsy):
        while tempLsy.count():
            item = tempLsy.takeAt(0)
            widget = item.widget()
            
            if widget :
                tempLsy.removeWidget(widget)
                widget.setParent(None)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = SigninPage()
    main_window.show()
    sys.exit(app.exec_())

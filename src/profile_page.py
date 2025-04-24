import gettext
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
import json
from firebase_admin import credentials, firestore
from colorama import Fore , Back ,Style
# from sign_in import SigninPage

credentials_path ='N:/Project/farm-help/assets/setup/python-ffb5f-firebase-adminsdk-ck3ar-baf9776356.json'
with open(credentials_path)as json_file:
    credentials_info = json.load(json_file)
db=firestore.Client.from_service_account_info(credentials_info)

class ProfilePage(QWidget):
    def  __init__(self):
        super().__init__()
    
        self.profileUi()

    def profileUi(self):

        # Left side with buttons
        self.left_layout = QVBoxLayout()

        self.profile_button = QPushButton("Profile")
        self.profile_button.setCursor(Qt.PointingHandCursor)
        self.profile_button.setFixedSize(210, 50)
        self.profile_button.clicked.connect(lambda: self.show_profile_info())
        self.profile_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-size: 22px; border-radius: 15px;""}"
                                        "QPushButton:hover"
                                        "{""font-size: 23px; border-radius: 15px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff;"
                                        "}")

        self.about_button = QPushButton("About Us")
        self.about_button.setCursor(Qt.PointingHandCursor)
        self.about_button.setFixedSize(210, 50)
        self.about_button.clicked.connect(self.show_about_us_info)
        self.about_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-size: 22px; border-radius: 15px;""}"
                                        "QPushButton:hover"
                                        "{""font-size: 23px; border-radius: 15px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff;"
                                        "}")        

        self.policy_button = QPushButton("Policy")
        self.policy_button.setCursor(Qt.PointingHandCursor)
        self.policy_button.setFixedSize(210,50)
        self.policy_button.clicked.connect(self.show_policy_info)
        self.policy_button.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-size: 22px; border-radius: 15px;""}"
                                        "QPushButton:hover"
                                        "{""font-size: 23px; border-radius: 15px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff;"
                                        "}")        

        self.terms_condition = QPushButton("Terms and condition")
        self.terms_condition.setCursor(Qt.PointingHandCursor)
        self.terms_condition.setFixedSize(210,50)
        self.terms_condition.clicked.connect(self.show_terms_condition)
        self.terms_condition.setStyleSheet("QPushButton"
                                        "{""background-color: #99ffcc; color: black; font-size: 22px; border-radius: 15px;""}"
                                        "QPushButton:hover"
                                        "{""font-size: 23px; border-radius: 15px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff;"
                                        "}")     
        
        self.left_layout.addWidget(self.profile_button, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.about_button, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.policy_button, alignment=Qt.AlignLeft)
        self.left_layout.addWidget(self.terms_condition, alignment=Qt.AlignLeft)

        # Right side with information
        self.right_layout = QVBoxLayout()
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.info_label = QLabel('')
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setStyleSheet("color: red; font-family: comic sans ms; font-size: 50px;  font-weight: bold;")

        self.img_label = QLabel()
        self.img = QPixmap("assets\images\profile-img.png")
        self.img_label.setPixmap(self.img)
        self.img_label.setFixedSize(500,501)

        self.info_label1 = QLabel('')
        self.info_label1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.info_label1.setStyleSheet("color: black; font-family: comic sans ms; font-size: 20px;")
        
        self.info_label2 = QLabel('')
        self.info_label2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.info_label2.setStyleSheet("color: black; font-family: comic sans ms; font-size: 20px;")

        self.right_layout.addWidget(self.img_label)
        self.right_layout.addWidget(self.info_label)
        self.right_layout.addWidget(self.info_label2)
        self.right_layout.addWidget(self.info_label1)

        # profile BG
        self.profile_bg = QLabel()
        bg_pixmap = QPixmap("./assets/images/rblur.jpeg")
        self.profile_bg.setPixmap(bg_pixmap)
        self.profile_bg_layout = QHBoxLayout()
        self.profile_bg.setLayout(self.profile_bg_layout)
        self.profile_bg_layout.addLayout(self.left_layout)
        self.profile_bg_layout.addLayout(self.right_layout)

        self.profile_main_layout_wid = QWidget()
        self.profile_main_layout = QVBoxLayout(self.profile_main_layout_wid)    
        self.profile_main_layout.addWidget(self.profile_bg)
        self.profile_main_layout.addSpacing(150)
        
        return self.profile_main_layout_wid

    def show_profile_info(self):
        self.img_label.hide()
        self.info_label2.hide()
        self.info_label.setText("Profile info:")
        
        login_info = open("./assets/setup/Login_in.txt","r")
        data = login_info.read()
        data1 = str(data)
        self.info_label1.setText(data1)
        
    def show_about_us_info(self):
        self.img_label.hide()
        self.info_label2.show()
        self.info_label.setText("🌳 About Us ")
        self.info_label2.setText("""I'd like to extend my heartfelt gratitude to Shashi Bagal Sir, Core2web for their\nunwavering support and trust in my project. Your belief in my vision has been\na driving force, and I'm excited to share the fruits of our collective efforts.\n Thank you for this incredible opportunity...... """)
        self.info_label1.setText("""Group Members:\n\n1) Abhishek Tapare (Group Leader)\n2) Rushabh Pawar\n3) Nitin Munde\n4)Nikhil Patil\n5) Ajay Pawar""")
        
    def show_policy_info(self):
        self.info_label2.hide()
        self.img_label.hide()
        self.info_label.setText("🌳 Farmer Help App Privacy Policy")
        self.info_label1.setText("""➤➤This privacy policy describes how Farmer Help us collects, uses, and shares information about you\nand your use of our mobile application.\n
            By using the App, you agree to the terms of this policy.Information We Collect\n\n
            ● Personal Information: When you use the App, we may collect personal information such as your\nname, email address, phone number, and location.\n
            ● Farm Information: We may also collect information about your farm, including size, location,\nand crops grown.\n
            ● Usage Information: We collect information about how you use the App, such as the features\nyou use and the actions you take.\n\
            ➤➤How We Use Your Information\n
            ● Provide Services: We use your information to provide you with the services offered by the App, such as crop management tools and\n
            market information.\n
            ● Communicate with You: We may use your information to communicate with you about the App, including updates and new features.\n
            ● Improve the App: We use your information to improve the App and develop new features. Information Sharing\n
            ● Third-Party Service Providers: We may share your information with third-party service providers who help us operate the App.\n
            ● Legal Requirements: We may share your information when required by law or to protect our rights or the rights of others.\n
            ● Aggregate Information: We may share aggregate information that does not identify you personally, such as usage statistics.\n
            Your Choices\n
            ● Opt-Out: You may opt-out of receiving communications from us by following the instructions in the communication.""")
    
    def show_terms_condition(self):
        self.img_label.hide()
        self.info_label2.hide()
        self.info_label.setText("🌳 Terms & Conditions ")
        self.info_label1.setText("""  1.Introduction
        1.1 These Terms and Conditions govern your use of the Farm Help mobile application operated\n
        by Farm-Help.
        1.2 By accessing or using the App, you agree to be bound by these Terms. If you disagree with any\n
        part of these Terms, you may not access the App.
        
        2. User Accounts
        2.1 To access certain features of the App, you may be required to create an account. You agree to\n
        provide accurate, current, and complete information during the registration process.
        2.2 You are responsible for maintaining the confidentiality of your account and password and for\n
        restricting access to your account. You agree to accept responsibility for all activities that occur\n
        under your account.

        3. Prohibited Activities
        3.1 You may not use the App for any illegal or unauthorized purpose. You may not, in the use of the App, violate\n
         any laws in your jurisdiction.""")

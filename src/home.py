from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtCore import Qt, QSize,QPoint, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from firebase_admin import firestore
import json
from profile_page import ProfilePage
from add_rental import Rental_Page
from cart  import Cart_App


#Initialize Firestore client
credentials_path ='N:/Project/farm-help/assets/setup/userform-1420c-firebase-adminsdk-0lqqo-812dcde81b.json'
with open(credentials_path)as json_file:
    credentials_info = json.load(json_file)
db=firestore.Client.from_service_account_info(credentials_info)

class Home_Page(QWidget):
    
    def __init__(self):
        super().__init__()
        self.home_main_layout_wid = QWidget()
        self.home_main_layout = QVBoxLayout(self.home_main_layout_wid)
        self.upper_layout_wid = QWidget()
        self.upper_layout = QVBoxLayout(self.upper_layout_wid)
        self.bottom_layout_wid = QWidget()
        self.bottom_layout = QHBoxLayout(self.bottom_layout_wid)
        self.home_main_layout.addWidget(self.upper_layout_wid)
        self.home_main_layout.addWidget(self.bottom_layout_wid)
        
    def home_UI(self):

        # Logo and Heading
        self.logo_label = QLabel()
        self.logo_Movie = QMovie("assets\images\htractor-logo.gif")
        self.logo_label.setMovie(self.logo_Movie)
        self.logo_label.setFixedSize(125, 120)
        self.logo_Movie.start()
        
        self.heading_label = QLabel("Farm-Help")
        self.heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.heading_label.setStyleSheet(("color: GREEN; font-weight: bold; font-size: 60px; font-family: snap itc;"))
        self.heading_label.setFixedSize(500,120)

        self.logo_label1 = QLabel()
        self.logo_Movie1 = QMovie("assets\images\han-shake.gif")
        self.logo_label1.setMovie(self.logo_Movie1)
        self.logo_label1.setFixedSize(225, 120)
        self.logo_Movie1.start()

        # button and label
        self.button1 = QPushButton()
        self.button1.setCursor(Qt.PointingHandCursor)
        self.button1.setIcon(QIcon("./assets/images/eqp.png"))
        self.button1.setIconSize(QSize(60, 70))
        self.button1.clicked.connect(self.fetch_rental_records)
        self.button1.setStyleSheet("QPushButton"
                                   "{""background-color: transparent; border:none;""}"
                                    "QPushButton:hover"
                                    "{""border: 2px solid #CCCCFF""}"
                                    "QPushButton::pressed"
                                    "{""background-color: #80e5ff;""}")

        self.text_label1 = QLabel("EQUIPMENTS")
        self.text_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label1.setStyleSheet("background-color: #99ffcc; color: black; font-family: comic sans ms; font-size: 15px; border: 2px solid #CCCCFF; border-radius: 5px; padding: 5px;")
        self.text_label1.setFixedSize(130,30)
 
        self.button2 = QPushButton()
        self.button2.setCursor(Qt.PointingHandCursor)
        self.button2.setIcon(QIcon("./assets/images/fertilizer.png"))
        self.button2.setIconSize(QSize(50, 50))
        self.button2.clicked.connect(self.go_to_Fertilizer)
        self.button2.setStyleSheet("QPushButton"
                                   "{""background-color: transparent; border:none;""}"
                                    "QPushButton:hover"
                                    "{""border: 2px solid #CCCCFF""}"
                                    "QPushButton::pressed"
                                    "{""background-color: #80e5ff;""}")
        

        self.text_label2 = QLabel("FERTILIZER")
        self.text_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label2.setStyleSheet("background-color: #99ffcc; color: black; font-family: comic sans ms; font-size: 15px; border: 2px solid #CCCCFF; border-radius: 5px; padding: 5px;")
        self.text_label2.setFixedSize(140,30)

        self.button3 = QPushButton()
        self.button3.setCursor(Qt.PointingHandCursor)
        self.button3.setIcon(QIcon("./assets/images/land.jpg"))
        self.button3.setIconSize(QSize(60,60))
        self.button3.clicked.connect(self.go_to_land_lease)
        self.button3.setStyleSheet("QPushButton"
                                   "{""background-color: transparent; border:none;""}"
                                    "QPushButton:hover"
                                    "{""border: 2px solid #CCCCFF""}"
                                    "QPushButton::pressed"
                                    "{""background-color: #80e5ff;""}")

        self.text_label3 = QLabel("LAND LEASE")
        self.text_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label3.setStyleSheet("background-color: #99ffcc; color: black; font-family: comic sans ms; font-size: 15px; border: 2px solid #CCCCFF; border-radius: 5px; padding: 5px;")
        self.text_label3.setFixedSize(140,30)

        self.button4 = QPushButton()
        self.button4.setCursor(Qt.PointingHandCursor)
        self.button4.setIcon(QIcon("./assets/images/add_feature.png"))
        self.button4.setIconSize(QSize(50,50))
        self.button4.setStyleSheet("QPushButton"
                                   "{""background-color: transparent; border:none;""}"
                                    "QPushButton:hover"
                                    "{""border: 2px solid #CCCCFF""}"
                                    "QPushButton::pressed"
                                    "{""background-color: #80e5ff;""}")

        self.text_label4 = QLabel("Comming Soon")
        self.text_label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label4.setStyleSheet("background-color: #99ffcc; color: black; font-family: comic sans ms; font-size: 15px; border: 2px solid #CCCCFF; border-radius: 5px; padding: 5px;")
        self.text_label4.setFixedSize(140,30)

        # image
        self.img_label = QLabel()
        self.img_label.setStyleSheet("background-color: transparent;")
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_pixmap = QPixmap("./assets/images/img1.png")
        self.img_label.setPixmap(img_pixmap)

        # Home, Profile, Add Rental, Total Buttons
        self.home_button = QPushButton()
        self.home_button.setCursor(Qt.PointingHandCursor)
        self.home_button.setText("🏠 Home")
        self.home_button.clicked.connect(self.go_to_home)
        self.home_button.setStyleSheet("QPushButton"
                                            "{""background-color: #FF9966; color: black; font-family: comic sans ms; font-size: 20px; border-radius: 17px; min-height:40px;""}"
                                            "QPushButton:hover"
                                            "{""background-color: #99ffcc; font-size: 23px; border-radius: 17px; min-height:43px;""}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color: #80e5ff;"
                                            "}")

        self.profile_button = QPushButton()
        self.profile_button.setCursor(Qt.PointingHandCursor)
        self.profile_button.setText("👤 Profile")
        self.profile_button.clicked.connect(self.go_to_profile)
        self.profile_button.setStyleSheet("QPushButton"
                                            "{""background-color: #FF9966; color: black; font-family: comic sans ms; font-size: 20px; border-radius: 17px; min-height:40px;""}"
                                            "QPushButton:hover"
                                            "{""background-color: #99ffcc; font-size: 23px; border-radius: 17px; min-height:43px;""}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color: #80e5ff;"
                                            "}")

        self.add_rental_button = QPushButton()
        self.add_rental_button.setCursor(Qt.PointingHandCursor)
        self.add_rental_button.setText("➕ Add Product")
        self.add_rental_button.clicked.connect(lambda : self.go_to_add_product())
        self.add_rental_button.setStyleSheet("QPushButton"
                                            "{""background-color: #FF9966; color: black; font-family: comic sans ms; font-size: 20px; border-radius: 17px; min-height:40px;""}"
                                            "QPushButton:hover"
                                            "{""background-color: #99ffcc; font-size: 23px; border-radius: 17px; min-height:43px;""}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color: #80e5ff;"
                                            "}")

        self.cart_button = QPushButton()
        self.cart_button.setCursor(Qt.PointingHandCursor)
        self.cart_button.setText("🛒 CART")
        self.cart_button.clicked.connect(self.go_to_cart)
        self.cart_button.setStyleSheet("QPushButton"
                                            "{""background-color: #FF9966; color: black; font-family: comic sans ms; font-size: 20px; border-radius: 17px; min-height:40px;""}"
                                            "QPushButton:hover"
                                            "{""background-color: #99ffcc; font-size: 23px; border-radius: 17px; min-height:43px;""}"
                                            "QPushButton::pressed"
                                            "{"
                                            "background-color: #80e5ff;"
                                            "}")
        # Layouts
        
        self.top_layout_wid = QWidget()
        self.top_layout = QHBoxLayout()
        self.top_layout_wid.setLayout(self.top_layout)
        self.top_layout.addWidget(self.logo_label)
        self.top_layout.addWidget(self.heading_label)
        self.top_layout.addWidget(self.logo_label1)
        # self.top_layout.addSpacing(120)

        self.big_layout_wid = QWidget()
        self.big_layout = QHBoxLayout(self.big_layout_wid)
        self.big_layout.setAlignment(Qt.AlignCenter)
        self.left_layout = QVBoxLayout()
        self.left_layout.setAlignment(Qt.AlignLeft)

        self.right_widget = QWidget()
        self.right_layout = QHBoxLayout(self.right_widget)
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        #Scroll Area for records
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("border: none; background-color: transparent;")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.right_widget)

        self.big_layout.addLayout(self.left_layout,2)
        self.big_layout.addWidget(self.scroll_area,7)

        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.text_label1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.text_label2)
        self.left_layout.addWidget(self.button3)
        self.left_layout.addWidget(self.text_label3)
        self.left_layout.addWidget(self.button4)
        self.left_layout.addWidget(self.text_label4)

        self.right_layout.addWidget(self.img_label)

        self.upper_layout.addWidget(self.top_layout_wid)
        self.upper_layout.addWidget(self.big_layout_wid)
        self.upper_layout.addSpacing(60)
        
        self.bottom_layout.addWidget(self.home_button)
        self.bottom_layout.addWidget(self.add_rental_button)
        self.bottom_layout.addWidget(self.cart_button)
        self.bottom_layout.addWidget(self.profile_button)
        self.home_main_layout.addLayout(self.upper_layout)
        
        return self.home_main_layout_wid

    def fetch_rental_records(self):
        #Fetch data from Firestore
        user_profile_ref = db.collection('user_profiles')
        user_profiles = user_profile_ref.stream()

        self.remove_layouts_widgets(self.right_layout)
        
        #display records in the right layout
        count = 1
        # records_text =""
        self.cart_list = []
        for user_profile in user_profiles:
            user_data = user_profile.to_dict()
            eqp_list_wid = QWidget()
            eqp_list_layout = QVBoxLayout(eqp_list_wid)
            self.record_label = QLabel()
            self.record_label.setFixedSize(250,250)
            add_to_cart = QPushButton()
            add_to_cart.setCursor(Qt.PointingHandCursor)
            add_to_cart.setText("Add To Cart")
            add_to_cart.setStyleSheet("QPushButton"
                                        "{""background-color: #FF9933; color: black; font-size: 15px; font-weight: bold; border-radius: 15px; min-width: 15px; min-height:30px;""}"
                                        "QPushButton:hover"
                                        "{""background-color: #FF6600;font-size: 17px; border-radius: 15px; min-width: 16px;min-height:31px;""}"
                                        "QPushButton::pressed"
                                        "{""background-color: #80e5ff;""}")

            # Convert the user profile dictionary into a tuple
            user_profile_tuple = tuple(user_data.items())
            
            records_text = f"Record: {count}\n"\
                f"Name:{user_data['first_name']} {user_data['last_name']}\n"\
                f"Mobile No: {user_data['mobile_no']}\n"\
                f"Product Name: {user_data['product_name']}\n"\
                f"Product Info: {user_data['product_info']}\n"\
                f"Quantity: {user_data['quantity']}\n"\
                f"Price: {user_data['price']}Rs\n"\

            self.record_label.setText(records_text)
            self.record_label.setStyleSheet("background-color: #FFFF99; font-family: comic sans ms; font-size: 15px; border: 1px solid black; padding: 5px; border-radius: 10px")
            eqp_list_layout.addWidget(self.record_label)
            eqp_list_layout.addWidget(add_to_cart)
            self.right_layout.addWidget(eqp_list_wid)
            add_to_cart.clicked.connect(lambda _, user_profile_tuple=user_profile_tuple:  self.addToCart(user_profile_tuple))
            count+=1
            if count%2==0:
                self.record_label.setStyleSheet("background-color: #FFFFCC; font-family: comic sans ms; font-size: 15px; border: 1px solid black; padding: 5px; border-radius:10px")
            # self.right_layout.addSpacing(10)

    def addToCart(self,record_text):
        self.cart_list.append(record_text)
        with open ('./assets/setup/cart.json','w') as f:
            json.dump(self.cart_list ,f  ,indent=3)       

    def go_to_Fertilizer(self):
        self.remove_layouts_widgets(self.right_layout)
        self.fertilizer_label = QLabel()
        self.comming_movie = QMovie("assets\images\comming-soon.gif")
        self.fertilizer_label.setMovie(self.comming_movie)
        self.comming_movie.start()

        self.men_label = QLabel()
        self.men_movie = QMovie("assets\images\seed-seeding.gif")
        self.men_label.setMovie(self.men_movie)
        self.men_movie.start()

        self.right_layout.addWidget(self.fertilizer_label)
        self.right_layout.addSpacing(20)
        self.right_layout.addWidget(self.men_label)
        self.fertilizer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def go_to_land_lease(self):
        self.remove_layouts_widgets(self.right_layout)
        self.lease_label = QLabel()
        self.comming_movie = QMovie("assets\images\comming-soon.gif")
        self.lease_label.setMovie(self.comming_movie)
        self.comming_movie.start()
        self.right_layout.addWidget(self.lease_label)
        self.lease_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def go_to_home(self):
        self.remove_layouts_widgets(self.upper_layout)
        self.remove_layouts_widgets(self.bottom_layout)
        self.home_UI()
        self.upper_layout.addWidget(self.top_layout_wid)
        self.upper_layout.addWidget(self.big_layout_wid)
        self.upper_layout.addSpacing(90)

    def go_to_profile(self):
        self.remove_layouts_widgets(self.upper_layout)
        self.profile_main_layout_wid = ProfilePage().profileUi()
        self.upper_layout.addWidget(self.profile_main_layout_wid)

    def go_to_cart(self,cart_list):
        self.remove_layouts_widgets(self.upper_layout)
        self.cart_list = cart_list
        self.cart_main_layout_wid = Cart_App().cart_ui()
        self.upper_layout.addWidget(self.cart_main_layout_wid)
    
    def go_to_add_product(self):
        print("In go to product")
        self.remove_layouts_widgets(self.upper_layout)
        self.rental_main_layout_wid = Rental_Page().rental_ui()
        self.upper_layout.addWidget(self.rental_main_layout_wid)

    def remove_layouts_widgets(self, tempLsy):
        while tempLsy.count():
            item = tempLsy.takeAt(0)
            widget = item.widget()

            if widget :
                tempLsy.removeWidget(widget)
                widget.deleteLater()
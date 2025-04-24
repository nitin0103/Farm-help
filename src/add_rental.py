import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout,QFileDialog, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import json
import firebase_admin
from firebase_admin import credentials, firestore

#Initialize Firestore client
credentials_path ='N:/Project/farm-help/assets/setup/userform-1420c-firebase-adminsdk-0lqqo-812dcde81b.json'
with open(credentials_path)as json_file:
    credentials_info = json.load(json_file)
db=firestore.Client.from_service_account_info(credentials_info)

class Rental_Page(QWidget):
    def __init__(self):
        super().__init__()
        
        self.rental_ui()
    
    def rental_ui(self):
        self.rental_main_layout_wid = QWidget()

        #form-layout BG
        self.r_layout_bg = QLabel()
        bg_pixmap = QPixmap("./assets/images/rblur.jpeg")
        self.r_layout_bg.setPixmap(bg_pixmap)

        # Header
        
        header_label = QLabel('Add Rental Equipment')
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('background-color: #003A6B; color: White; padding:10px; font-family: comic sans ms; font-size:35px; max-height:45px')

        # Form Elements
        self.first_name_edit = QLineEdit()
        self.first_name_edit.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.first_name_edit.setFixedWidth(250)
        self.first_name_edit.setMaxLength(20)

        self.last_name_edit = QLineEdit()
        self.last_name_edit.setStyleSheet("color: black ; font-size: 20px;border: 3px solid #99ffcc ; border-radius: 5px;")
        self.last_name_edit.setMaxLength(20)
        self.last_name_edit.setFixedWidth(250)

        self.mobile_no_edit = QLineEdit()
        self.mobile_no_edit.setStyleSheet("color: black ; font-size: 20px;border: 3px solid #99ffcc ; border-radius: 5px;")
        self.mobile_no_edit.setMaxLength(13)
        self.mobile_no_edit.setFixedWidth(250)

        self.product_name_edit = QLineEdit()
        self.product_name_edit.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.product_name_edit.setMaxLength(20)
        self.product_name_edit.setFixedWidth(250)

        self.product_info_edit = QLineEdit()
        self.product_info_edit.setStyleSheet("color: black ; font-size: 20px;border: 3px solid #99ffcc ; border-radius: 5px;")
        self.product_info_edit.setMaxLength(20)
        self.product_info_edit.setFixedWidth(250)

        self.quantity = QLineEdit()
        self.quantity.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.quantity.setMaxLength(20)
        self.quantity.setFixedWidth(250)

        self.Price = QLineEdit()
        self.Price.setStyleSheet("color: black ; font-size: 20px; border: 3px solid #99ffcc ; border-radius: 5px;")
        self.Price.setMaxLength(20)
        self.Price.setFixedWidth(250)

        # Form layout
        form_widget = QWidget()
        form_layout1 = QFormLayout(form_widget)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">First Name:</span>', self.first_name_edit)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">Last Name:</span>', self.last_name_edit)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">Mobile No:</span>', self.mobile_no_edit)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">Product Name:</span>', self.product_name_edit)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">Product Information:</span>', self.product_info_edit)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">Number of Quantity:</span>', self.quantity)
        form_layout1.addRow('<span style="font-size: 20px; font-family: comic sans ms;">Product Price Per day:</span>', self.Price)

        self.save_button = QPushButton('Save')
        self.save_button.setCursor(Qt.PointingHandCursor)
        self.save_button.setFixedSize(150, 50)
        self.save_button.setStyleSheet("QPushButton"
                                        "{""background-color: #003A6B; color: White; font-size: 25px; border-radius: 15px; min-width: 150px; min-height:50px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #99ffcc; color: black;"
                                        "}")
        self.save_button.clicked.connect(lambda : self.save_data())

        self.r_layout = QVBoxLayout()
        self.r_layout_bg.setLayout(self.r_layout)
        self.r_layout.addWidget(header_label)
        self.r_layout.addWidget(form_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.r_layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # rental-main-layout
        self.rental_main_layout = QVBoxLayout(self.rental_main_layout_wid)
        self.rental_main_layout.addWidget(self.r_layout_bg)
        self.rental_main_layout.addSpacing(150)
        self.setLayout(self.rental_main_layout)

        return self.rental_main_layout_wid
            
    def save_data(self):
        
        # Gather data from input fields
        if not self.first_name_edit.text() or not self.last_name_edit.text() or not self.mobile_no_edit.text() or not self.product_name_edit.text() or not self.product_info_edit.text() or not self.quantity.text() or not self.Price.text():
        # Display an error message if any of the required fields are empty
            QMessageBox.critical(self, "Error", "Please fill in all required fields.")
            return 
    
        #Mobile number validation
        mobile_no = self.mobile_no_edit.text()

        if not mobile_no.isdigit() or len(mobile_no) != 10:
            QMessageBox.critical(self, "Error", "Please enter a valid 10-digit mobile number.")
            return 
        
        #Quantity validation
        Quantity = self.quantity.text()
        if not Quantity.isdigit():
            QMessageBox.critical(self, "Error", "Please enter quantiy in digit format.")
            return
        
        #Price validation
        price_of_pro = self.Price.text()
        if not price_of_pro.isdigit():
            QMessageBox.critical(self, "Error", "Please enter price in digit format.")
            return
        
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        mobile_no = self.mobile_no_edit.text()
        product_name = self.product_name_edit.text()
        product_info = self.product_info_edit.text()
        quantity = self.quantity.text()
        price = self.Price.text()

        # Prepare data to be saved
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_no': mobile_no,
            'product_name': product_name,
            'product_info': product_info,
            'quantity': quantity,
            'price': price
        }
        print("Data SAVED ")

        # Save data to Firestore
        doc_ref = db.collection('user_profiles').document()  # Provide a unique document ID here
        doc_ref.set(data)
        QMessageBox.information(self, 'Success', 'Data saved successfully!')  
        self.first_name_edit.clear()
        self.last_name_edit.clear()
        self.mobile_no_edit.clear()
        self.product_name_edit.clear()
        self.product_info_edit.clear()
        self.quantity.clear()
        self.Price.clear()  
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = Rental_Page()
#     ui.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLabel, QMessageBox, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import json
class Cart_App(QWidget):
    def __init__(self):
        super().__init__()
    
        self.cart_ui()

    def cart_ui(self):
        # cart BG
        self.cart_bg = QLabel()
        bg_pixmap = QPixmap("C:/Users/nitin/OneDrive/Desktop/Final/farmer-help/farm-help/assets/setup/cart.json")
        self.cart_bg.setPixmap(bg_pixmap)

        with open('./assets/setup/cart.json', 'r') as f:
            data = json.load(f)

        # Extract product_name and price and create a dictionary to map product names to prices
        product_price_map = {}
        for item in data:
            for sublist in item:
                if sublist[0] == 'product_name':
                    product_name = sublist[1]
                elif sublist[0] == 'price':
                    price = sublist[1]
                    if product_name:
                        product_price_map[product_name] = float(price)
                        product_name = None

        # List of items
        self.cart_list_wid = QListWidget()
        self.cart_list_wid.setStyleSheet("color: black; font-family: comic sans ms; font-size: 22px; border: none;")
        for name in product_price_map:
            self.cart_list_wid.addItem(name)

        # Cart
        self.final_cart_list = QListWidget(self)
        self.final_cart_list.setStyleSheet("QListWidget"
                                           "{""color: black; font-family: comic sans ms; font-size: 22px; border: none;""}"
                                           "QListView::item:selected"
                                            "{""color: black; background-color : #FFFFCC;""}") 


        # Total price label
        self.total_price_label = QLabel('Total Price: 0.00', self)
        self.total_price_label.setStyleSheet("color: black ; font-size: 20px; font-weight: bold;")

        # Buttons
        self.buy_now_button = QPushButton('BOOK', self)
        self.buy_now_button.setCursor(Qt.PointingHandCursor)
        self.buy_now_button.setStyleSheet("QPushButton"
                                        "{""background-color: #ffa64d; color: black; font-size: 25px; font-weight: bold; border-radius: 15px; min-width: 150px; min-height:50px;""}"
                                        "QPushButton::pressed"
                                        "{"
                                        "background-color: #80e5ff; color: black;"
                                        "}")
        self.buy_now_button.clicked.connect(self.show_order_confirmation)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.cart_list_wid)

        cart_layout = QVBoxLayout()
        cart_layout.addWidget(self.final_cart_list)
        cart_layout.addWidget(self.total_price_label)
        cart_layout.addWidget(self.buy_now_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add "Add to Cart" buttons next to each item
        for i in range(self.cart_list_wid.count()):
            item_name = self.cart_list_wid.item(i).text()
            price = product_price_map[item_name]
            add_to_cart_button = QPushButton(f'Product: ({item_name}) - Rs{price:.2f}', self)
            add_to_cart_button.setCursor(Qt.PointingHandCursor)
            add_to_cart_button.setStyleSheet("QPushButton"
                                             "{""background-color: #99ffcc; color: black; font-size: 20px; min-width: 200px;""}"
                                             "QPushButton:hover"
                                             "{""background-color: #99FFFF; font-size: 21px;""}")
            add_to_cart_button.clicked.connect(lambda _, name=item_name, price=price: self.final_cart(name, price))
            self.cart_list_wid.setItemWidget(self.cart_list_wid.item(i), add_to_cart_button)

        # Set up context menu for items in the cart
        self.final_cart_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.final_cart_list.customContextMenuRequested.connect(self.show_context_menu)

        # Connect item click event to confirmation dialog
        self.final_cart_list.itemClicked.connect(self.confirm_remove_from_cart)

        # Layouts
        self.cart_bg_layout = QHBoxLayout()
        self.cart_bg.setLayout(self.cart_bg_layout)
        self.cart_bg_layout.addLayout(layout)
        self.cart_bg_layout.addLayout(cart_layout)

        self.cart_main_layout_wid = QWidget()
        main_layout = QVBoxLayout(self.cart_main_layout_wid)
        main_layout.addWidget(self.cart_bg)
        main_layout.addSpacing(150)
        return self.cart_main_layout_wid
    
    def final_cart(self, item_name, item_price):
        self.final_cart_list.addItem(f'{item_name} - Rs{item_price:.2f}')
        self.update_total_price()

    def remove_from_cart(self, item_name):
        item_row = self.final_cart_list.findItems(item_name, Qt.MatchExactly)
        if item_row:
            row = self.final_cart_list.row(item_row[0])
            self.final_cart_list.takeItem(row)
            self.update_total_price()

    def update_total_price(self):
        self.total_price = sum(float(item.text().split()[-1][2:]) for item in self.final_cart_list.findItems('*', Qt.MatchWildcard))
        self.total_price_label.setText(f'Total Price: Rs{self.total_price:.2f}')
    
    def show_order_confirmation(self):
        cart_items = [self.final_cart_list.item(i).text() for i in range(self.final_cart_list.count())]
        if not cart_items:
            QMessageBox.warning(self, 'Empty Cart', 'Please add items to the cart before purchasing.')
            return

    # Calculate total price
        confirmation_message = f"Your order is successfully placed!\n\nItems:\n{', '.join(cart_items)}\n\nTotal Price: Rs{self.total_price:.2f}"
        QMessageBox.information(self, 'Order Confirmation', confirmation_message)

    def show_context_menu(self, point):
        item = self.final_cart_list.itemAt(point)
        if item:
            item_name = item.text()
            menu = QMenu(self)
            remove_action = QAction(f'Remove Product ({item_name})', self)
            remove_action.triggered.connect(lambda _, name=item_name: self.remove_from_cart(name))
            menu.addAction(remove_action)
            menu.exec_(self.final_cart_list.mapToGlobal(point))

    def confirm_remove_from_cart(self, item):
        confirmation = QMessageBox.question(self, 'Remove Product', f'Do you want to remove "{item.text()}" from the cart?', QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.remove_from_cart(item.text())

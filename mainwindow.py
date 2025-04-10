from PyQt5 import QtWidgets, uic
import sys
import resources_rc  # Import the compiled resource file
from Case_study import menu, orders, apply_discount

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("mainwindow.ui", self)

        self.btnPlaceOrder = self.findChild(QtWidgets.QPushButton, "btnPlaceOrder")
        self.btnConfirmOrder = self.findChild(QtWidgets.QPushButton, "btnConfirmOrder")
        self.btnExit = self.findChild(QtWidgets.QPushButton, "btnExit")

        self.btnPlaceOrder.clicked.connect(self.show_menu_window)
        self.btnConfirmOrder.clicked.connect(self.show_order_summary)
        self.btnExit.clicked.connect(self.close)

        self.show()

    def show_menu_window(self):
        self.menu_window = QtWidgets.QWidget()
        self.menu_window.setWindowTitle("📋 Menu - Select Items")
        layout = QtWidgets.QVBoxLayout()

        self.item_selectors = {}

        for item_id, item in menu.items():
            row = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(f"{item['name']} - ${item['price']:.2f}")
            spin = QtWidgets.QSpinBox()
            spin.setRange(0, 10)
            self.item_selectors[item_id] = spin
            row.addWidget(label)
            row.addWidget(spin)
            layout.addLayout(row)

        add_btn = QtWidgets.QPushButton("Add to Order")
        add_btn.clicked.connect(self.add_to_order)
        layout.addWidget(add_btn)

        self.menu_window.setLayout(layout)
        self.menu_window.show()

    def add_to_order(self):
        for item_id, spin in self.item_selectors.items():
            qty = spin.value()
            if qty > 0:
                item = menu[item_id]
                total = item['price'] * qty
                orders.append((item['name'], qty, total))
        QtWidgets.QMessageBox.information(self, "Success", "Items added to order.")
        self.menu_window.close()

    def show_order_summary(self):
        if not orders:
            QtWidgets.QMessageBox.information(self, "Order Summary", "Your order is empty.")
            return

        summary = "Your Order:\n\n"
        total_amount = 0
        for item, qty, price in orders:
            summary += f"{item} x{qty} = ${price:.2f}\n"
            total_amount += price

        discount_code, ok = QtWidgets.QInputDialog.getText(self, "Discount", "Enter discount code (if any):")
        if ok and discount_code.strip() == "SAVE10":
            total_amount = apply_discount(total_amount, 10)
            summary += "\n10% discount applied."
        elif discount_code:
            summary += "\nInvalid discount code."

        summary += f"\n\nTotal: ${total_amount:.2f}"
        confirm = QtWidgets.QMessageBox.question(self, "Confirm Order", summary, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            QtWidgets.QMessageBox.information(self, "Order Placed", "Thank you for your order!")
        else:
            orders.clear()
            QtWidgets.QMessageBox.information(self, "Cancelled", "Your order has been cancelled.")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
sys.exit(app.exec_())
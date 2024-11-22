Inventory Management System
A Python-based Inventory Management System (IMS) with a Graphical User Interface (GUI), designed to manage products, track inventory levels, and generate low-stock alerts. It also features user authentication for secure access.

Features
1. User Authentication
Secure login with hardcoded credentials for demonstration purposes.
Prevents unauthorized access to the system.
2. Product Management
Add new products with ID, name, quantity, and price.
Edit existing products.
Delete products from the inventory.
3. Inventory Tracking
View the entire inventory with details like product ID, name, quantity, and price.
Automatically saves data in a JSON file for persistence.
4. Low Stock Alerts
Alerts when product quantities drop below a predefined threshold (5 units by default).
5. Graphical User Interface (GUI)
User-friendly interface built using Python’s tkinter library.
Intuitive controls for managing inventory efficiently.
Prerequisites
Python 3.6 or later installed on your system.
The tkinter library (bundled with Python).
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system
Run the script:

bash
Copy code
python inventory_system.py
Log in using the default credentials:

Username: admin
Password: password123
Start managing your inventory!

File Structure
bash
Copy code
.
├── inventory_system.py   # Main program file
├── inventory_data.json   # Persistent storage for inventory (auto-created)
├── README.md             # Documentation
Usage
Login: Enter valid credentials to access the system.
Manage Products:
Fill in the product details and click Add Product to add a new product.
Select a product from the inventory list to edit or delete it.
Track Inventory:
View the inventory list for all products.
Use the Low Stock Alert button to identify products with low inventory.
Exit: Close the GUI to end the session.
Sample Screenshots
Login Screen

Inventory Management

Future Enhancements
Multi-user authentication with a database.
Advanced reporting (e.g., sales summaries, inventory trends).
Support for barcode scanning.
Export inventory reports as Excel or PDF.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

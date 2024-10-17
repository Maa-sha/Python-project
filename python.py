# Define the product catalog as a list of dictionaries
cart = []
def list_products(): """List all products in the catalog""" print("\nProduct List:")
for product in products:
print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']:.2f}")
def add_to_cart(product_id, quantity): """Add a product to the cart"""
for product in products:
if product['id'] == product_id:
cart.append((product_id, quantity))
print(f"Added {quantity} of {product['name']} to the cart.")
return
print("Product not found.")
def view_cart(): """View all items in the cart"""
if not cart:
print("\nYour cart is empty.")
return
print("\nShopping Cart:")
for item in cart:
product = next((prod for prod in products if prod['id'] == item[0]), None)
if product:
print(f"Product ID: {product['id']}, Name: {product['name']}, Quantity: {item[1]}")
def checkout(): """Calculate the total price of items in the cart and clear the cart"""
total = 0.0
for item in cart:
product = next((prod for prod in products if prod['id'] == item[0]), None)
if product:
total += product['price'] * item[1]
print(f"\nTotal amount: {total:.2f}")
cart.clear()
def main():
while True:
print("\n1. List Products")
print("2. Add to Cart")
print("3. View Cart")
print("4. Checkout")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == '1':
list_products()
elif choice == '2':
product_id = int(input("Enter Product ID to add to cart: "))
quantity = int(input("Enter Quantity: "))
add_to_cart(product_id, quantity)
elif choice == '3':
view_cart()
elif choice == '4':
checkout()
elif choice == '5':
break
else:
print("Invalid choice, please try again.")
if "_main_":
main()
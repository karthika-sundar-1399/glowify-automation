from pages.home_page import HomePage  # Import HomePage class for home page interactions
from pages.product_list_page import ProductListPage  # Import ProductListPage class for product listing interactions
from pages.product_detail_page import ProductDetailPage  # Import ProductDetailPage class for product detail page interactions
from pages.cart_page import CartPage  # Import CartPage class for shopping cart interactions
from pages.login_page import LoginPage  # Import LoginPage class for login page interactions
from pages.signup_page import SignupPage  # Import SignupPage class for signup/registration interactions
from pages.checkout_page import CheckoutPage  # Import CheckoutPage class for checkout process interactions


def test_full_user_journey(get_driver):  # Main end-to-end test function that simulates complete user purchase journey

    driver = get_driver  # Get the WebDriver instance from the test fixture

    home = HomePage(driver)  # Initialize HomePage page object with driver
    product_list = ProductListPage(driver)  # Initialize ProductListPage page object with driver
    product_detail = ProductDetailPage(driver)  # Initialize ProductDetailPage page object with driver
    cart = CartPage(driver)  # Initialize CartPage page object with driver
    login = LoginPage(driver)  # Initialize LoginPage page object with driver
    signup = SignupPage(driver)  # Initialize SignupPage page object with driver
    checkout = CheckoutPage(driver)  # Initialize CheckoutPage page object with driver

    # Step 1  # Comment indicating the first step of the journey
    home.open()  # Open the home page of the Glowify cosmetics website

    # Step 2  # Comment indicating navigation to lipsticks section
    home.go_to_lipsticks()  # Navigate to the lipsticks category via the shop menu dropdown

    # Step 3  # Comment indicating product selection
    product_list.select_first_product()  # Select the first product from the lipsticks product list

    # Step 4  # Comment indicating adding product to cart and navigation
    product_detail.add_product_to_cart()  # Add the selected product to the shopping cart
    product_detail.go_to_cart()  # Navigate to the shopping cart page

    # Step 5  # Comment indicating proceeding to checkout
    cart.proceed_to_checkout()  # Proceed to checkout from the cart page

    # 🔥 SMART LOGIN CHECK  # Comment indicating intelligent login verification logic
    if not home.is_logged_in():  # Check if user is not logged in

        login.go_to_signup()  # Navigate from login page to signup page
        signup.register_user()  # Register a new user account with test data

        home.open()  # Re-open the home page after registration

        # Re-add product after signup  # Comment indicating re-adding product after user registration
        home.go_to_lipsticks()  # Navigate back to lipsticks section
        product_list.select_first_product()  # Re-select the first product
        product_detail.add_product_to_cart()  # Re-add product to cart
        product_detail.go_to_cart()  # Navigate back to cart

    # Step 6  # Comment indicating proceeding to checkout again (after login/signup if needed)
    cart.proceed_to_checkout()  # Proceed to checkout (may require authentication)

    # Step 7  # Comment indicating filling checkout details
    checkout.fill_details()  # Fill in the checkout form with test shipping/billing information

    # Step 8  # Comment indicating placing the order
    checkout.place_order_click()  # Click the place order button to initiate purchase

    # Step 9  # Comment indicating payment popup verification
    checkout.verify_payment_popup()  # Verify that the Razorpay payment popup appears
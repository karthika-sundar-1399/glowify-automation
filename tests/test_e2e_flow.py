from pages.home_page import HomePage
from pages.product_list_page import ProductListPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.checkout_page import CheckoutPage


def test_full_user_journey(get_driver):

    driver = get_driver

    home = HomePage(driver)
    product_list = ProductListPage(driver)
    product_detail = ProductDetailPage(driver)
    cart = CartPage(driver)
    login = LoginPage(driver)
    signup = SignupPage(driver)
    checkout = CheckoutPage(driver)

    # Step 1
    home.open()

    # Step 2
    home.go_to_lipsticks()

    # Step 3
    product_list.select_first_product()

    # Step 4
    product_detail.add_product_to_cart()
    product_detail.go_to_cart()

    # Step 5
    cart.proceed_to_checkout()

    # 🔥 SMART LOGIN CHECK
    if not home.is_logged_in():

        login.go_to_signup()
        signup.register_user()

        home.open()

        # Re-add product after signup
        home.go_to_lipsticks()
        product_list.select_first_product()
        product_detail.add_product_to_cart()
        product_detail.go_to_cart()

    # Step 6
    cart.proceed_to_checkout()

    # Step 7
    checkout.fill_details()

    # Step 8
    checkout.place_order_click()

    # Step 9
    checkout.verify_payment_popup()
from Authentication.auth import User
from restaurant.restaurant import Restaurant

user = User.signin()
if user:
    Restaurant().run()
import random
from models import db, User, Gift, Giftlist
from app import application
from faker import Faker

fake = Faker()

with application.app_context():
    print("Deleting data................")
    User.query.delete()
    Gift.query.delete()
    Giftlist.query.delete()
    db.session.commit()

    # Create users and their lists of gifts
    print("Seeding users................")

    users = [
        {'name': "Johnny Deep", 'email': "johnyndeep3@gmail.com", 'password': "password12"},
        {'name': "Amber Heard", 'email': "amberheaard3@gmail.com", 'password': "password132"},
        {'name': "Adam Sandler", 'email': "adamsandie67@gmail.com", 'password': "password123"},
        {'name': "George Washington", 'email': "georgewashington@usa.gov", 'password': "password1234"}
    ]

    for data in users:
        user = User(**data)
        db.session.add(user)
    db.session.commit()

    print("Seeding gifts................")

    gift_name = ["Jewelry", "Spaday", "Giftcard", "Flowers", "Chocolate"]
    descriptions = ["Gold and Silver jewelry", "Have a day of relaxation at our new location",
                    "Redeemable for goods and services", "Ingrown Fresh bouquets", "From white to dark chocolate, bring your taste buds!"]

    sample_gifts = []
    for n in range(20):
        gift = Gift(name=random.choice(gift_name), description=random.choice(descriptions), price=random.randint(1000, 3000))
        sample_gifts.append(gift)
    db.session.add_all(sample_gifts)
    db.session.commit()

    print("Seeding gift lists................")

    giftlists = ["My Wish List", "Her Wish List", "Staycation", "Valentines"]
    giftls = []
    for n in range(20):
        users = User.query.all()
        random_user = random.choice(users)
        gift_list_obj = Giftlist(description=random.choice(giftlists), budget=random.randint(1000, 3000), user_id=random_user.id)
        giftls.append(gift_list_obj)

    db.session.add_all(giftls)
    db.session.commit()

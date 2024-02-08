from random import choice, randint
from models import db, User, Gift, Giftlist
from app import app
import faker

Faker= faker.Faker()

with app.app_context():
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
    
    gift_name= ["Jewelry", "Spaday", "Giftcard", "Flowers", "Chocolate"]
    descriptions= ["Gold and Silver jewelry", "Have a day of relaxation at our new location", "Redeemable for goods and services", "Ingrown Fresh bouquets", "From white to dark chocolate, bring your taste buds!"]
  
    sample_gifts= []
    for n in range(20):
        gift = Gift(name=choice(gift_name), description=choice(descriptions), price= randint(1000,3000))
        sample_gifts.append(gift)
    db.session.add_all(sample_gifts)
    db.session.commit()
    
    print("Seeding gift lists................")
    
    
    giftlists = ["My Wish List","Her Wish List","Staycation","Valentines"]      
    
    giftls= []
    for n in  range(20):
        users= User.query.all()
        random_user= choice(users)
        gift_list_obj = Giftlist(description=choice(giftlists),budget=randint(1000,3000), user_id=random_user.id)
        giftls.append(gift_list_obj)
        
    db.session.add_all(giftls)
    db.session.commit()
# gift_lists = [
#     {'description': 'Myish List', 'get': 12000.0, 'user_id': 1},
#     {'description': ' Wish List', 'budget': 8000.0, 'user_id': 2},
#     {'description': 'aycation', 'budget': 28000.0, 'user_id': 3},
#     {'description': 'Valentines', 'budget': 20000.0, 'user_id': 4}
# ]

# for gift_list in gift_lists:
#     gift_list_obj = Giftlist(
#         description=gift_list['description'],
#         budget=gift_list['budget'],
#         user=User.query.get(gift_list['user_id'])
#     )
#     db.session.add(gift_list_obj)
#     db.session.commit()
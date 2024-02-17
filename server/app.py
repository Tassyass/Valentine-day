#!/usr/bin/env python3

from flask import  Flask, make_response, request, jsonify, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound
import os


from dotenv import load_dotenv
load_dotenv()

from models import db,  User, Gift, Giftlist

application = Flask(
    __name__,
    static_url_path='',
    static_folder='../valentines-day-gift-planner/build',
    template_folder='../valentines-day-gift-planner/build'
    )
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI ', "postgresql://v_day_yr6g_user:5gTZwgHUoFqtWW1MU7mkT6v9UKauMIga@dpg-cn7h8ruct0pc738um2b0-a.oregon-postgres.render.com/v_day_yr6g")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
Migrate(application, db)

db.init_app(application)
api= Api(application)

@application.errorhandler(NotFound)
def handle_not_found(e):
    # response= make_response("NotFound: The requested resource not found", 404)
    return render_template('index.html', title= 'Homepage')

@application.route('/')
def home():
    return 'Think Valentine, Think us!'

class Users(Resource):
    def get(self):
        response_dict= [n.to_dict() for n in User.query.all()]
        response= make_response(response_dict, 200)
        return  response

api.add_resource(Users, '/users')
    
class  UserById(Resource):
    def  get(self, id):
        record=User.query.filter_by(id=id).first()
        if record is None:
            response= make_response(jsonify({'error': 'No such user id exists!'}),404)
            return response
        else:
             response_dict=record.to_dict()
             response = make_response (response_dict ,200)
             return response
         
   
    def delete(self,  id):
        record=User.query.filter_by(id=id).first()
        if record is None:
           response= make_response(jsonify({'error':'The user with the id does not exist'}) ,400)
           return response
        db.session.delete(record)
        db.session.commit()

api.add_resource(UserById, '/user/<int:id>') 
        
class Gifts(Resource):
    def get(self):
        response_dict=[n.to_dict() for n in Gift.query.all()]
        if response_dict is None:
            response=make_response("Gift not found", 404)
            return response
        else:
            response= make_response(jsonify(response_dict), 200)
            return response
        
    # @gifs.route('/create', methods=['POST'])
    def post(self):
     
       try:
           data = request.get_json()
           name=data.get('name')
           description = data.get('description')
           price= data.get('price')
           user_id = data.get('user_id')
           gift_id = data.get('gift_id')
           
           user = User.query.get(user_id)
           gift = Gift.query.get(gift_id)
           
           if not gift or user :
               return make_response(jsonify({"message": ["Gift or User does not exist"]}), 404)
           else:
               gift_new= Gift(name=name, description=description, price=price, user_id=user_id, gift_id=gift_id)
               db.session.add(gift_new)   
               db.session.commit()
               
               return make_response(jsonify(gift_new.to_dict()), 201)
          
       except Exception as e:
           error_dict = {"errors": ["validation errors", str(e)]}
           response = make_response(error_dict, 400)
           db.session.rollback()
           return response
             
api.add_resource(Gifts, '/gifts')

class GiftById(Resource):
    def get(self, id):
        record = Gift.query.filter_by(id=id).first()
        if record  is None:
            response = make_response(jsonify({"error":"This gift does not exist"}), 404)
            return response
        else:
            response_dict=record.to_dict()
            response = make_response (response_dict ,200)
            return response
        
    
    def delete(self,  id):
        record=Gift.query.filter_by(id=id).first()
        if record is None:
           response= make_response(jsonify({'error':'The gift with the id does not exist'}) ,400)
           return response
        db.session.delete(record)
        db.session.commit()

api.add_resource(GiftById, '/gift/<int:id>')     


class GiftLists(Resource):
    def post(self):
        try:
            data = request.get_json()
            description = data.get('description')
            budget = data.get('budget')
            user_id = data.get('user_id')
            # gift_id = data.get('gift_id')

            user = User.query.get(user_id)
            # gift = Gift.query.get(gift_id)

            if not user :
                return make_response(jsonify({"message": ["User does not exist"]}), 404)
            else:
                new_gift = Giftlist(description=description, budget=budget, user_id=user_id)
                db.session.add(new_gift)
                db.session.commit()

                return make_response(jsonify(new_gift.to_dict()), 201)

        except Exception as e:
            error_dict = {"errors": ["validation errors", str(e)]}
            response = make_response(error_dict, 400)
            db.session.rollback()
            return response

api.add_resource(GiftLists, '/gift_lists')
          
# # api.add_resource(Users, '/users')
# api.add_resource(Gifts, '/gifts')
# api.add_resource(UserById, '/user/<int:id>')
# api.add_resource(GiftLists, '/gift_lists')
            
if __name__ == '__main__':
    application.run(port=5555, debug=True)                 
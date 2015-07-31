from flask import make_response
from flask import jsonify
from flask import Blueprint
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date
client = MongoClient()
db = client.moviedb
movies = db.movies
order = Blueprint('order', __name__, template_folder = 'templates')



# needs to require authentication
# standard CRUD route, adds document to collection
@movie.route('', methods = ['POST'])
def add_new_movie():
  full_name = request.form.get('full_name')
  phone_number = request.form.get('phone_number')
  id_card_number = request.form.get('id_card_number')
  to_add = jsonify({
    'full_name': full_name,
    'phone_number': phone_number,
    'id_card_number': id_card_number,
    })
  movies.insert(to_add)

@movie.route('/calendar', methods = ['GET'])
def get_calendar():
  movies.find().sort({date: -1})
@movie.route('/homepage', methods = ['GET'] )
def get_homepage_movies():
  now = date.today()
  movies.find({
      date : {
        '$gte' : now - now.weekday,
        '$lte' : now + (14 - now.weekday),
    }
      }).sort({date: -1})

@movie.route(/<title>, methods = ["GET"])
def get_detail_page():
  movies.find({'title' : title})

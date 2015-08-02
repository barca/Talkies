from flask import make_response
from flask import jsonify
from flask import Blueprint
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date
client = MongoClient()
db = client.moviesdb
movies = db.movies
movie = Blueprint('movie', __name__, template_folder = 'templates')


# needs to require authentication
# standard CRUD route, adds document to collection
@movie.route('', methods = ['POST'])
def add_new_movie():
  title = request.form.get('title')
  runtime = request.form.get('runtime')
  big_pic = request.form.get('big_pic')
  trailer = request.form.get('trailer')
  poster = request.form.get('poster')
  director = request.form.get('director')
  cast1 = request.form.get('cast1')
  cast2 = request.form.get('cast2')
  date = request.form.get('date')
  desc = request.form.get('desc')
  to_add = {
    'title': title,
    'runtime': runtime,
    'big_pic': big_pic,
    'trailer': trailer,
    'poster': poster,
    'director': director,
    'cast1': cast1,
    'cast2': cast2,
    'date': date,
    'desc': desc,
    }
  movies.insert(to_add)
  # in future make response should render an example page

  return jsonify({'database': 'updated'})
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

@movie.route('/<title>', methods = ["GET"])
def get_detail_page():
  movies.find({'title' : title})

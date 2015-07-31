from flask import make_response
from flask import jsonify
from flask import Blueprint
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()
db = client.moviedb
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
  to_add = jsonify({
    'runtime': runtime,
    'big_pic': big_pic,
    'trailer': trailer,
    'poster': poster,
    'director': director,
    'cast1': cast1,
    'cast2': cast2,
    'date': date,
    'desc': desc,
    })
  movies.insert(to_add)

@movie.route('/all', methods = ['GET'])
def get_all_movies():
  movies.find()


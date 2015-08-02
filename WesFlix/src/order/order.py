from flask import make_response
from flask import jsonify
from flask import Blueprint
from flask import request
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, time
from twilio.rest import TwilioRestClient
from twilio.twiml import Response
import re

#ACCOUNT_SID = key
#AUTH_TOKEN = key
#ORIGIN = phone num
client = MongoClient()
db = client.menudb
menu_items = db.menu_items
order_history = db.order_history
order = Blueprint('order', __name__, template_folder = 'templates')

def send_text(destination,origin,message):
  try:
    TwilioClient = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    TwilioClient.messages.create(
        to = destination,
        from_= origin,
        body = message
        )
    return True
  except:
    return False


def write_message(name,id_card, movie):
  return "Thanks for using WesFlix! "+ name + "we hope you enjoy watching " + movie + "." + "ID CARD NUMBER: " + id_card

@smshook.route('', methods = ['GET'])
def index():
  dest = request.form.get('dest')
  origin = request.form.get('origin')
  name = request.form.get('name')
  id_card = request.form.get('id_card')
  movie = request.form.get('movie')
  msg = write_message(name, id_card, movie)
  send_text(dest, origin, msg)

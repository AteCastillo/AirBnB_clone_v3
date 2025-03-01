#!/usr/bin/python3
"""Index file"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    '''define status ok'''
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    '''returns number of objects for every class'''
    new_dict = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    for key, value in new_dict.items():
        new_dict[key] = storage.count(value)
    return jsonify(new_dict)

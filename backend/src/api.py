import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
#db_drop_and_create_all()

# ROUTES


@app.route('/drinks')
def get_drinks():
    try:
        all_drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.short() for drink in all_drinks]
        }), 200
    except:
        abort(422)





@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_details(jwt):
    try:
        all_drinks = Drink.query.all()
        return jsonify({
            'success': True,
            'drinks': [drink.long() for drink in all_drinks]
        }), 200
    except:
        abort(422)



@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drinks(jwt):
    body = request.get_json()

    drink_title = body['title']
    drink_recipe = json.dumps(body['recipe'])

    if drink_title is None or drink_recipe is None:
        abort(422)

    try:
        new_drink = Drink(title=drink_title, recipe=drink_recipe)
        new_drink.insert()
        
        return jsonify({
            'success': True,
            'drinks': [new_drink.long()]
        }), 200
    except:
        abort(500)



@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(jwt, id):
    body = request.get_json()

    drink = Drink.query.get(id)

    if drink is None:
        abort(404)
    
    try:
        if 'title' in body:
            drink.title = body['title']

        if 'recipe' in body:
            drink.recipe = body['recipe']

        drink.update()

        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        }), 200
    except:
        abort(500)
    




@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(jwt, id):
    
    drink = Drink.query.get(id)

    if drink is None:
        abort(404)
    try:
        drink.delete()

        return jsonify({
            'success': True,
            "delete": drink.id
        }), 200
    
    except:
        abort(500)


# Error Handling



@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422




@app.errorhandler(404)
def notFound(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "resource not found"
        }), 404


@app.errorhandler(400)
def badRequest(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "bad request"
        }), 400




@app.errorhandler(AuthError)
def authError(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code
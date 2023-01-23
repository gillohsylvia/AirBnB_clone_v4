#!/usr/bin/python3
"""
Creates a new view for State objects that handles all
default RESTFul API actions
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():

    """Retrieves the list of all"""
    states = storage.all(State)
    # return jsonify([state.to_dict() for state in states.values()])

    state_list = []
    for state in states.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state_object(state_id):
    """Retrieves a State object"""
    id_state = storage.get(State, state_id)
    if id_state is None:
        abort(404)

    return jsonify(id_state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    return jsonify({})


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_states():
    """Creates a State"""
    body = request.get_json()
    if body is None:
        abort(404, 'Not a JSON')

    if body['name'] is None:
        abort(404, 'Missing name')

    new_state = State(**body)
    new_state.save()
    return jsonify(new_state.to_dict())


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    new_state = storage.get(State, state_id)
    body = request.get_json()
    if new_state is None:
        abort(404)

    if body is None:
        abort(404, 'Not a JSON')
    c = 'created_at'
    u = 'updated_at'

    for key, value in body.items():
        if key != c and key != u and key != 'id':
            setattr(new_state, key, value)
        new_state.save()
        return jsonify(new_state.to_dict())

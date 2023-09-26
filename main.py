from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec
from app.app import *
from utils.logger import *

app = Flask(__name__)
api = FlaskPydanticSpec('flask')


@app.get("/ping")
def ping():
    return "pong", 200


@app.get("/get-data-name")
def get_data_name():
    name = request.args.get('name')
    response = get_name_info(name)
    if response is None:
        log.info(f"The name {name} you are looking for don't exist.")
        return f"The name {name} you are looking for don't exist.", 404
    return response, 200


@app.get("/get-names-by-condition")
def get_name_by_condition():
    letter = request.args.get('letter')
    pattern = request.args.get('pattern')
    response = find_name_by_condition(letter, pattern)
    if response is []:
        log.info(f"There's not name that match with the letter and/or pattern given.")
        return "There's not name that match with the letter and/or pattern given.", 404
    return response, 200


@app.get("/get-count-names-per-gender")
def get_count_names_per_gender():
    response = calculate_count_names_per_gender()
    if isinstance(response, dict):
        return response, 200
    else:
        log.error('An error ocurred trying to get the names per gender.')
        return 'An error ocurred trying to get the names per gender.', 500


@app.get("/get-top-10-names")
def get_top_10_used_names():
    response = get_more_used_names()
    if len(response) > 0:
        log.info('More used names are: ' + str(response))
        return response, 200
    else:
        log.info('We dont have enough info to provide you the 10 most used names.')
        return 'We dont have enough info to provide you the 10 most used names.', 500


@app.get("/is-an-approved-name")
def is_an_approved_name():
    name = request.args.get('name')
    response = is_approved_name(name)
    if isinstance(response, dict):
        log.info(f"Information on approved or non-approved names: " + str(response))
        return response, 200
    else:
        log.error(f"Error analyzing if the name {name} is approved.")
        return f"Error analyzing if the name {name} is approved.", 500


if __name__ == "__main__":
    api.register(app)
    app.run(host='0.0.0.0', port=3030)

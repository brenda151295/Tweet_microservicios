from flask import (
    Flask,
    request,
)
from werkzeug.exceptions import NotFound

from services import nice_json
from persistence.models import (
    User,
)


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "users": "/users",
            "user": "/users/<username>",
        }
    })


@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        raise NotImplementedError()
    else:
        return nice_json([x.to_json() for x in User.query.all()])


@app.route("/users/<username>", methods=['GET'])
def user_record(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        raise NotFound

    return nice_json(user.to_json())


if __name__ == "__main__":
    app.run(port=5000,host='0.0.0.0', debug=True)

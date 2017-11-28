from datetime import datetime

from flask import (
    Flask,
    request,
)
from werkzeug.exceptions import NotFound

from services import nice_json
from persistence.models import (
    db,
    Tweet,
    User,
)


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "tweets": "/tweets",
            "tweets_by_user": "/tweets/<username>"
        }
    })


@app.route("/tweets", methods=['GET', 'POST'])
def tweets():
    if request.method == 'POST':
        tweet = request.json
        print request
        username = tweet.get('username', '')

        user = User.query.filter_by(username=username).first()
        if user is None:
            raise NotFound("User '{}' not found.".format(username))

        content = tweet.get('content', '')
        if not content:
            raise NotFound("No content found.")

        tweet = Tweet(
            content=content, author=user, pub_date=datetime.utcnow()
        )
        db.session.add(tweet)
        db.session.commit()

        return nice_json(tweet.to_json())

    else:
        return nice_json([x.to_json() for x in Tweet.query.all()])


@app.route("/tweets/<username>", methods=['GET'])
def user_tweets(username):
    """
    Gets the user's tweets
    :param username:
    :return: List of User's tweets
    """
    user = User.query.filter_by(username=username).first()
    if user is None:
        raise NotFound("User '{}' not found.".format(username))

    return nice_json([x.to_json() for x in user.tweets.all()])


if __name__ == "__main__":
    app.run(port=5004,host='0.0.0.0', debug=True)

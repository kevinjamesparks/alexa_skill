import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from flask_sqlalchemy import SQLAlchemy
from utilities.api import get_current_temp


app = Flask(__name__)

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Warning exception handling
db = SQLAlchemy(app)

# flask-ask
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


# user model
class User(db.Model):
    """
    This class defines user logged in the app to know if it is their first
    time using this skill
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    amazonId = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.amazonId


def create_user(userId):
    """
    This function add a new user to the database
    :param userId: Amazon Id of the current user
    """
    new_user = User(amazonId=userId)
    db.session.add(new_user)
    db.session.commit()
    

@ask.launch
def start_skill():
    """
    This is the entry point of the skill. We welcome the user.
    :return: welcome string
    """

    # Get current logged in user amazon ID
    userId = session.user.userId

    # Get current temperature in berlin
    temp = get_current_temp()

    # Check if user exists
    query = User.query.filter_by(amazonId=userId).first()

    if query:
        return question(render_template('welcome', temp=temp))
    else:
        # Add new user to db
        create_user(userId)
        return question(render_template('welcome-new', temp=temp))


@ask.intent("YesIntent")
def next_round():
    """
    This function asks the user a random multiplication question of two random numbers
    :return: question string
    """
    number1 = randint(0,9)
    number2 = randint(0,4)
    round_msg = render_template('round', number1=number1, number2=number2)
    session.attributes['result'] = number1 * number2
    return question(round_msg)


@ask.intent("NoIntent")
def exit_skill():
    """
    This function quits the skill since the user responded that he/she was not ready
    :return: statement string
    """
    return statement(render_template('exit'))


@ask.intent("AnswerIntent", convert={'answer': int})
def answer(answer):
    """
    This functions validates if the user has the correct answer to the math questions.
    If the answer is correct, we announce the winning price.
    :param answer: Preferred travel type
    :return: Message to announce if user wins or loses
    """
    result = session.attributes['result']
    if answer == result:
        msg = render_template('win')
        return question(msg)
    else:
        msg = render_template('lose')
        return statement(msg)


@ask.intent("TripIntent")
def travel_answer(travel):
    """
    This function returns a trip booking confirmation with the user choice. Final point of skill.
    :param travel:
    :return: Message to announce choice of travel type
    """
    travel = travel
    return statement(render_template('trip', travel=travel))


if __name__ == '__main__':
    app.run(debug=True)

import random

from bottle import default_app, route, run, view, request, response

from models import Message


YES_LIST = [
  "yes",
  "affirmative",
  "amen",
  "fine",
  "good",
  "okay",
  "true",
  "yea",
  "all right",
  "aye",
  "beyond a doubt",
  "by all means",
  "certainly",
  "definitely",
  "even so",
  "exactly",
  "gladly",
  "good enough",
  "granted",
  "indubitably",
  "just so",
  "most assuredly",
  "naturally",
  "of course",
  "positively",
  "precisely",
  "sure thing",
  "surely",
  "undoubtedly",
  "unquestionably",
  "very well",
  "willingly",
  "without fail",
  "yep"
]

NO_LIST = [
  "no",
  "negative",
  "nix",
  "absolutely not",
  "by no means",
  "never",
  "no way",
  "not at all",
  "not by any means",
  "nix",
  "nay",
  "never",
  "not"
]

QUESTIONS = [
    'Are you ok?',
    'Do you like Python?',
    'Do you like Javascript?',
    'Have you heard about async\\await in Python?',
    'Are you aware about JS Promises?',
    'Do you use the lastest version of your browser?',
    'Was your day ok?',
    'Do you like pizza?'
]

CONFIRMATION_MSG = 'I didn\'t understand you. '\
                   'Do you still want to talk?'

START_TALK_MSG = 'Yey. Let\'s talk.\n'


@route('/')
@view('index')
def hello_world():
    return {}


def preprocess_msg(msg):
    return msg.lower().strip(' \r\n,.')


def get_msg_type(msg):
    if msg in YES_LIST:
        return 'yes'
    if msg in NO_LIST:
        return 'no'
    return 'unknown'


@route('/bot', method='POST')
def bot():
    was_confirmation = request.forms.get('confirmation', 'false') == 'true'
    message = request.forms.get('message', '')
    message = preprocess_msg(message)

    if message:
        msg_type = get_msg_type(message)
        finish = was_confirmation and msg_type == 'no'
        if msg_type == 'unknown':
            confimation = True
            res = CONFIRMATION_MSG
        else:
            confimation = False
            res = random.choice(QUESTIONS)
        if was_confirmation and msg_type == 'yes':
            res = START_TALK_MSG + res
        Message(message=message, response=res).save()
        return {'text': res,
                'confirmation': confimation,
                'finish': finish}
    response.status = 400
    return {'error': 'Bad message provided.'}


application = default_app()
run(application, threaded=True)
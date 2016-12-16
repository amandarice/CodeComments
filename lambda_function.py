from ask import alexa
import urllib2

def lambda_handler(request_obj, context={}):
    return alexa.route_request(request_obj)

@alexa.default_handler()
def default_handler(request):
    return launch_request_handler(request)

@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="Welcome to Code Comments! If you give me the name of a programming language, I will respond with instructions for making a comment in that language! In what language would you like to comment?",
                                 reprompt_message="Learning how to comment can be fun! What language would you like to comment out?")

@alexa.request_handler(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

@alexa.intent_handler("GetProgrammingLanguage")
def get_animal_sound_handler(request):

    language = request.get_slot_value("ProgrammingLanguage")
    comments = {}
    with open("comments.txt") as f:
        for line in f:
            newline = line.strip()
            key = newline[:newline.find(': ')]
            val = newline[newline.find(': ')+2:]
            comments[key]=val
    if language in comments:
        return alexa.create_response(message="For " + language + ", " + comments[language] + ".", end_session=True)
    else:
        return alexa.create_response(message="We don't know how to comment in that language. Please try again.", end_session=False)

@alexa.intent_handler("AMAZON.HelpIntent")
def help_intent_handler(request):
    return alexa.create_response(message="I will give you instructions on how to comment in a language you provide me.", end_session=False)

@alexa.intent_handler("AMAZON.StopIntent")
def stop_intent_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

@alexa.intent_handler("AMAZON.CancelIntent")
def cancel_intent_handler(request):
    return alexa.create_response(message="Goodbye!", end_session=True)

# CodeComments

CodeComments is an Alexa skill that provides an explanation of how to comment in a user-supplied programming language.

Sample Interaction:

* Your Question: "Alexa, ask Code Comments how do I comment in Python?"
* Alexa's Response: "Just use the hash character at the beginning of the comment for each line of code."

This skill is primarily intended for programmers needing a quick learning session or reminder on how to comment in a certain language. There are currently responses for 30 programming languages available.

### Project Format

The speech_assets folder contains the files which comprise the Voice User Interface:
* intent schema in intent_schema.json
* sample utterances in utterances.txt
* custom slot values in LIST_OF_LANGUAGES.txt, which contains a list of programming languages supported by this skill

The ask folder is based on the ask-alexa-pykit and is used to help develop an Alexa skill in Python.

The lambda function in lambda_function.py is used to run the Alexa skill using AWS Lambda.

### To Upload to Lambda

Right click all of the following, then compress:
* ask folder
* lambda_function.py
* comments.txt

Upload the compressed zip to Lambda.

### Testing

Text/JSON calls and responses - https://developer.amazon.com/edw/home.html

Vocal calls and responses - https://echosim.io/

**Written by Amanda Rice**

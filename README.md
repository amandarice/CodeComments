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

### To Create the Lambda Function

Most of the steps taken to create the Lambda function are found on this page:

https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function

Namely:
* Create or use your own AWS account.
* Log in to the AWS Management Console and navigate to AWS Lambda.
* Click the region drop-down in the upper-right corner of the console and select US East (N. Virginia).

  > Note: Lambda functions for Alexa skills can be hosted in either the US East (N. Virginia) or EU (Ireland) region. These are the only regions the Alexa Skills Kit supports as of 02/12/17.

* If you have no Lambda functions yet, click Get Started Now. Otherwise, click Create a Lambda Function.
* Select the Alexa Skills Kit blueprint called alexa-skills-kit-color-expert-python.

  > Tip: Type "alexa" in the Filter box to filter the list of blueprints.

* When prompted to configure triggers, click the box and select Alexa Skills Kit, then click Next.
* Enter a Name and Description for the function.
* Select the language you want to use for the Runtime (e.g. Python).

  >Note: You cannot change the language for a function once it is saved.

* Select the Role for the function. This defines the AWS resources the function can access.
  * To use an existing role, select the role under Use existing role.
  * To create a new role:
    * For Role (under Lambda function handler and role), select Create new role from template(s).
    * Enter the Role Name.
    * From the Policy templates list, select Simple Microservice permissions.
* On the Review page, make sure that the Triggers section includes Alexa Skills Kit.
* Click Create function to save your new function.

### To Upload to Lambda

One you have finished writing your code, right click all of the following, then compress:
* ask folder
* lambda_function.py
* comments.txt

Return to the AWS Management console, edit your Lambda function, select the Code tab, and upload this compressed zip file.

### Testing

Text/JSON calls and responses - https://developer.amazon.com/edw/home.html

Vocal calls and responses - https://echosim.io/

**Written by Amanda Rice**

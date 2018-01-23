import json
import uuid

from flask import Flask, request, jsonify, session, redirect

from helpers import get_greetings, get_permissions
from services.issue_services import create_issue, rename_issue, redescribe_issue, reprioritize_issue, redate_issue

app = Flask(__name__)

ESPRESSO_AUTH_URL = 'https://espressoemulator.herokuapp.com/o/login/google-oauth2'
GA_REDIRECT_ENDPOINT = 'https://oauth-redirect.googleusercontent.com/r/servicedesktest-4c7b8'
# ESPRESSO_GOOGLE_CLIENT_ID = 'ESPRESSO_GENERATED_VALUE'
GA_GOOGLE_CLIENT_ID = '106465978261-3it16mqdn461c7okp8ioftcebfan812m.apps.googleusercontent.com'
# implement oauth
# generate access token


@app.route('/')
def hello_world():
    return """
    <iframe
        width="350"
        height="430"
        src="https://console.dialogflow.com/api-client/demo/embedded/ffae5553-95ff-4ef5-b4e3-a7b6bcb5f0f5">
    </iframe>
    """


@app.route('/api')
def get_access_token():
    state = str(uuid.uuid4())

    espresso_auth_url = '{0}?client_id={1}&redirect_uri={2}&state={3}&response_type=token'.format(
        ESPRESSO_AUTH_URL, GA_GOOGLE_CLIENT_ID, GA_REDIRECT_ENDPOINT, state
    )

    return redirect(espresso_auth_url)

    # response = requests.post(espresso_auth_url)

    # generate access token for an espresso user
    # access_token = uuid.uuid4()

    # # this will be on espresso
    # return redirect('{0}#access_token={1}&token_type=bearer&state={2}'.format(
    #     ESPRESSO_REDIRECT_ENDPOINT, access_token, state
    # ))


    # response = requests.post(settings.TINKOFF_ENDPOINT + 'GetState', json={
    #     'TerminalKey': settings.TINKOFF_TERMINAL_KEY,
    #     'PaymentId': transaction_id,
    #     'Token': hash_value,
    # }


@app.route('/api/handle-google-assistant-request', methods=['GET', 'POST'])
def handle_google_assistant_request():
    body = request.json
    action = body['result']['action']

    if action == 'get_permissions':
        return jsonify(get_permissions())

    if action == 'greet_user':
        result = get_greetings(body.get('originalRequest', {}))
        return jsonify(result)

    if action == 'create_issue':
        return jsonify(create_issue(body['result']['contexts']))

    if action == 'rename_issue':
        return jsonify(rename_issue())

    if action == 'redescribe_issue':
        return jsonify(redescribe_issue())

    if action == 'reprioritize_issue':
        return jsonify(reprioritize_issue())

    if action == 'redate_issue':
        return jsonify(redate_issue())

    # return jsonify({
    #     'displayText': "Hello! This",
    #     'speech': "Hello! This is th",
    #     'data': {
    #         "google": {
    #             "conversationToken": "{\"state\":null,\"data\":{}}",
    #             "expectUserResponse": True,
    #             "expectedInputs": [
    #                 {
    #                     "inputPrompt": {
    #                         "initialPrompts": [
    #                             {
    #                                 "textToSpeech": "PLACEHOLDER_FOR_SIGN_IN"
    #                             }
    #                         ],
    #                         "noInputPrompts": []
    #                     },
    #                     "possibleIntents": [
    #                         {
    #                             "intent": "actions.intent.SIGN_IN",
    #                             "inputValueData": {}
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     }
    # })

if __name__ == '__main__':
    app.run()

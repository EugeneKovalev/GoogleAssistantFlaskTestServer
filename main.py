import uuid

import requests
from flask import Flask, request, jsonify, session, redirect

from helpers import rename_issue, prioritize_issue, get_greetings

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

    if action == 'greet_user':

        return jsonify({
            "intent": "actions.intent.SIGN_IN",
            "inputValueData": {}
        })


        # return jsonify({
        #     'displayText': "Hello! This is the Service Desk App! Do you agree to provide your device and profile data?",
        #     'speech': "Hello! This is the Service Desk App! Do you agree to provide your device and profile data?",
        #     'data':
        #         {
        #             "google": {
        #                 "expectUserResponse": True,
        #                 "isSsml": False,
        #                 "noInputPrompts": [],
        #                 "systemIntent": {
        #                     "intent": "actions.intent.PERMISSION",
        #                     "data": {
        #                         "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
        #                         "permissions": [
        #                             "NAME",
        #                             "DEVICE_COARSE_LOCATION",
        #                             "DEVICE_PRECISE_LOCATION"
        #                         ]
        #                     }
        #                 }
        #             }}
        # })



    elif action == 'greet_user_fallback':
        result = get_greetings(body.get('originalRequest', {}))
        return jsonify(result)

    elif action == 'rename_issue':
        result = rename_issue(body['result']['contexts'])
        return jsonify(result)

    elif action == 'prioritize_issue':
        result = prioritize_issue(body['result']['contexts'])
        return jsonify(result)


if __name__ == '__main__':
    app.run()


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/handle-google-assistant-request', methods=['GET', 'POST'])
def handle_google_assistant_request():
    if request.method == 'GET':
        return 'Hello, world!'
    else:
        body = request.json

        if body.get('originalRequest'):
            user_id = body['originalRequest']['data']['user']['userId']
            conversation_id = body['originalRequest']['data']['conversation']['conversationId']
        else:
            user_id = 0
            conversation_id = 0

        action = body['result']['action'] # BY THIS UNIQUE VAR WE CAN DEFINE WHAT SHOULD WE DO
        contexts = body['result']['contexts']  # contexts - they store data about raw user input and passed parameters

        print("""
        USER ID: {0} \n
        CONVERSATION ID: {1} \n
        ACTION: {2} \n
        CONTEXTS: {3} \n
        """.format(user_id, conversation_id, action, contexts))

        return jsonify({
            "speech": "Eugene Kovalev server speech", # text a user will hear
            "displayText": "Eugene Kovalev server text", # text a user will see
            "data": {}, # "data": {"facebook": {<facebook_message>}}
            "contextOut": contexts, # we can change it before sending to Google
            "source": "eugene's server"
        })


if __name__ == '__main__':
    app.run()


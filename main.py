from flask import Flask, request, jsonify, session

from helpers import rename_issue, prioritize_issue

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
    <iframe
        width="350"
        height="430"
        src="https://console.dialogflow.com/api-client/demo/embedded/ffae5553-95ff-4ef5-b4e3-a7b6bcb5f0f5">
    </iframe>
    """


@app.route('/api/handle-google-assistant-request', methods=['GET', 'POST'])
def handle_google_assistant_request():
    body = request.json
    action = body['result']['action']

    if action == 'greet_user':
        return jsonify({
            'data': {"google": {
                "expectUserResponse": True,
                "isSsml": False,
                "noInputPrompts": [],
                "systemIntent": {
                    "intent": "actions.intent.PERMISSION",
                    "data": {
                        "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
                        "optContext": "To pick you up",
                        "permissions": [
                            "NAME",
                            "DEVICE_PRECISE_LOCATION"
                        ]
                    }
                }
            }}
        })

    elif action == 'greet_user_fallback':
        print(1)
        return jsonify({
            'test': "Hello! This is Service Desk App! How can I help?",
            'speech': "Hello! This is Service Desk App! How can I help?"
        })

    elif action == 'rename_issue':
        result = rename_issue(body['result']['contexts'])
        return jsonify(result)

    elif action == 'prioritize_issue':
        result = prioritize_issue(body['result']['contexts'])
        return jsonify(result)


if __name__ == '__main__':
    app.run()


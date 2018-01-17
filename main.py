from flask import Flask, request, jsonify, session

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

    if action == 'rename_issue':
        if 'context-of-described-issue' in [_['name'] for _ in body['result']['contexts']]:
            response_text = "Excellent! Now, add the description, please!"
        else:
            response_text = "Good job! Now, set a priority status of the issue!"

        return jsonify({
            "speech": response_text,
            "displayText": response_text,
            "data": {},
            "source": "testserver"
        })

    elif action == 'prioritize_issue':
        root_context = [_ for _ in body['result']['contexts'] if _['name'] == 'context-of-named-issue'][0]

        response_text = "The name of the {0} issue is {1}. Described as {2}".format(
            body['result']['parameters']['issue_priority'],
            root_context['parameters']['issue_name'],
            root_context['parameters']['issue_description']
        )

        return jsonify({
            "speech": response_text,
            "displayText": response_text,
            "data": {},
            "contextOut": [
                {
                    "name": "context-of-no-issues",
                    "lifespan": 5
                },
                {
                    "name": "context-of-named-issue",
                    "lifespan": 0
                },
                {
                    "name": "context-of-described-issue",
                    "lifespan": 0
                }
            ],
            "source": "testserver"
        })


if __name__ == '__main__':
    app.run()


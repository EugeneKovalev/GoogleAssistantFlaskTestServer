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

    if action == 'prioritize_issue':
        root_context = [_ for _ in body['result']['contexts'] if _['name'] == 'context-of-named-issue'][0]

        name = root_context['parameters']['issue_name']
        description = root_context['parameters']['issue_description']
        priority = body['result']['parameters']['issue_priority']

        return jsonify({
            "speech": "The name of the {0} issue is {1}. Described as {2}".format(
                priority, name, description
            ),
            "displayText": "The name of the {0} issue is {1}. Described as {2}".format(
                priority, name, description
            ),
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


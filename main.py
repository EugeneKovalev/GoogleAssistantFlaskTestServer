from flask import Flask, request, jsonify, session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world"


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
            "contextOut": body['result']['contexts'],
            "source": "testserver"
        })


if __name__ == '__main__':
    app.run()


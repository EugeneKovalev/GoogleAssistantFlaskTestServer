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
        name = ''
        description = ''
        priority = body['result']['parameters']['issue_priority']
        for context in body['result']['contexts']:
            if context['name'] == 'context-of-named-issue':
                name = context['parameters']['issue_name']
            elif context['name'] == 'context-of-described-issue':
                description = context['parameters']['issue_description']

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

    # elif action == 'describe_issue':
    #     session['description'] = body['parameters']['any']
    #
    #     return jsonify({
    #         "speech": "The description of the issue is " + session['description'] + " Please, set the priority of an issue!",
    #         "displayText": "The description of the issue is " + session['description'],
    #         "data": {},
    #         "contextOut": body['result']['contexts'],
    #         "source": "testserver"
    #     })



    #
    # if request.method == 'GET':
    #     return 'Hello, world!'
    # else:
    #
    #
    #     if body.get('originalRequest'):
    #         user_id = body['originalRequest']['data']['user']['userId']
    #         conversation_id = body['originalRequest']['data']['conversation']['conversationId']
    #     else:
    #         user_id = 0
    #         conversation_id = 0
    #
    #      # BY THIS UNIQUE VAR WE CAN DEFINE WHAT SHOULD WE DO
    #     contexts = body['result']['contexts']  # contexts - they store data about raw user input and passed parameters
    #
    #     print("""
    #     USER ID: {0} \n
    #     CONVERSATION ID: {1} \n
    #     ACTION: {2} \n
    #     CONTEXTS: {3} \n
    #     """.format(user_id, conversation_id, action, contexts))
    #
    #     return jsonify({
    #         "speech": "Eugene Kovalev server speech", # text a user will hear
    #         "displayText": "Eugene Kovalev server text", # text a user will see
    #         "data": {}, # "data": {"facebook": {<facebook_message>}}
    #         "contextOut": contexts, # we can change it before sending to Google
    #         "source": "eugene's server"
    #     })


if __name__ == '__main__':
    app.run()


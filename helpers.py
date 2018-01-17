
def greet_user():
    pass


def rename_issue(contexts):
    if 'context-of-described-issue' in (_['name'] for _ in contexts):
        response_text = "Good job! Now, set a priority status of the issue!"
    else:
        response_text = "Excellent! Now, add the description, please!"

    return {
        "speech": response_text,
        "displayText": response_text,
        "data": {},
        "source": "testserver"
    }


def prioritize_issue(contexts):
    root_context = [_ for _ in contexts if _['name'] == 'context-of-named-issue'][0]

    response_text = "The name of the {0} issue is {1}. Described as {2}".format(
        root_context['parameters']['issue_priority'],
        root_context['parameters']['issue_name'],
        root_context['parameters']['issue_description']
    )

    return {
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
    }

import json


def get_permissions():
    return {
        'displayText': "Hello! This is the Service Desk App! Do you agree to provide your device and profile data?",
        'speech': "Hello! This is the Service Desk App! Do you agree to provide your device and profile data?",
        'data': {
            "google": {
                "expectUserResponse": True,
                "isSsml": False,
                "noInputPrompts": [],
                "systemIntent": {
                    "intent": "actions.intent.PERMISSION",
                    "data": {
                        "@type": "type.googleapis.com/google.actions.v2.PermissionValueSpec",
                        "permissions": [
                            "NAME",
                            "DEVICE_COARSE_LOCATION",
                            "DEVICE_PRECISE_LOCATION"
                        ]
                    }
                }
            }
        }
    }


def get_greetings(original_request):
    return {
        'displayText': 'qwert',
        'speech': 'qwertyt'
    }
    if original_request.get('data', {}).get('user', {}).get('profile'):
        response_text = 'Yay! Welcome, sir!'
        return {
            'displayText': response_text,
            'speech': response_text
        }
    else:
        response_text = 'You denied to provide access to your data. Terminating processes. Good bye.'

        return {
            'displayText': response_text,
            'speech': response_text,
            "data": {
                "google": {
                    "expect_user_response": False,
                    "is_ssml": False,
                    "no_input_prompts": []
                }
            }
        }


def rename_issue(contexts):
    issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]

    if issue_context['parameters'].get('issue_priority'):
        response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
            issue_context['parameters']['issue_priority'],
            issue_context['parameters']['issue_name'],
            issue_context['parameters']['issue_description']
        )
    elif issue_context['parameters'].get('issue_description'):
        response_text = 'Good job! Now, set a priority status of the issue!'
    else:
        response_text = 'Excellent! Now, add the description, please!'

    return {
        "speech": response_text,
        "displayText": response_text,
        "data": {},
        "source": "testserver"
    }


def redescribe_issue(contexts):
    issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]

    if issue_context['parameters'].get('issue_priority'):
        response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
            issue_context['parameters']['issue_priority'],
            issue_context['parameters']['issue_name'],
            issue_context['parameters']['issue_description']
        )
    else:
        response_text = 'Good job! Now, set a priority status of the issue!'

    return {
        "speech": response_text,
        "displayText": response_text,
        "data": {},
        "source": "testserver"
    }


def prioritize_issue(contexts):
    issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]

    response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
        issue_context['parameters']['issue_priority'],
        issue_context['parameters']['issue_name'],
        issue_context['parameters']['issue_description']
    )

    return {
        "speech": response_text,
        "displayText": response_text,
        "data": {},
        # "contextOut": [
        #     {
        #         "name": "context-of-no-issues",
        #         "lifespan": 5
        #     },
        #     {
        #         "name": "context-of-named-issue",
        #         "lifespan": 0
        #     },
        #     {
        #         "name": "context-of-described-issue",
        #         "lifespan": 0
        #     }
        # ],
        "source": "testserver"
    }


def send_issue(contexts):
    return {
        "speech": 'Your issue has been sent! Have a nice day!',
        "displayText": 'Your issue has been sent! Have a nice day!',
        "data": {
            "google": {
                "expect_user_response": False,
                "is_ssml": False,
                "no_input_prompts": []
            }
        },
        # "contextOut": [
        #     {
        #         "name": "context-of-no-issues",
        #         "lifespan": 5
        #     },
        #     {
        #         "name": "context-of-named-issue",
        #         "lifespan": 0
        #     },
        #     {
        #         "name": "context-of-described-issue",
        #         "lifespan": 0
        #     }
        # ],
        "source": "testserver"
    }

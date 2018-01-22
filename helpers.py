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
    if original_request.get('data', {}).get('user', {}).get('profile'):
        response_text = 'Yay! Welcome, sir! How can I help you?'
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





# def redescribe_issue(contexts):
#     issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]
#
#     if issue_context['parameters'].get('issue_priority'):
#         response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
#             issue_context['parameters']['issue_priority'],
#             issue_context['parameters']['issue_name'],
#             issue_context['parameters']['issue_description']
#         )
#     else:
#         response_text = 'Good job! Now, set a priority status of the issue!'
#
#     return {
#         "speech": response_text,
#         "displayText": response_text,
#         "data": {},
#         "source": "testserver"
#     }
#
#
# def prioritize_issue(contexts):
#     issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]
#
#     response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
#         issue_context['parameters']['issue_priority'],
#         issue_context['parameters']['issue_name'],
#         issue_context['parameters']['issue_description']
#     )
#
#     return {
#         "speech": response_text,
#         "displayText": response_text,
#         "data": {},
#         "source": "testserver"
#     }
#
#
# def send_issue(contexts):
#     return {
#         "speech": 'Your issue has been sent! Have a nice day!',
#         "displayText": 'Your issue has been sent! Have a nice day!',
#         "data": {
#             "google": {
#                 "expect_user_response": False,
#                 "is_ssml": False,
#                 "no_input_prompts": []
#             }
#         },
#         "source": "testserver"
#     }

#
# def create_stepless_issue(contexts):
#     issue_context = [_ for _ in contexts if _['name'] == 'context-of-stepless-issue'][0]
#
#     # required params name and priority
#
#     # required name
#
#     if not issue_context['parameters'].get('issue_priority'):
#         response_text = "Set an issue priority! Available options are blocker, critical, major, minor or trivial"
#         contexts = [
#             {
#                 "name": "context-of-wait-for-priority-stepless-issue",
#                 "lifespan": 1
#             }
#         ]
#
#     elif not issue_context['parameters'].get('issue_description'):
#         response_text = "Would you like to add a description?"
#         contexts = [
#             {
#                 "name": "context-of-wait-for-description-stepless-issue",
#                 "lifespan": 1
#             }
#         ]
#
#     else:
#         response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
#             issue_context['parameters']['issue_priority'],
#             issue_context['parameters']['issue_name'],
#             issue_context['parameters']['issue_description']
#         )
#         contexts = []
#
#     return {
#             "speech": response_text,
#             "displayText": response_text,
#             "data": {},
#             "contextOut": contexts,
#             "source": "testserver"
#         }
#
#
# def add_priority_stepless_issue(contexts):
#     issue_context = [_ for _ in contexts if _['name'] == 'context-of-stepless-issue'][0]
#
#     response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
#         issue_context['parameters']['issue_priority'],
#         issue_context['parameters']['issue_name'],
#         issue_context['parameters']['issue_description']
#     )
#
#     return {
#         "speech": response_text,
#         "displayText": response_text,
#         "data": {},
#         "source": "testserver"
#     }
#
#
# def accept_description_adding_for_stepless_issue(contexts):
#     return {
#         "speech": 'Then tell me a description, please!',
#         "displayText": 'Then tell me a description, please!',
#         "data": {},
#         "contextOut": [
#             {
#                 "name": "context-of-add-description-stepless-issue",
#                 "lifespan": 1
#             }
#         ],
#         "source": "testserver"
#     }
#
#
# def add_description_for_stepless_issue(contexts):
#     issue_context = [_ for _ in contexts if _['name'] == 'context-of-stepless-issue'][0]
#
#     response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
#         issue_context['parameters']['issue_priority'],
#         issue_context['parameters']['issue_name'],
#         issue_context['parameters']['issue_description']
#     )
#
#     return {
#         "speech": response_text,
#         "displayText": response_text,
#         "data": {},
#         "source": "testserver"
#     }
#
#
# def deny_description_adding_for_stepless_issue(contexts):
#     issue_context = [_ for _ in contexts if _['name'] == 'context-of-stepless-issue'][0]
#
#     response_text = "The name of the {0} issue is {1}. Do you want to send it?".format(
#         issue_context['parameters']['issue_priority'],
#         issue_context['parameters']['issue_name']
#     )
#
#     return {
#         "speech": response_text,
#         "displayText": response_text,
#         "data": {},
#         "source": "testserver"
#     }
#
#



def _invoke_name_setting():
    return {
        "speech": "Name your issue, please!",
        "displayText": "Name your issue, please!",
        "data": {},
        "contextOut": [
            {
                "name": "issue-naming",
                "lifespan": 1
            }
        ],
        "source": "testserver"
    }


def _invoke_description_setting():
    return {
        "speech": "Describe your issue, please!",
        "displayText": "Describe your issue, please!",
        "data": {},
        "contextOut": [
            {
                "name": "issue-describing",
                "lifespan": 1
            }
        ],
        "source": "testserver"
    }


def _invoke_priority_setting():
    return {
        "speech": "Set a priority of the issue, please!",
        "displayText": "Set a priority of the issue, please!",
        "data": {},
        "contextOut": [
            {
                "name": "issue-prioritizing",
                "lifespan": 1
            }
        ],
        "source": "testserver"
    }


def create_issue(contexts):
    issue_context = [_ for _ in contexts if _['name'] == 'context-of-stepless-issue'][0]

    if not issue_context['parameters'].get('issue_name'):
        return _invoke_name_setting()

    if not issue_context['parameters'].get('issue_description'):
        return _invoke_description_setting()

    if not issue_context['parameters'].get('issue_priority'):
        return _invoke_priority_setting()



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


def _invoke_name_setting():
    return {
        "speech": "Name your issue, please!",
        "displayText": "Name your issue, please!",
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
        "contextOut": [
            {
                "name": "issue-prioritizing",
                "lifespan": 1
            }
        ],
        "source": "testserver"
    }


def _invoke_dating_setting():
    # return {
    #     "speech": "When do you want it to be done?",
    #     "displayText": "When do you want it to be done?",
    #     "contextOut": [
    #         {
    #             "name": "issue-dating",
    #             "lifespan": 1
    #         }
    #     ],
    #     "source": "testserver"
    # }
    return {
        # 'displayText': "Hello! profile data?",
        'speech': "PLACEHOLDER_FOR_DATETIME",
        'data': {
            "google": {
                "expectUserResponse": True,
                "isSsml": False,
                "noInputPrompts": [],
                "systemIntent": {
                    "intent": "actions.intent.DATETIME",
                    "data": {
                        "@type": "type.googleapis.com/google.actions.v2.DateTimeValueSpec",
                        # "dialogSpec": {
                        #     "requestDatetimeText": "When do you want it to be done?",
                        #     "requestDateText": "What is the best date to resolve the issue?",
                        #     "requestTimeText": "What time of day works best for you?"
                        # }
                    }
                }
            }
        }
    }







        # {
        #
        #         "expectUserResponse": True,
        #         "expectedInputs": [
        #             {
        #                 "inputPrompt": {
        #                     "initialPrompts": [
        #                         {
        #                             "textToSpeech": "PLACEHOLDER_FOR_DATETIME"
        #                         }
        #                     ],
        #                     "noInputPrompts": []
        #                 },
        #                 "possibleIntents": [
        #                     {
        #                         "intent": "actions.intent.DATETIME",
        #                         "inputValueData": {
        #                             "@type": "type.googleapis.com/google.actions.v2.DateTimeValueSpec",
        #                             "dialogSpec": {
        #                                 "requestDatetimeText": "When do you want to come in?",
        #                                 "requestDateText": "What is the best date to schedule your appointment?",
        #                                 "requestTimeText": "What time of day works best for you?"
        #                             }
        #                         }
        #                     }
        #                 ]
        #             }
        #         ]
        #     }



def create_issue(contexts):
    issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]

    if not issue_context['parameters'].get('issue_name'):
        return _invoke_name_setting()

    elif not issue_context['parameters'].get('issue_description'):
        return _invoke_description_setting()

    elif not issue_context['parameters'].get('issue_priority'):
        return _invoke_priority_setting()

    elif not issue_context['parameters'].get('issue_expiration_date'):
        return _invoke_dating_setting()

    else:
        response_text = """
        The name of the {0} issue is {1}. 
        Described as {2}. 
        Expiration date set to {3}
        Do you want to send it?""".format(
            issue_context['parameters']['issue_priority'],
            issue_context['parameters']['issue_name'],
            issue_context['parameters']['issue_description'],
            issue_context['parameters']['issue_expiration_date']
        )

        return {
            "speech": response_text,
            "displayText": response_text,
            "contextOut": [
                {
                    "name": "issue-sending",
                    "lifespan": 1
                }
            ],
            "source": "testserver"
        }


def rename_issue():
    result = _invoke_name_setting()

    result['contextOut'].extend([
        {"name": "issue-describing", "lifespan": 0},
        {"name": "issue-prioritizing", "lifespan": 0},
        {"name": "issue-dating", "lifespan": 0},
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result


def redescribe_issue():
    result = _invoke_description_setting()

    result['contextOut'].extend([
        {"name": "issue-naming", "lifespan": 0},
        {"name": "issue-prioritizing", "lifespan": 0},
        {"name": "issue-dating", "lifespan": 0},
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result


def reprioritize_issue():
    result = _invoke_priority_setting()

    result['contextOut'].extend([
        {"name": "issue-naming", "lifespan": 0},
        {"name": "issue-describing", "lifespan": 0},
        {"name": "issue-dating", "lifespan": 0},
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result


def redate_issue():
    result = _invoke_dating_setting()

    result['contextOut'].extend([
        {"name": "issue-naming", "lifespan": 0},
        {"name": "issue-describing", "lifespan": 0},
        {"name": "issue-prioritizing", "lifespan": 0},
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result

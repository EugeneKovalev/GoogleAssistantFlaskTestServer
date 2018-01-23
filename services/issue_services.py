

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
    return {
        "speech": "When do you want it to be done?",
        "displayText": "When do you want it to be done?",
        "contextOut": [
            {
                "name": "issue-dating",
                "lifespan": 1
            }
        ],
        "source": "testserver"
    }


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

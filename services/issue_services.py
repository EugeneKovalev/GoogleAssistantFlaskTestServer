

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


def create_issue(contexts):
    issue_context = [_ for _ in contexts if _['name'] == 'context-of-issue'][0]

    if not issue_context['parameters'].get('issue_name'):
        return _invoke_name_setting()

    if not issue_context['parameters'].get('issue_description'):
        return _invoke_description_setting()

    if not issue_context['parameters'].get('issue_priority'):
        return _invoke_priority_setting()

    else:
        response_text = "The name of the {0} issue is {1}. Described as {2}. Do you want to send it?".format(
            issue_context['parameters']['issue_priority'],
            issue_context['parameters']['issue_name'],
            issue_context['parameters']['issue_description']
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
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result


def redescribe_issue():
    result = _invoke_description_setting()

    result['contextOut'].extend([
        {"name": "issue-naming", "lifespan": 0},
        {"name": "issue-prioritizing", "lifespan": 0},
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result


def reprioritize_issue():
    result = _invoke_description_setting()

    result['contextOut'].extend([
        {"name": "issue-naming", "lifespan": 0},
        {"name": "issue-describing", "lifespan": 0},
        {"name": "issue-sending", "lifespan": 0}
    ])

    return result

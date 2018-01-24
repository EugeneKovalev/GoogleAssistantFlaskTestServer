

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

    elif not issue_context['parameters'].get('issue_date') \
            and not issue_context['parameters'].get('issue_time')\
            and not issue_context['parameters'].get('issue_date_period') \
            and not issue_context['parameters'].get('issue_date'):
        return _invoke_dating_setting()

    else:
        text_components = [
            'The name of the {0} issue is {1}.'.format(
                issue_context['parameters']['issue_priority'],
                issue_context['parameters']['issue_name']
            )
        ]

        if issue_context['parameters'].get('issue_description'):
            text_components.append('Described as {0}'.format(
                issue_context['parameters']['issue_description']
            ))

        if issue_context['parameters'].get('issue_date'):
            text_components.append('Execution date is {0}'.format(
                issue_context['parameters']['issue_date']
            ))
        elif issue_context['parameters'].get('issue_date_period'):
            text_components.append('Execution date period is {0}'.format(
                issue_context['parameters']['issue_date_period']
            ))

        if issue_context['parameters'].get('issue_time'):
            text_components.append('Execution time is {0}'.format(
                issue_context['parameters']['issue_date']
            ))
        elif issue_context['parameters'].get('issue_time_period'):
            text_components.append('Execution time period is {0}'.format(
                issue_context['parameters']['issue_date_period']
            ))

        response_text = '\n'.join(text_components)

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

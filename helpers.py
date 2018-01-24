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
    # return {
    #     'displayText': 'Permissions check has temporarily been disabled. How can I help you?',
    #     'speech': 'Permissions check has temporarily been disabled. How can I help you?'
    # }
    if original_request.get('data', {}).get('user', {}).get('profile'):
        print(original_request.get('data', {}).get('user', {}).get('profile'))
        response_text = 'Yay! Welcome, sir! How can I help you?'
        return {
            'displayText': response_text,
            'speech': response_text
        }
    else:
        print(original_request.get('data', {}).get('user', {}).get('profile'))
        response_text = 'Yay! Welcome, Dialogflow user! How can I help you?'
        return {
            'displayText': response_text,
            'speech': response_text
        }
        
        # response_text = 'You denied to provide access to your data. Terminating processes. Good bye.'
        #
        # return {
        #     'displayText': response_text,
        #     'speech': response_text,
        #     "data": {
        #         "google": {
        #             "expect_user_response": False,
        #             "is_ssml": False,
        #             "no_input_prompts": []
        #         }
        #     }
        # }

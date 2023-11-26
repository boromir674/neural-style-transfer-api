"""A Lambda App (AWS Lambda) that delegates http requests to NST App."""
import sys
import json


def handler(event, context):

    search_path = sys.path

    return json.dumps({
        'msg': 'Hello from AWS Lambda using Python ' + sys.version + ' !',
        # 'search_path': '[' + '\n'.join(search_path) + ']',
        'search_path': '[' + ', '.join([f'{x}' for x in search_path]) + ']',
        'event': dict(event),
        'event_type': str(type(event)),
        'context_type': str(type(context)),
    }, sort_keys=True, indent=4)

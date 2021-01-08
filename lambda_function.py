import json
import os

from urllib.request import Request

SLACK_HOOK_URL = os.getenv('SLACK_HOOK_URL')

def lambda_handler(event, context):
    record = event.get('Records')[0]
    sns_data = record.get('Sns')
    if not sns_data:
      return

    sns_message = sns_data.get('Message')
    if not sns_message:
        return
    
    sns_message = json.loads(sns_message)

    old_state_value = sns_message.get('OldStateValue')
    new_state_value = sns_message.get('NewStateValue')
    target_lambda_function = sns_message.get('Trigger').get('Dimensions')[0].get('value')
    
    slack_message = {
        'text': f'람다 함수 {target_lambda_function} 상태 변경: {old_state} -> {new_state}'
    }
    
    req = Request(SLACK_HOOK_URL, json.dumps(slack_message).encode('utf-8'))

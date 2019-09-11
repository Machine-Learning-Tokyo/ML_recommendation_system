import json
from botocore.vendored import requests
from botocore.vendored.requests.auth import HTTPBasicAuth
import helper as hp

def lambda_handler(event, context):
    try:
        param_names = ['query', 'init_idx', 'count']
        response_msg = hp.response('success', 200)
        
        if hp.is_valid_parameters(event, param_names):
            params = hp.parse_parameters(event)
            if params.values():
                auth_info = {
                    'user': 'xxxx',
                    'password': 'xxxx'
                }
                url = f"https://paperswithcode.com/api/v0/search/?q={params['query']}"
                query_result = requests.get(
                    url, 
                    auth=HTTPBasicAuth(auth_info['user'], auth_info['password'])
                    )
                    
                if query_result.status_code == 200:
                    content = json.loads(query_result.content)
                    content = content[params['init_idx']:params['init_idx'] + params['count']]
                    response_msg = hp.response(content, query_result.status_code)
                    return response_msg
                
        response_msg = hp.response('Invalid parameters.', 400)
        return response_msg
    except Exception as ex:
        response_msg = hp.response(str(ex), 500)
        return response_msg
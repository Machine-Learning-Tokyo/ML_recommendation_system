import json
import scholarly
import helper as hp

def lambda_handler(event, context):
    try:
        param_names = ['query', 'init_idx', 'count']
        response_msg = hp.response('success', 200)
        
        if hp.is_valid_parameters(event, param_names):
            params = hp.parse_parameters(event)
            if params.values():
                result = []
                iters = scholarly.search_pubs_query(params['query'])
                for _ in range(params['init_idx'] + params['count']):
                    result.append(next(iters).__dict__)
                result = result[params['init_idx']:]
                response_msg = hp.response(result, 200)
                return response_msg
                
        response_msg = hp.response('Invalid parameters.', 400)
        return response_msg
    except Exception as ex:
        response_msg = hp.response(str(ex), 500)
        return response_msg
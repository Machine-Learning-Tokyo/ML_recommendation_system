def is_valid_parameters(event, param_names):
    """
    Check whether the item in param_names exist in event dictionary.
    
    :param  event:          Lambda event object.
    :param  param_names:    The list of the param names to be checked.
    
    :retrun:                True if exist else False
    """
    for param in param_names:
        if not param in event:
            return False
    return True

def response(message, status_code):
    """
    Response message for the request.
    
    :param message:     The response message.
    :param status_code: The response status.
    
    :return:            The dic('statusCode', 'body')
    """
    return {
        'statusCode': status_code,
        'body': message
    }

def parse_parameters(event):
    """
    Parse the parameters from event dictionary.
    
    :param  event:      The event dictionary.
    :return:            dict('query', 'init_idx', 'count')
    """
    try:
        param = dict()
        param['query'] = event['query']
        param['init_idx'] = int(event['init_idx'])
        param['count'] = int(event['count'])
        param['source'] = event['source']
        
        if param['init_idx'] >= 0 and param['count'] > 0:
            return param
        else:
            return dict()
            
    except:
        return dict()
import json
from botocore.vendored import requests

def lambda_handler(event, context):
    query = event['query']
    query+='+language:python'
    params = (
        ('q', query),
        ('sort', 'stars'),
        ('order', 'desc'),
    )
    
    response = requests.get('https://api.github.com/search/repositories', params=params)
    
    return response.json()
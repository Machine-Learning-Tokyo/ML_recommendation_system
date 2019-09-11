# Input Test

```
{
  "category": "code",
  "query": "tensorflow",
  "page": 0
}
```

At the test_lambda_script, only `query` is taken into account 

<hr>
## APIs for ML Search

1. For Paper With Code
```
 curl --header 'x-api-key:YOURAPIKEY' \
  -H "Content-Type: application/json" -X POST \
   -d '{
  "query": "LSTM",
  "init_idx": 0,
  "count": 30
}' \
   https://hjmlipdub8.execute-api.us-east-2.amazonaws.com/development/paperwithcode
```

2. For Scholarly

```
 curl --header 'x-api-key:YOURAPIKEY' \
  -H "Content-Type: application/json" -X POST \
   -d '{
  "query": "LSTM",
  "init_idx": 0,
  "count": 30
}' \
   https://hjmlipdub8.execute-api.us-east-2.amazonaws.com/development/scholarly
```
Expected Headers:
- x-api-key - The API authentication key for accessing the APIs.
- Content-Type - applicatin/json is expected.

Expected Body:
- query - The key word for searching.
- init_idx - The initial result index. Use for pagination.
- count - Total number of query result to be fetched. 

<i><span style="color:blue">Note: For Scholarly, due to the performance issue, only 30 max request could be done per single keyword.</span></i>
import json
import requests

headers = {
  'Accept': 'application/json',
  'X-Api-Key': '7ZwpX3iQww9NtZsdVLcH2ZeuroV33c9LakOhABC1jHc'
}

r = requests.get('https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent', params={

}, headers = headers)

json_response = r.json()

if r.status_code != 200:
    print('API Error:', r.status_code)
    print(json.dumps(json_response, indent=4))
    if raiseError:
        raise APIError(r)

print(json.dumps(json_response, indent=4))

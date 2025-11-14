from infrahub_sdk.transforms import InfrahubTransform
import json
import requests
import time
class Transform(InfrahubTransform):
    query = "switch_check_query"
    async def transform(self, data):
        device = data["AvdLeafswitch"]["edges"][0]["node"]
        device_name = device["name"]["value"]
        device_primary_address = device["primary_address"]["node"]["address"]["value"].split("/")[0]

        s = requests.Session()
        kriten_url = "http://kriten-dev.192.168.10.190.nip.io/api/v1/jobs/"
        kriten_launch_url = kriten_url + "infrahubanta"

        payload = json.dumps({
        "name": device_name,
        "primary_address": device_primary_address
        })
        headers = {
        'Content-Type': 'application/json',
        'Token': 'kri_Rnx8Pvr2jBalEjvfwA4nIHUhI8lIUGHIK5zH'
        }
        url = kriten_launch_url
        response = s.post(url, headers=headers, data=payload)

        job_id = response.json()['id']
        url = kriten_url + job_id
        print("job_id:", job_id)
        completed = 0
        while completed == 0:
            time.sleep(5)
            response = s.get(url, headers=headers)
            result = response.json()
            completed = result['completed']
            print("completed:", completed)
        print(response.json()['json_data'])
        return response.json()['json_data']
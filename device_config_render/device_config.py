from infrahub_sdk.transforms import InfrahubTransform
import json
import requests
import time
class DeviceConfigTransform(InfrahubTransform):
    query = "device_config_query"
    async def transform(self, data):
        device = data["KubeDevice"]["edges"][0]["node"]
        device_name = device["name"]["value"]
        device_description = device["description"]["value"]


        s = requests.Session()
        kriten_url = "http://kriten-dev.192.168.10.190.nip.io/api/v1/jobs/"
        kriten_launch_url = kriten_url + "hello-kriten"

        payload = json.dumps({
        "target_hosts": "arista"
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
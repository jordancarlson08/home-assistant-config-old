import json
import requests
import time


class Codes:
    def send_command(body):
        url = "http://192.168.0.102/5c-cf-7f-13-c3-5f/api/ir/write"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        response = requests.request("PUT", url, headers=headers, data=json.dumps(body))
        print(response.text)
        time.sleep(0.5)

    roku_home = {
        "period": 862316,
        "n": 68,
        "seq": [343, 171, 21, 22, 21, 65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 22, 21, 65, 21, 65, 21, 65, 21, 65, 21,
                65, 21, 22, 21, 65, 21, 65, 21, 65, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22,
                21, 65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 1672],
        "repeat": [1, 0, 68]
    }

    roku_right = {
        "frequency": 38000,
        "n": 68,
        "seq": [343, 171, 21, 22, 21, 65, 21, 22, 21, 65, 21, 22, 21, 65, 21, 65, 21, 65, 21, 22, 21, 65, 21, 22, 21,
                22, 21, 22, 21, 22, 21, 65, 21, 65, 21, 65, 21, 22, 21, 65, 21, 65, 21, 22, 21, 65, 21, 22, 21, 22, 21,
                22, 21, 65, 21, 22, 21, 22, 21, 65, 21, 22, 21, 65, 21, 65, 21, 1672],
        "repeat": [1, 0, 68]
    }

    roku_ok = {
        "frequency": 38000,
        "n": 68,
        "seq": [343, 171, 21, 22, 21, 65, 21, 22, 21, 65, 21, 22, 21, 65, 21, 65, 21, 65, 21, 22, 21, 65, 21, 22, 21,
                22, 21, 22, 21, 22, 21, 65, 21, 65, 21, 22, 21, 65, 21, 22, 21, 65, 21, 22, 21, 65, 21, 22, 21, 22, 21,
                65, 21, 22, 21, 65, 21, 22, 21, 65, 21, 22, 21, 65, 21, 65, 21, 1672],
        "repeat": [1, 0, 68]
    }

    tv_power = {
        "frequency": 40000,
        "n": 26,
        "seq": [96, 24, 48, 24, 24, 24, 48, 24, 24, 24, 48, 24, 24, 24, 24, 24, 48, 24, 24, 24, 24, 24, 24, 24, 24,
                1032],
        "repeat": [1, 0, 26]
    }

    sound_power = {
        "frequency": 38000,
        "n": 72,
        "seq": [343, 171, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 65, 21, 65, 21, 65, 21,
                65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 22, 21, 65, 21, 22, 21,
                65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 65, 21, 22, 21, 65, 21, 1672, 343, 86, 21, 3730],
        "repeat": [1, 68, 72]
    }


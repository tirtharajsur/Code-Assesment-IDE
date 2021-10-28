import http.client
import json


def submitRequest(langId, code, inputText):
    conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")

    payload = {
        "language_id": langId,
        "source_code": code,
        "stdin": inputText
    }

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "judge0-ce.p.rapidapi.com",
        'x-rapidapi-key': "55253743e0mshf29b9e0a5ba97eep1c5211jsndfa9c2572a09"
    }

    conn.request("POST", "/submissions?wait=true&fields=stderr,stdout,compile_output",
                 json.dumps(payload), headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    return json.loads(data.decode("utf-8"))

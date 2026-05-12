import json

def parse_json_response(response):

    try:
        return json.loads(response)

    except Exception:
        return {"route": "retriever"}
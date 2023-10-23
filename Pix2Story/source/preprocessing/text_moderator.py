import http.client, urllib.request, urllib.parse, urllib.error, base64, json

def text_moderator(text):

    headers = {
        # Request headers
        'Content-Type': 'text/plain',
        'Ocp-Apim-Subscription-Key': 'subscription_key',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'autocorrect': True,
        'PII': False,
        'classify': 'True'
    })

    try:
        conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
        conn.request(
            "POST",
            f"/contentmoderator/moderate/v1.0/ProcessText/Screen?{params}",
            text,
            headers,
        )
        response = conn.getresponse()
        data = response.read()
        conn.close()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    d = data.decode('utf-8')
    data = json.loads(d)
    return (
        data['Classification']['ReviewRecommended']
        if 'Classification' in data
        else False
    )
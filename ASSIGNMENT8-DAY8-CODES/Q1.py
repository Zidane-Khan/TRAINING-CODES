# subject filler

import requests


token = f"ya29.a0AeXRPp5YMZIanOcbxFgHmcHlBPi24Dz8XoRBg_B94urVPPErAc-38cx9oAAJIyA7hc3bdu8-6aBcX8Z7aGY-DmUjBtxAwPX_V6qXU7FzODgWjBullgif6p-FAZDJywV9rMh2btkmTT5YrZEz52x0IokUhyW9vLHIsg6ycML3aCgYKASYSARMSFQHGX2Mikzuhy3E2KBBwaMNF59Sjcg0175"

url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages?q=subject:Security Alert"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

responseJson = response.json()

print(responseJson)

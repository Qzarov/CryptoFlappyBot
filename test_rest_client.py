import requests


def integrate_with_third_party():
    #url = "http://localhost:5000/todo/api/v1.0/tasks"
    wallet = "EQBE_FGocrOcmXuCYxMUkRoW-2Ozz0rvOmuCRjkrU6x8ttvE"
    client_side_key = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicXphcm92Il0sImV4cCI6MTgyMjQwNDQyNywiaXNzIjoiQHRvbmFwaV9ib3QiLCJqdGkiOiI1NllBN0RHT0tHVlNTM09HQ0VSUkUzVk0iLCJzY29wZSI6ImNsaWVudCIsInN1YiI6InRvbmFwaSJ9.mIwrMMta0CfR7MwSqqf75VXuI58bkx2cE-oQ_8uQjLkE6rh5jV9K2ZK49X90DJB0ZXdF8Wf90PzwvOcDw5haCw"
    redir_url = "https://t.me/qzarov"

    auth_url = "tonapi.io/login?" + redir_url

    url = "https://tonapi.io/v1/blockchain/getAccount?" + "account=" + wallet

    header = {
        'Authorization': 'Bearer ' + client_side_key
    }

    response = requests.request("GET", url, headers=header)
    print(response.text)
    return response


integrate_with_third_party()

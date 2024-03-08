import data
import sender_stand_request

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def get_kits_headers(auth_token):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + auth_token
    return current_headers


def get_kits_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body




# Тест 1.


def test1():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("a")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]


# Тест 2.


def test2():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabC")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]


# Тест 3.


def test3():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 400


# Тест 4.


def test4():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcD")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 400


# Тест 5.


def test5():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("QWErty")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]


# Тест 6.


def test6():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("Мария")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]

# Тест 7.


def test7():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("\"№%@\",")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]

# Тест 8.


def test8():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body(" Человек и КО ")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]

# Тест 9.


def test9():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body("123")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]



# Тест 10.


def test10():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = {}
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 400


# Тест 11.


def test11():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kits_headers = get_kits_headers(auth_token)
    kit_body = get_kits_body(123)
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    assert kits_response.status_code == 400



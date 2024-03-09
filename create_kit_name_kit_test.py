import data
import sender_stand_request


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


def get_kits_headers():
    user_body = get_user_body("Аа")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + auth_token
    return current_headers


def get_kits_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(kits_response,kit_body):
    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit_body["name"]


def negative_assert(kits_response):
    assert kits_response.status_code == 400


# Тест 1.


def test_kit_name_single_symbol():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("a")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 2.


def test_kit_name_max_symbols():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabC")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 3.


def test_kit_name_empty():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    negative_assert(kits_response)


# Тест 4.


def test_kit_name_512_symbols():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcD")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    negative_assert(kits_response)


# Тест 5.


def test_kit_name_latin_symbols():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("QWErty")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 6.


def test_kit_name_cyrillic_symbols():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("Мария")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 7.


def test_kit_name_special_symbols():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("\"№%@\",")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 8.


def test_kit_name_space_symbols():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body(" Человек и КО ")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 9.


def test_kit_name_digits():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body("123")
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    positive_assert(kits_response, kit_body)


# Тест 10.


def test_kit_empty_body():
    kits_headers = get_kits_headers()
    kit_body = {}
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    negative_assert(kits_response)


# Тест 11.


def test_kit_name_int_type():
    kits_headers = get_kits_headers()
    kit_body = get_kits_body(123)
    kits_response = sender_stand_request.post_new_client_kit(kit_body, kits_headers)
    negative_assert(kits_response)

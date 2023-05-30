import os
from dotenv import load_dotenv, find_dotenv
import json
import base64


def get_service_account_key() -> dict:
    """
    Returns service account key for firestore
    """
    load_dotenv(find_dotenv())
    encoded_key = os.getenv("SERVICE_ACCOUNT_KEY")

    # https://stackoverflow.com/questions/50693871/error-in-json-loads-for-data-that-has-base64-decoding-applied
    dic = base64.b64decode(str(encoded_key)[2:-1]).decode('utf-8')
    return json.loads(dic)


def service_key_to_base64(service_key: dict) -> bytes:
    """
    Converts firebase service key to base64.

    Args:
        service_key (dict): Service account key generated in firebase project
        settings. Check docs for an example of a service key.

    Returns:
        bytes: base64 string. String begins with `b'` and ends with `'`
    """

    # convert json to a string
    str_service_key = json.dumps(service_key)

    # encode service key
    encoded_service_key = base64.b64encode(str_service_key.encode('utf-8'))

    # Format of encoded_service_key: b'a_lot_of_chars'
    return encoded_service_key


if __name__ == "__main__":
    service_key = {
        "type": "service_account",
        "project_id": "xxx",
        "private_key_id": "xxx",
        "private_key": "xxxx",
        "client_email": "xxxx.com",
        "client_id": "xxxx",
        "auth_uri": "xxxx",
        "token_uri": "xxxx",
        "auth_provider_x509_cert_url": "xxxx",
        "client_x509_cert_url": "xxxx"
    }
    print(service_key_to_base64(service_key))
    # b'eyJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsICJwcm9qZWN0X2lkIjogInh4eCIsICJwcml2YXRlX2tleV9pZCI6ICJ4eHgiLCAicHJpdmF0Z
    # V9rZXkiOiAieHh4eCIsICJjbGllbnRfZW1haWwiOiAieHh4eC5jb20iLCAiY2xpZW50X2lkIjogInh4eHgiLCAiYXV0aF91cmkiOiAieHh4eCIsI
    # CJ0b2tlbl91cmkiOiAieHh4eCIsICJhdXRoX3Byb3ZpZGVyX3g1MDlfY2VydF91cmwiOiAieHh4eCIsICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJ4eHh4In0='

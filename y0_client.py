#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
from decouple import config
import requests


def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


def collect():
    yo_client_user_id = config('YO_CLIENT_USER_ID', '')
    yo_server_host = config('YO_SERVER_HOST', '')
    my_mac = get_mac_address()
    print(yo_client_user_id)
    print(my_mac)


if __name__ == "__main__":
    collect()

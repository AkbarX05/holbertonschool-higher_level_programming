#!/usr/bin/python3
"""
Bu skript arqument kimi verilən URL-ə daxil edilmiş email ilə POST
sorğusu göndərir və cavabın gövdəsini (body) göstərir.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

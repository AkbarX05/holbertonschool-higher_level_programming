#!/usr/bin/python3
"""
Bu skript arqument kimi verilən URL-ə sorğu göndərir və
cavabın header hissəsindəki X-Request-Id dəyərini göstərir.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info().get('X-Request-Id'))

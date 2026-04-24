#!/usr/bin/python3
"""
Bu skript requests paketi vasitəsilə statusu yoxlayır
və cavabı formatlaşdırılmış şəkildə göstərir.
"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")

#!/bin/bash

response=$(curl -s -w "%{http_code}" "$1")
body=$(echo "$response" | sed '$d')
status=$(echo "$response" | tail -n1)

if [ "$status" -eq 200 ]; then
    echo "$body"
fi

#!/bin/bash
# Displays the size of the body of a response from a given URL
curl -s "$1" | wc -c

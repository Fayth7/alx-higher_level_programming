#!/bin/bash
# takes a URL, sends a request, and displays the size of response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

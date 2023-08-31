#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body

URL="$1"
curl -sI "$URL" | grep -i Content-Length | awk '{print $2}'

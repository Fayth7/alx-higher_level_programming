#!/bin/bash
# sends a JSON POST request to a URL,displays body of response
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"

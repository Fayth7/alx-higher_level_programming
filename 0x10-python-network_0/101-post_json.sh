#!/bin/bash
# sends a JSON POST request to a URL,displays body of response
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L

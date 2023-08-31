#!/bin/bash
# sends a JSON POST request to a URL,displays body of response
    curl -s -X POST -H "Content-Type: application/json" -d @"$FILE" "$1"
    

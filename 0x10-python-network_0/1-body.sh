#!/bin/bash
#takes URL, sends a GET request to URL, and displays body of response
curl -s -X GET "$1"

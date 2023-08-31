#!/bin/bash
# This script makes a request to a URL and displays the body of the response
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
 
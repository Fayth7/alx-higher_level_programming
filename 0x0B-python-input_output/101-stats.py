#!/usr/bin/python3

import sys

metrics = {
    'total_size': 0,
    'status_codes': {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
}

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split(' ')
        metrics['total_size'] += int(split_line[-1])

        status_code = int(split_line[-2])
        if status_code in metrics['status_codes']:
            metrics['status_codes'][status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(metrics['total_size']))
            for code, count in sorted(metrics['status_codes'].items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    print("File size: {}".format(metrics['total_size']))
    for code, count in sorted(metrics['status_codes'].items()):
        if count > 0:
            print("{}: {}".format(code, count))

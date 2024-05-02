#!/usr/bin/python3
"""script reads stdin line"""
import sys
import re


def main():
    """ function.. """
    fileSize = 0
    count = 0
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    stats = {i: 0 for i in codes}

    def print_stats(fileSize, stats):
        """ print stats """
        print(f'File size: {fileSize}')
        for k in sorted(stats.items()):
            if status[key] != 0:
                print(f'{k}: {status[k]}')

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code += int(data[-1])
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                fileSize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, fileSize)
        print_stats(stats, fileSize)
    except KeyboardInterrupt:
        print_stats(stats, fileSize)
        raise
    if __name__ == "__main__":
        main()

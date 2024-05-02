#!/usr/bin/python3
"""script reads stdin line"""
import sys

def print_stats(file_size, stats):
    """ print stats """
    print(f'File size: {file_size}')
    for code, count in sorted(stats.items()):
        if count != 0:
            print(f'{code}: {count}')

def main():
    """ main function """
    file_size = 0
    count = 0
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    stats = {code: 0 for code in codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = int(data[-2])
                if str(status_code) in stats:
                    stats[str(status_code)] += 1
            except ValueError:
                pass
            try:
                file_size += int(data[-1])
            except ValueError:
                pass
            if count % 10 == 0:
                print_stats(file_size, stats)
        print_stats(file_size, stats)
    except KeyboardInterrupt:
        print_stats(file_size, stats)
        raise

if __name__ == "__main__":
    main()

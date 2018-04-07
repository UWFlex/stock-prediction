"""driver module"""
import sys
import getopt
import time
import fetch_combined_data
# import validate_stock_data


def main(argv):
    '''driver method'''
    start = time.time()

    try:
        opts, _ = getopt.getopt(argv, 'f', ['fetch'])
    except getopt.GetoptError:
        print('run.py')
        sys.exit(2)

    print('-----command line options-----')
    print(opts)

    for opt, _ in opts:
        if opt in ('-f', '--fetch'):
            print('-----fetching new data-----')
            # fetch
            fetch_combined_data.fetch(
                'input/symbols',
                'input/indicators',
            )

    elapsed = time.time() - start

    print('time elapsed: ' + str(elapsed))
    print('-----program finished-----')



    # validate
    # validate_stock_data.validate(
    #     context[env]['output_raw'],
    #     context[env]['output_valid']
    # )


if __name__ == '__main__':
    main(sys.argv[1:])

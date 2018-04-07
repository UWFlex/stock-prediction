"""driver module"""
import sys
import getopt
import time
import fetch_combined_data

def main(argv):
    '''driver method'''
    start = time.time()

    try:
        opts, _ = getopt.getopt(argv, 'ft', ['fetch'])
    except getopt.GetoptError:
        print('run.py')
        sys.exit(2)

    print('-----command line options-----')
    print(opts)

    single_opt = [opt[0] for opt in opts]


    # run pipeline in order according to command line options
    if '-f' or '--fetch' in single_opt:
        print('-----fetching new data-----')
        # fetch
        fetch_combined_data.fetch(
            'input/symbols',
            'input/indicators',
            'output/raw'
        )


    elapsed = time.time() - start

    print('time elapsed: ' + str(round(elapsed, 2)) + " seconds")
    print('-----program finished-----')



    # validate
    # validate_stock_data.validate(
    #     context[env]['output_raw'],
    #     context[env]['output_valid']
    # )


if __name__ == '__main__':
    main(sys.argv[1:])

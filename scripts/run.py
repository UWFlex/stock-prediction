"""driver module"""
import sys
import getopt
import time
import fetch_combined_data
import preprocess

def main(argv):
    '''driver method'''
    start = time.time()

    try:
        opts, _ = getopt.getopt(argv, 'fp', ['fetch', 'preprocess'])
    except getopt.GetoptError:
        print('run.py')
        sys.exit(2)

    print('-----command line options-----')
    print(opts)

    single_opt = [opt[0] for opt in opts]


    # run pipeline in order according to command line options
    if '-f' in single_opt or '--fetch' in single_opt:
        print('-----fetching new data-----')
        # fetch
        fetch_combined_data.fetch(
            'input/symbols',
            'input/indicators',
            'output/raw'
        )
    if '-p' in single_opt or '--preprocess' in single_opt:
        print('-----preprocessing data-----')
        # fetch
        preprocess.preprocess_batch(
            'output/raw',
            'output/preprocessed',
            0.8
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

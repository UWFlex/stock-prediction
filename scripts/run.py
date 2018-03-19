"""driver module"""
import sys
import getopt
import fetch_combined_data
import validate_stock_data


def main(argv):
    '''driver method'''
    try:
        opts, _ = getopt.getopt(argv, 'p', ['production'])
    except getopt.GetoptError:
        print('run.py')
        sys.exit(2)
    env = 'dev'
    for opt, _ in opts:
        if opt in ('-p', '--production'):
            print('Running in production mode')
            env = 'prod'
    if env == 'dev':
        print('Running in development mode')

    # data pipe line:
    # fetch -> validate -> normalize -> dump into db
    context = {
        'dev': {
            'input_symbols': 'input/dev_symbols',
            'input_indicators': 'input/dev_indicators',
            'output_raw': 'output/dev/raw',
            'output_valid': 'output/dev/valid'
        },
        'prod': {
            'input_symbols': 'input/prod_symbols',
            'input_indicators': 'input/prod_indicators',
            'output_raw': 'output/prod/raw',
            'output_valid': 'output/prod/valid'
        }
    }

    # fetch
    fetch_combined_data.fetch(
        context[env]['input_symbols'],
        context[env]['input_indicators'],
        context[env]['output_raw']
    )

    # validate
    # validate_stock_data.validate(
    #     context[env]['output_raw'],
    #     context[env]['output_valid']
    # )


if __name__ == '__main__':
    main(sys.argv[1:])

def main():
    import sys
    import argparse
    sys.path.insert(0, '../../.')  # noqa
    import my_utils

    parser = argparse.ArgumentParser(
                description='Usage: get_data.py --datafile INPUTFILE'
                            '--outfile OUTFILE --country COUNTRY'
                            '--x_datacol RESULT_COLUMN'
                            '--y_datacol RESULT_COLUMN',
                prog='get_data')

    parser.add_argument('--datafile',
                        type=str,
                        help='Data file name',
                        required=True)

    parser.add_argument('--outfile',
                        type=str,
                        help='Output file name',
                        required=True)

    parser.add_argument('--country',
                        type=str,
                        help='Country',
                        required=True)

    parser.add_argument('--x_datacol',
                        type=str,
                        help='Column containing desired x results',
                        required=True)

    parser.add_argument('--y_datacol',
                        type=str,
                        help='Column containing desired y results',
                        required=True)

    args = parser.parse_args()
    country = args.country
    x_datacol = args.x_datacol
    y_datacol = args.y_datacol
    datafile = args.datafile
    outfile = args.outfile

    # Get x data using get_column function
    x_data = my_utils.get_column(file_name=datafile,
                                 query_column='Area',
                                 query_value=country,
                                 result_column=x_datacol)

    # Get y data using get_column
    y_data = my_utils.get_column(file_name=datafile,
                                 query_column='Area',
                                 query_value=country,
                                 result_column=y_datacol)

    # Get list of years associated with data
    years = my_utils.get_column(file_name=datafile,
                                query_column='Area',
                                query_value=country,
                                result_column='Year')

    # Write data to text file
    with open(outfile, 'w') as outf:
        outf.write(country + '\n')
        for i, xval in enumerate(x_data):
            line = str(years[i]) + ' ' + str(xval) \
                    + ' ' + str(y_data[i]) + '\n'
            outf.write(line)


if __name__ == '__main__':
    main()

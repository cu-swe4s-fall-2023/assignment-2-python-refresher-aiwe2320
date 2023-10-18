def main():
    import sys
    import matplotlib
    import matplotlib.pyplot as plt
    import argparse

    parser = argparse.ArgumentParser(
                description='Usage: hist.py --datafile FILE_NAME'
                            '--data_label DATA_LABEL'
                            '--col_ndx COLUMN_INDEX'
                            '--title TITLE --outfile OUTFILE',
                prog='hist')

    parser.add_argument('--datafile',
                        type=str,
                        help='Data file name',
                        required=True)

    parser.add_argument('--data_label',
                        type=str,
                        help='x data label',
                        required=True)

    parser.add_argument('--col_ndx',
                        type=int,
                        help='Index of data column',
                        required=True)

    parser.add_argument('--title',
                        type=str,
                        help='Plot title',
                        required=True)

    parser.add_argument('--outfile',
                        type=str,
                        help='Output file name',
                        required=True)

    args = parser.parse_args()
    data_label = args.data_label
    title = args.title
    datafile = args.datafile
    outfile = args.outfile
    col_ndx = args.col_ndx

    # Check index range
    if not (col_ndx >= 0 and col_ndx <= 2):
        print("ERROR: Column index out of range")
        sys.exit(1)

    # Make scatter plot of y vs x
    # Data file looks like "COUNTRY"
    #                      "YEAR x1 y1"
    #                      "YEAR x2 y2"
    # etc.
    data = []

    with open(datafile, 'r') as f:
        for i, line in enumerate(f):  # Parse data line by line
            if (i != 0):
                tmp = line.strip().split()
                data.append(tmp[col_ndx])

    # Convert values to integers
    data_int = []
    try:
        data_int = [int(val) for val in data]
    except Exception as e:
        print("ERROR: Data is non-numerical")
        sys.exit(1)

    fig, ax = plt.subplots()
    ax.hist(data_int, edgecolor='black')
    ax.set_xlabel(data_label)
    ax.set_ylabel("Frequency")
    ax.set_title(title)

    plt.savefig(outfile)


if __name__ == '__main__':
    main()

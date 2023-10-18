def main():
    import sys
    import matplotlib
    import matplotlib.pyplot as plt
    import argparse

    parser = argparse.ArgumentParser(
                description='Usage: scatter.py --datafile FILE_NAME'
                            '--x_label X_LABEL --y_label Y_LABEL'
                            '--title TITLE --outfile OUTFILE',
                prog='scatter')

    parser.add_argument('--datafile',
                        type=str,
                        help='Data file name',
                        required=True)

    parser.add_argument('--x_label',
                        type=str,
                        help='x data label',
                        required=True)

    parser.add_argument('--y_label',
                        type=str,
                        help='y data label',
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
    x_label = args.x_label
    y_label = args.y_label
    title = args.title
    datafile = args.datafile
    outfile = args.outfile

    # Make scatter plot of y vs x
    # Data file looks like "COUNTRY"
    #                      "YEAR x1 y1"
    #                      "YEAR x2 y2"
    # etc.
    years = []
    x = []
    y = []

    with open(datafile, 'r') as f:
        for i, line in enumerate(f):  # Parse data line by line
            if (i != 0):
                tmp = line.strip().split()
                years.append(tmp[0])
                x.append(tmp[1])
                y.append(tmp[2])

    # Convert values to integers
    xint = []
    yint = []
    try:
        xint = [int(val) for val in x]
        yint = [int(val) for val in y]
    except Exception as e:
        print("ERROR: x or y indices non-numerical")
        sys.exit(1)

    fig, ax = plt.subplots()
    ax.scatter(xint, yint)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.savefig(outfile, bbox_inches='tight')


if __name__ == '__main__':
    main()

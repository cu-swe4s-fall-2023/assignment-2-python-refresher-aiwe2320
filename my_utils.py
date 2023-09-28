def get_column(file_name, query_column, query_value, result_column='Area'):
    """Search csv file for queried value and return list of matching results

    Parameters
    ----------
    file_name : string
                csv file name

    query_column : string
                Exact name of query column

    query_value : string
                Value searching for

    result_column : string
                Exact name of column to pull results from

    Returns
    -------
    result_int_list
        List of result column integer values if values are numerical
        None if unsuccessful search
    result_list
        List of result column values if values are not numerical
        None if unsuccessful

    """
    result_list = []

    with open(file_name, 'r') as f:
        if not f:
            # print("File is empty!")
            return None
        else:
            query_ndx = -1
            result_ndx = -1
            for i, line in enumerate(f):  # Open file and parse line by line
                temp = line.split(',')
                if(i == 0):  # If reading first line, find array indices
                    for j, col in enumerate(temp):
                        if(col == query_column):
                            query_ndx = j  # Query column array index
                        elif(col == result_column):
                            result_ndx = j

                    # Columns not found
                    if(query_ndx == -1 and result_ndx == -1):
                        # Query and result column names not found
                        return None
                    elif(query_ndx == -1):
                        # Query column name not found
                        return None
                    elif(result_ndx == -1):
                        # Result column name not found
                        return None

                # Check data in line
                if(temp[query_ndx] == query_value):
                    result_list.append(temp[result_ndx])

    # Check if results list is empty
    if not result_list:
        # print("No matching queries found")
        return None
    else:
        try:  # try to convert list to integers
            result_float_list = [float(entry) for entry in result_list]
            result_int_list = [int(entry) for entry in result_float_list]
            return result_int_list
        except Exception as e:  # If non-numerical, return strings
            return result_list


def main():
    print("my_utils.py Library:")
    print("   get_column(file_name, query_column, query_value, result_column)")


if __name__ == '__main__':
    main()

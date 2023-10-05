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
                        if(col.strip() == query_column):
                            query_ndx = j  # Query column array index
                        elif(col.strip() == result_column):
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
                    result_list.append(temp[result_ndx].strip())

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


def mean(arr):
    """Calculate the mean of a list of values

    Parameters
    ----------
    arr : list
        List of values, can be of mixed type

    Returns
    -------
    mean
        Arithmetic mean of numerical values in list
        None if no numbers found or list empty

    """
    if arr:
        total = 0
        count = 0
        for val in arr:
            try:
                num = float(val)
                total += num
                count += 1
            except Exception as e:
                continue  # Skip over strings
        # Calculate mean, return if nonzero
        if count > 0:
            mean = total / count
            return mean
        else:
            return None  # No numerical entries
    else:  # If arr is empty
        return None


def median(arr):
    """Find the median of a list of values

    Parameters
    ----------
    arr : list
        List of values, can be of mixed type

    Returns
    -------
    median
        Median of numerical values in list
        None if no numbers found or list empty

    """
    # Get list of numerical entries
    temp = []
    for val in arr:
        try:
            num = float(val)
            temp.append(num)
        except Exception as e:
            continue
    if temp:
        # Sort list of numbers using built in Python list sorting
        sortlist = sorted(temp)
        llen = len(temp)
        if llen % 2 == 0:  # Even length
            low_ndx = (llen - 1) // 2  # Use int division to get floored value
            low_num = sortlist[low_ndx]
            high_num = sortlist[low_ndx + 1]
            median = (low_num + high_num) / 2
        else:  # Odd length
            ndx = (llen - 1) // 2
            median = sortlist[ndx]
        return median
    else:
        return None


def stdeviation(arr):
    """Calculate the standard deviation of a list of values

    Parameters
    ----------
    arr : list
        List of values, can be of mixed type

    Returns
    -------
    median
        Standard deviation of numerical values in list
        None if no numbers found or list empty

    """
    # Must use mean function
    avg = mean(arr)
    if avg is None:
        return None
    else:
        if arr:
            running_sum = 0
            N = 0
            for val in arr:
                try:  # Calculate contribution to sum
                    x = float(val)
                    running_sum += pow((x - avg), 2)
                    N += 1
                except Exception as e:  # Ignore string inputs
                    continue
            if N > 0:
                stdev = pow((running_sum / N), 0.5)
                return stdev
            else:
                return None
        else:
            return None


def main():
    print("my_utils.py Library:")
    print("    get_column(file_name, query_column, "
          "query_value, result_column)")
    print("    mean(arr)")
    print("    median(arr)")
    print("    stdeviation(arr)")


if __name__ == '__main__':
    main()

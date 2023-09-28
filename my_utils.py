def get_column(file_name, query_column, query_value, result_column='Area'):
    """
    Function: get_column(file_name, query_column, query_value, result_column='Area')

    Given a csv file that is comma separated and the name of a query column, query value, and result column,
    search the csv file for the queried value and return the corresponding value in the result column.
    Will return a list of results.
    
    Input:
        file_name: csv file name
        query_column: string of exact name of query column
        query_value: string of value searching for
        result_column: string of exact name of column to pull results from
    
    Output:
        List of result column values if successful search
        None if unsuccessful
    """
    result_list = []
    
    with open(file_name,'r') as f:
        if not f:
            #print("File is empty!")
            return None
        else:
            query_ndx = -1
            result_ndx = -1
            for i,line in enumerate(f): # Open file and parse line by line
                temp = line.split(',')
                if(i == 0): # If reading first line, find array indices
                    for j,col in enumerate(temp):
                        if(col == query_column):
                            query_ndx = j # Query column array index
                        elif(col == result_column):
                            result_ndx = j

                    # Columns not found
                    if(query_ndx == -1 and result_ndx == -1):
                        #print('Query and result column names not found, please try again')
                        return None
                    elif(query_ndx == -1):
                        #print("Query column name not found, please try again")
                        return None
                    elif(result_ndx == -1):
                        #print("Result column name not found, please try again")
                        return None

                # Check data in line
                if(temp[query_ndx] == query_value):
                    result_list.append(temp[result_ndx])

    # Check if results list is empty
    if not result_list:
        #print("No matching queries found")
        return None
    else:
        try: # try to convert list to integers
            result_float_list = [float(entry) for entry in result_list]
            result_int_list = [int(entry) for entry in result_float_list]
            return result_int_list
        except:
            return result_list

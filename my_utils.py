def get_column(file_name, query_column, query_value, result_column):
    #Input validation
    if(result_column == query_column):
        print("Query column and result column are identical!")
        return None
    
    result_list = []
    
    with open(file_name,'r') as f:
        if not f:
            print("File is empty!")
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
                        print('Query and result column names not found, please try again')
                        return None
                    elif(query_ndx == -1):
                        print("Query column name not found, please try again")
                        return None
                    elif(result_ndx == -1):
                        print("Result column name not found, please try again")
                        return None

                # Check data in line
                if(temp[query_ndx] == query_value):
                    result_list.append(temp[result_ndx])

    # Check if results list is empty
    if not result_list:
        print("No matching queries found")
        return None
    else:
        return result_list

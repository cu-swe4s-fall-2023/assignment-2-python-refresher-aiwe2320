import my_utils
country='United States of America'
fire_col_name = 'Forest fires'
country_col_name = 'Area'
year_col_name = 'Year'
file_name = 'Agrofood_co2_emission.csv'
# get_column(file_name, query_column, query_value, result_column)
forest_fires = my_utils.get_column(file_name,country_col_name,country,fire_col_name)
year_list = my_utils.get_column(file_name,country_col_name,country,year_col_name)
fire_by_year = list(zip(year_list,forest_fires))
print(f'Total Forest Fires in the {country} by Year:')
print("Year: Fires")
for item in fire_by_year:
    print(f'{item[0]}: {item[1]}')

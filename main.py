import pandas as pd


# sort them based on first column desc order
# check if phone number starts the prefix
# (as fetching in desc order the highest prefix will match first)
# break out once the first match is found
def phone_prefix_match(data, phone_number):
    """

    :param phone_number: str
    :param data: dataframe
    :return: dict ex: {'operator1.csv': 0.3, 'operator2.csv': 0.1}
    """
    operator_price_data = {}
    for key, val in data.items():
        desc_table = val.sort_values(by=0, ascending=False)
        for index, row in desc_table.iterrows():
            str_prefix = str(int(row[0]))
            if phone_number.startswith(str_prefix):
                operator_price_data[key] = row[1]
                break
    return operator_price_data


# operator_price_dict has all the matched prefix operator with price/min
def min_price_operator_checker(operator_price_data):
    """

    :param operator_price_data: dict ex: {'operator1.csv': 0.3, 'operator2.csv': 0.1}
    :return: None
    """
    if operator_price_data:
        min_operator = min(operator_price_data, key=operator_price_data.get)
        min_operator_price = min(operator_price_data.values())
        print('Operator who provides cheapest rate is:', min_operator)
        print('Price offered by the operator is :', min_operator_price)
        return min_operator,min_operator_price
    else:
        print('There are no operator available')
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Expected comma separated Input file names which are in csv format ex: operator1.csv,operator2.csv
    print("Enter Operator file names in comma separated (Expected CSV files): ")
    file_names = input()

    # Enter the phone number to be checked
    print('Enter the phone number:')
    phone_no = input()

    # read the operator file, used pandas csv reader for reading
    file_list = file_names.split(',')
    data_dict = {}
    for file in file_list:
        df = pd.read_csv(file, header=None)
        data_dict[file] = df

    operator_price_dict = phone_prefix_match(data_dict, phone_no)
    min_price_operator_checker(operator_price_dict)


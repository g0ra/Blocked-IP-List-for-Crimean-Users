import pandas as pd

file_ip_xls = "ASKozlov.xls"
file_ip_txt = "blocked_from_crimea_ip_list.txt"

xl_file = pd.ExcelFile(file_ip_xls)

with open(file_ip_txt,'w') as log:
    for sheet_name in xl_file.sheet_names:
        df = xl_file.parse(sheet_name, header = None)
        df_list = df.to_string(header = False, index = False, index_names = False).split('\n')
        for value in df_list:
            log.write('{}\n'.format(value.strip()))
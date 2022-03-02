import os
import csv


log_file_path = os.path.expanduser("~/Downloads/klaviyo_25-10-2021.log")

log_rows = []

endpoints = ['products', 'orders', 'customers', 'shipments', 'categories']

with open(log_file_path, 'r') as file:
    logs = file.readlines()
    for row in logs:
        columns = row.split(' ')
        cols = [c.strip('[]- ') for c in columns]
        endpoint = cols[7].split('?')

        # account for log rows with no endpoint data
        if len(endpoint) < 2: continue
        params = endpoint[0].split('/')

        # account for log rows with extra param between /rest/ and /<endpoint>/
        if len(params) < 6 or (len(params) == 6 and params[5] in endpoints):
            endpoint_params = None,
        elif params[4] not in endpoints and len(params) == 6:
            endpoint_params = None
        elif params[4] not in endpoints:
            endpoint_params = params[6]
        else:
            endpoint_params = params[5]

        log_rows.append(
            {
             "ip": columns[1],
             "date": columns[4],
             "method": columns[6],
             "endpoint": params[4] if params[4] in endpoints else params[5],
             "endpoint_params": endpoint_params,
             "response": columns[9]
            }
        )


data_file1 = open(os.path.expanduser("~/data_log_file.csv"), 'w')
data_file2 = open(os.path.expanduser("~/data_log_file2.csv"), 'w')
csv_writer1 = csv.writer(data_file1)
csv_writer2 = csv.writer(data_file2)


count = 0
for row in log_rows[0:500000]:
    if count == 0:
        csv_writer1.writerow(row.keys())
        count += 1
    csv_writer1.writerow(row.values())

count = 0
for row in log_rows[500001:]:
    if count == 0:
        csv_writer2.writerow(row.keys())
        count +=1
    csv_writer2.writerow(row.values())
    

data_file1.close()
data_file2.close()
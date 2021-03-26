def get_web_data(url):
    # example: read earthquake data from usgs
    response = requests.get(url)
    # get website response in unicode
    csv_io = io.StringIO(response.text)
    # creater csv reader object
    reader = csv.reader(csv_io)
    # set up headers and data rows
    header = next(reader) # sets up the first line of data as the header
    data_body = [data_holder(row) for row in header] # hold data from each reader line
    data_body = [q for q in data_body if q.magnitude > 0]
    print(f'header row: {header}')
    return data_body

def handle_errors(message):
    if message == '1':
        raise BaseException("Server Error")
    elif message == '502':
        raise BaseException("Data Unavailable")
    elif message == '0':
        print("Request Successfully Processed")
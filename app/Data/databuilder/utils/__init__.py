def get_file_binary_data(filename):
    with open(filename, 'rb') as f:
        b_data = f.read()
    return b_data


if __name__ == '__main__':
    pass

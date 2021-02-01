import app.data.repository.table_functions as tf


def row_to_dict(row):
    return tf.row_to_dict(row)


def rows_to_dicts(rows):
    return tf.rows_to_dicts(rows)


def refresh_row(row):
    tf.refresh_row(row)


if __name__ == '__main__':
    pass

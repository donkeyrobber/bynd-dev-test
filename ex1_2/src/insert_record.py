import pymysql

def insert_record(data):
    if type(data['name']) is not str:
        print('name must be a string')
        return 1

    if type(data['age']) is not int:
        print('name must be a string')
        return 1

    conn = pymysql.connect(
        host='db',
        user='dev_test',
        password='xr5dr6nne47BEDEB',
        database='dev_test'
    )
    sql = "INSERT INTO record (name, age) VALUE (%s, %s)"

    with conn.cursor() as cursor:
        cursor.execute(sql, (data['name'], data['age']))

        conn.commit()

        data.update(id=cursor.lastrowid)

    return data

if __name__ == '__main__':

    data = {
        'name': 'Main One',
        'age': 37
    }

    insert_record(data)

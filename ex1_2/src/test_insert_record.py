import unittest
import pymysql

from insert_record import insert_record

class InsertRecordTest(unittest.TestCase):

    test_record_id = None

    def test_insert_record_returns_valid_record_id(self):

        record_data = {
            'name': 'Tester One',
            'age': 24
        }

        record = insert_record(record_data)
        self.assertIn('id', record)

        self.test_record_id = record['id']

    def tearDown(self):
        sql = "DELETE FROM record WHERE id = %s"

        conn = pymysql.connect(
            host='db',
            user='dev_test',
            password='xr5dr6nne47BEDEB',
            database='dev_test'
        )
        with conn.cursor() as cursor:
            cursor.execute(sql, self.test_record_id)

            conn.commit()

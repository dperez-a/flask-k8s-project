from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'mysql-service'),
        database=os.environ.get('MYSQL_DATABASE', 'test_db'),
        user=os.environ.get('MYSQL_USER', 'appuser'),
        password=os.environ.get('MYSQL_PASSWORD', 'apppassword')
    )

@app.route('/api/message')
def get_message():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT text FROM message LIMIT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result:
            return jsonify({'message': result[0]})
        return jsonify({'message': 'No message found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### `backend/requirements.txt`
```
Flask==3.0.0
mysql-connector-python==8.2.0
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://backend-service:5000')

@app.route('/')
def index():
    try:
        response = requests.get(f'{BACKEND_URL}/api/message')
        if response.status_code == 200:
            data = response.json()
            message = data.get('message', 'No message')
        else:
            message = 'Error fetching message'
    except Exception as e:
        message = f'Error: {str(e)}'
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

#### `frontend/requirements.txt`
```
Flask==3.0.0
requests==2.31.0
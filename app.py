from src import create_app
import os

app = create_app()

if __name__ == '__main__':
    app.run(debug=True if app.config['ENV'] == 'development' else False, host=app.config['HOST'],
            port=app.config['PORT'])

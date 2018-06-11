import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route('/')
def index():
    return "Bam "

def main():
    app.run()

if __name__ == '__main__':
    main()
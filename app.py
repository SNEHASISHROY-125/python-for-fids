from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)

# Directory to store static files
STATIC_DIR = os.path.join(os.getcwd(), 'static', 'images')

@app.route('/get_schedule', methods=['GET'])
def get_schedule():
    return send_from_directory(os.getcwd(), 'schedule.json')

@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route('/')
def display_page():
    return render_template('display.html')

if __name__ == '__main__':
    # Replace '192.168.1.100' with your actual local IP address
    app.run(host='192.168.1.2', port=5000, debug=True)




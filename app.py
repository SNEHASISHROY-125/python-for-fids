from flask import Flask, jsonify, send_from_directory, render_template
import os 
# import control as c

app = Flask(__name__)

# Directory to store static files
STATIC_DIR = os.path.join(os.getcwd(), 'static', 'images')

# @app.route('/get_schedule', methods=['GET'])
# def get_schedule():
#     return send_from_directory(os.getcwd(), 'schedule.json')

# Define the data structure
data = [
    {
        "type": "info",
        "data": [
            {
                "logo": "static/images/indigo-logo.png",
                "flight": "AA123",
                "arrival": "10:00 AM",
                "departure": "12:00 PM",
                "status": "On Time"
            },
            {
                "logo": "static/images/delta-logo.png",
                "flight": "DL456",
                "arrival": "11:00 AM",
                "departure": "1:00 PM",
                "status": "Delayed"
            }
        ]
    },
    {
        "type": "image",
        "data": "static/images/image1.png",
        "timer": 1000,
        "hide": False
    },
    {
        "type": "video",
        "data": "static/videos/video3.mp4",
        "timer": 5,
        "hide": False
    }
]

# Endpoint to get the schedule
@app.route('/get_schedule', methods=['GET'])
def get_schedule():
    return jsonify(data)


@app.route('/static/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route('/')
def display_page():
    return render_template('display.html')

if __name__ == '__main__':
    # Replace '192.168.1.100' with your actual local IP address
    app.run(host='192.168.1.4', port=5000, debug=True)

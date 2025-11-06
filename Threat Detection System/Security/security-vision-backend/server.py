# server.py
# This is the backend server for your security vision system.

from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import time
import random
from threading import Lock
from datetime import datetime

# --- Basic Setup ---
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
app.config['SECRET_KEY'] = 'your-very-secret-key!' 
socketio = SocketIO(app, cors_allowed_origins="*")

print("Backend server starting...")

# --- Data & State ---
# Default settings, will be updated by the client.
venue_settings = {
    'securityGuards': 4,
    'otherStaff': 10,
    'maxCapacity': 250
}

# In a real application, this data would come from your CV model.
alert_titles = ["Potential Intoxication", "Guard Line Obstructed", "Person Approaching Guard", "Potential Weapon Detected", "Aggressive Posture Detected"]
alert_levels = ["Info", "Medium", "High"]
alert_descriptions = ["Subject near Main Entrance showing unsteady gait.", "Security Guard #2 standing on exit line for 25s at Patio Exit.", "Unidentified person approaching Security Guard #4.", "Object resembling a weapon detected near the bar.", "Two individuals in a heated argument near the dance floor."]

thread = None
thread_lock = Lock()

# --- Background Task to Simulate Live Data ---

def background_data_simulator():
    """
    This function runs in the background and simulates data
    coming from your computer vision model. It sends an update
    every few seconds.
    """
    print("Starting data simulator thread...")
    # Start guest count at a realistic level (e.g., 90% of default capacity)
    guest_count = int(venue_settings['maxCapacity'] * 0.9)
    alert_id = 3

    while True:
        socketio.sleep(random.randint(5, 10))
        
        # ### START OF MODIFIED LOGIC ###
        
        # Retrieve current settings
        max_guests = venue_settings['maxCapacity']
        
        # Prevent guest count from exceeding max capacity
        if guest_count >= max_guests:
            # If at max capacity, simulate someone leaving
            guest_count -= 1
        else:
            # Otherwise, simulate normal entry/exit
            if random.random() < 0.6: # 60% chance of entering
                guest_count += 1
            else: # 40% chance of exiting
                guest_count -= 1
        
        # Ensure guest count doesn't go below zero
        if guest_count < 0:
            guest_count = 0

        # Calculate total occupancy and percentage using the latest settings
        total_staff = venue_settings['securityGuards'] + venue_settings['otherStaff']
        total_occupancy = guest_count + total_staff
        total_capacity = max_guests + total_staff
        
        # Calculate percentage, avoiding division by zero
        occupancy_percentage = (total_occupancy / total_capacity * 100) if total_capacity > 0 else 0
        
        # Create a richer data object to send to the client
        occupancy_data = {
            'current': guest_count,
            'percentage': round(occupancy_percentage, 2)
        }
        
        # Emit the enhanced occupancy update
        print(f"Sending occupancy update: {occupancy_data}")
        socketio.emit('occupancy_update', occupancy_data)

        # ### END OF MODIFIED LOGIC ###

        # 50% chance to also send a new alert
        if random.random() < 0.5:
            alert_id += 1
            new_alert = {
                'id': alert_id,
                'time': datetime.now().isoformat(),
                'level': random.choice(alert_levels),
                'title': random.choice(alert_titles),
                'description': random.choice(alert_descriptions)
            }
            print(f"Sending new alert: {new_alert['title']}")
            socketio.emit('new_alert', new_alert)


# --- SocketIO Event Handlers ---

@socketio.on('connect')
def handle_connect():
    """
    This function is called when a new client (your React app) connects to the server.
    """
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_data_simulator)
    print('Client connected successfully!')
    # Optional: You can ask the client to send its latest settings upon connection
    emit('request_settings')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected.')


@socketio.on('config_update')
def handle_config_update(data):
    """
    Handles configuration updates for individual cameras (e.g., line positions).
    """
    print('Received camera configuration update from client:')
    print(data)
    # In a real app, you would pass this data to your CV model script.


# ### NEW EVENT HANDLER ###
@socketio.on('settings_update')
def handle_settings_update(data):
    """
    Handles updates to the main venue settings from the configuration panel.
    """
    global venue_settings
    print('Received venue settings update from client:')
    print(data)
    venue_settings.update(data)


# --- Main Execution ---

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)
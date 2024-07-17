import subprocess
import signal
import time
from datetime import datetime
import os

class Ros2BagRecorder:
    def __init__(self, bag_name_prefix, save_directory):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.bag_name = f"{bag_name_prefix}_{timestamp}"
        self.save_directory = save_directory
        self.process = None
    
    def start_recording(self):
        os.makedirs(self.save_directory, exist_ok=True)
        full_path = os.path.join(self.save_directory, self.bag_name)
        command = ['ros2', 'bag', 'record', '-a', '-o', full_path]
        self.process = subprocess.Popen(command)
        print(f"Started recording to bag: {full_path}")
   
    def stop_recording(self):
        if self.process:
            self.process.send_signal(signal.SIGINT)
            self.process.wait()
            print(f"Stopped recording to bag: {self.bag_name}")

if __name__ == '__main__':
    bag_name = 'bunker_bag'
    save_directory = '/path/to/save/directory'  # Change this to your desired directory
    topics = ['/tree_info', '/rosout']

    recorder = Ros2BagRecorder(bag_name, save_directory)

    try:
        recorder.start_recording()
        print("Recording... Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Recording interrupted by user.")
    finally:
        recorder.stop_recording()

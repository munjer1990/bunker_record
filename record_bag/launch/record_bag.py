import subprocess
import signal
import time
from datetime import datetime

class Ros2BagRecorder:
    def __init__(self, bag_name_prefix):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.bag_name = f"{bag_name_prefix}_{timestamp}"
        self.process = None
    
    def start_recording(self):
        command = ['ros2', 'bag', 'record', '-a', '-o', self.bag_name]
        self.process = subprocess.Popen(command)
        print(f"Started recording to bag: {self.bag_name}")
   
    #  >>>>>>>>>>>>>>for selected topics uncomment two function
        
    # def __init__(self, bag_name_prefix, topics):
    #     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    #     self.bag_name = f"{bag_name_prefix}_{timestamp}"
    #     self.topics = topics
    #     self.process = None
    
    # def start_recording(self):
    #     command = ['ros2', 'bag', 'record', '-o', self.bag_name] + self.topics
    #     self.process = subprocess.Popen(command)
    #     print(f"Started recording to bag: {self.bag_name} on topics: {', '.join(self.topics)}")

    def stop_recording(self):
        if self.process:
            self.process.send_signal(signal.SIGINT)
            self.process.wait()
            print(f"Stopped recording to bag: {self.bag_name}")

if __name__ == '__main__':
    bag_name = 'bunker_bag'
    topics = ['/tree_info', '/rosout']

    # recorder = Ros2BagRecorder(bag_name, topics)    #for selected topics
    
    recorder = Ros2BagRecorder(bag_name)

    try:
        recorder.start_recording()
        print("Recording... Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Recording interrupted by user.")
    finally:
        recorder.stop_recording()

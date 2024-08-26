import psutil
import time
import sys
import threading

# Function to monitor high CPU usage
def find_high_cpu_usage(threshold=30.0):
    print(f"Monitoring processes with CPU usage above {threshold}%. Press 'q' to quit.")
    while True:
        try:
            # Clear screen (optional)
            print("\033c", end="")
            
            # Find and display processes with high CPU usage
            found = False
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    pid = proc.info['pid']
                    name = proc.info['name']
                    cpu_usage = proc.info['cpu_percent']
                    
                    if cpu_usage > threshold:
                        print(f"PID: {pid}, Name: {name}, CPU Usage: {cpu_usage}%")
                        found = True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            
            if not found:
                print("No processes using more than 100% CPU.")
            
            # Delay before the next iteration
            time.sleep(1)
            
            # Check if 'q' was pressed
            if input() == 'q':
                print("Exiting...")
                break
                
        except KeyboardInterrupt:
            print("\nExiting due to keyboard interrupt.")
            break

if __name__ == "__main__":
    # Run the function to monitor CPU usage
    find_high_cpu_usage()

# Import necessary libraries
import psutil  # For system and process utilities
import time    # For time-related functions, like sleep
import datetime  # For getting current date and time
import csv      # For writing data to a CSV file
import os       # For file system operations, like checking if a file exists

# --- Configuration ---
LOG_INTERVAL = 10  # Seconds between each log entry
LOG_FILE_NAME = "system_performance_log.csv"  # Name of the log file


def get_system_stats():
    """
    Retrieves current CPU and memory usage.

    Returns:
        tuple: A tuple containing (cpu_percent, memory_percent)
               Returns (None, None) if an error occurs.
    """
    try:
        # Get CPU usage percentage
        # interval=1 means it will block for 1 second to get a more accurate reading.
        # If you want non-blocking, set interval=None, but it might be less accurate
        # or return 0.0 on the first call.
        cpu_percent = psutil.cpu_percent(interval=1)

        # Get virtual memory usage (RAM)
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        return cpu_percent, memory_percent
    except Exception as e:
        print(f"Error getting system stats: {e}")
        return None, None


def log_stats(timestamp, cpu_usage, memory_usage):
    """
    Logs the system stats to a CSV file.

    Args:
        timestamp (str): The current timestamp.
        cpu_usage (float): Current CPU usage percentage.
        memory_usage (float): Current memory usage percentage.
    """
    file_exists = os.path.isfile(
        LOG_FILE_NAME)  # Check if log file already exists

    try:
        with open(LOG_FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write header only if the file is new
            if not file_exists or os.path.getsize(LOG_FILE_NAME) == 0:
                writer.writerow(
                    ["Timestamp", "CPU Usage (%)", "Memory Usage (%)"])

            # Write the data row
            writer.writerow([timestamp, cpu_usage, memory_usage])
    except IOError as e:
        print(f"Error writing to log file {LOG_FILE_NAME}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during logging: {e}")


def main():
    """
    Main function to run the system performance monitor.
    """
    print("Starting System Performance Monitor...")
    print(f"Logging data every {LOG_INTERVAL} seconds to {LOG_FILE_NAME}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            # Get current timestamp
            now = datetime.datetime.now()
            timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

            # Get system stats
            cpu, mem = get_system_stats()

            if cpu is not None and mem is not None:
                # Log the stats
                log_stats(timestamp_str, cpu, mem)
                print(f"{timestamp_str} - CPU: {cpu}%, Memory: {mem}% - Logged.")
            else:
                print(
                    f"{timestamp_str} - Failed to retrieve stats. Skipping log entry.")

            # Wait for the defined interval
            time.sleep(LOG_INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user (Ctrl+C).")
    except Exception as e:
        print(f"An unexpected error occurred in the main loop: {e}")
    finally:
        print("Exiting System Performance Monitor.")


if __name__ == "__main__":
    # This ensures the main() function is called only when the script is executed directly
    # (not when imported as a module).
    main()

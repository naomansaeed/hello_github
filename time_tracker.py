import datetime

def log_session(task, duration_minutes=25):
    """Logs a coding session with a timestamp. A simple way to start a habit."""
    now = datetime.datetime.now()
    end_time = now + datetime.timedelta(minutes=duration_minutes)
    print(f"\n--- Coding Session Log ---")
    print(f"Task: {task}")
    print(f"Started: {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"Planned End: {end_time.strftime('%H:%M')}")
    print(f"Duration: {duration_minutes} minutes")
    print("---------------------------")
    print("Stay focused! You've got this.\n")

if __name__ == "__main__":
    # This runs if you execute the script directly
    task = input("What are you working on? (e.g., 'Learning Git'): ")
    log_session(task)
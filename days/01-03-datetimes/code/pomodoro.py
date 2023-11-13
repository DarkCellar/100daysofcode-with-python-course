from datetime import datetime, timedelta
import time

POMODORO_INTERVAL = 25


def main():
    start_time = datetime.now()
    print(f"Starting timer at {start_time}")
    print()
    pomodoro_count(start_time)
    return


def pomodoro_count(start):
    duration = timedelta(minutes=POMODORO_INTERVAL)

    for t in range(duration.seconds + 1):
        current_increment = start + timedelta(seconds=1)
        print("\r", f"Elapsed time: {format_counter(t)} m:s", end="")
        # print(f"Elapsed time: {t} seconds")
        time.sleep(1)

    print()
    print(f"Stopping timer at {datetime.now()}")


def format_counter(seconds):
    return f"{int(seconds/60)}:{int(seconds % 60)}"


if __name__ == "__main__":
    main()

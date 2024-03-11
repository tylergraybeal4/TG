import time
import winsound

def parse_timer_input(timer_input):
    try:
        if ':' in timer_input:
            minutes, seconds = map(int, timer_input.split(':'))
            if seconds < 0 or seconds >= 60:
                raise ValueError
            return minutes * 60 + seconds
        else:
            return int(timer_input)
    except ValueError:
        raise ValueError("Invalid timer input format. Please use 'MM:SS' or 'M' format.")

def countdown_timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timer_display = '\033[91m{:02d}:{:02d}\033[0m'.format(mins, secs)
        print(timer_display, end='\r')
        time.sleep(1)
        duration -= 1
    print('\033[92mBEEP BEEP, ITS TIME FOR SIEGE!\033[0m')
    for _ in range(2): 
        winsound.Beep(500, 200)

def get_timer_duration():
    while True:
        try:
            timer_input = input("So, when Siege?: ")
            duration = parse_timer_input(timer_input)
            if duration <= 0:
                print("Please enter a positive duration.")
            else:
                return duration
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    print("Welcome to the SIEGE CLOCK!")
    duration = get_timer_duration()
    countdown_timer(duration)
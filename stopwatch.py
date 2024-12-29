import time

def stopwatch():
    print("Press Enter to start and CTRL + C to stop the watch.\n")
    input()
    start_time = time.time()
    try: 
        while True:
            current_time = time.time() - start_time
            print(f"Time : {current_time:.2f} seconds", end = '\r')
    except KeyboardInterrupt:
        print("Stopwatch stop !\n")
        total_time = time.time() - start_time
        print(f"Total time : {total_time:.2f} seconds")

stopwatch()
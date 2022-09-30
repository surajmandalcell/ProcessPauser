import os
from time import sleep
import psutil
from rich.console import Console

console = Console()


def main():
    while True:
        try:
            console.print("------------x------------")
            pid = input("Enter pid to pause: ")
            pid_int = int(pid)
            console.print("Pausing process: ", pid_int)
            p = psutil.Process(pid_int)
            p.suspend()

            # Wait for user input to resume process
            input("Press any key to resume process: ")
            console.print("Resuming process: ", pid_int)
            p.resume()
        except KeyboardInterrupt:
            os.system("cls")
            console.print("\nExiting...")
            sleep(2)
            break


if __name__ == "__main__":
    main()

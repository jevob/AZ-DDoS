import sys
import time
import os
from threading import Thread


class AZtheme:
    # ANSI escape sequences for colors and styles
    # Standard colors
    BLACK = '\033[30m'
    RED_DARK = '\033[31m'
    GREEN_DARK = '\033[32m'
    YELLOW_DARK = '\033[33m'
    BLUE_DARK = '\033[34m'
    MAGENTA_DARK = '\033[35m'
    CYAN_DARK = '\033[36m'
    WHITE_DARK = '\033[37m'

    # Bright colors
    BLACK_BRIGHT = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

    # Styles
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'

    @classmethod
    def clear(cls):
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def banner(cls):
        """Displays a program banner."""
        print(f"""{cls.PURPLE}{cls.BOLD}
    ╔═╗╔═╗╔╦╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
    ╠═╝╠═╣║║║║║║║ ║╚═╗ ║ ╚═╗
    ╩  ╩ ╩╩ ╩╩ ╩╚═╝╚═╝ ╩ ╚═╝{cls.ENDC}
    {cls.BLUE}Advanced Console Interface v1.1{cls.ENDC}
    {cls.RED}Warning: Authorized Access Only{cls.ENDC}
        """)

    @classmethod
    def input(cls, prompt):
        """Displays a styled input prompt."""
        sys.stdout.write(f"{cls.CYAN}{cls.BOLD}[INPUT] {prompt}{cls.ENDC}")
        return input()

    @classmethod
    def error(cls, title, message, fatal=False):
        """Displays a formatted error message."""
        if fatal:
            message = message + " FATAL ERROR. TERMINATING PROCESS."
        print(f"{cls.RED}{cls.BOLD}[{title.upper()}] {message}{cls.ENDC}")

    @classmethod
    def success(cls, title, message):
        """Displays a formatted success message."""
        print(f"{cls.GREEN}{cls.BOLD}[{title}] {message}{cls.ENDC}")

    @classmethod
    def info(cls, title, message):
        """Displays a formatted informational message."""
        print(f"{cls.BLUE}{cls.BOLD}[{title}] {message}{cls.ENDC}")

    @classmethod
    def warning(cls, title, message):
        """Displays a formatted warning message."""
        print(f"{cls.YELLOW}{cls.BOLD}[{title}] {message}{cls.ENDC}")

    @classmethod
    def downloading(cls, filename, speed="512 kbps Max"):
        """Simulates a downloading animation."""
        print(f"{cls.PURPLE}{cls.BOLD}[DOWNLOADING] {filename}{cls.ENDC}", end='', flush=True)
        for i in range(3):
            time.sleep(0.5)
            print(f"{cls.PURPLE}.{cls.ENDC}", end='', flush=True)
        print(f" {cls.GREEN}{cls.BOLD}[COMPLETE]{cls.ENDC}")
        print(f"{cls.PURPLE}[SPEED] {speed}{cls.ENDC}")

    @classmethod
    def loading(cls, task_name, duration=3):
        """Displays a loading animation for a specific task."""
        print(f"{cls.BLUE}{cls.BOLD}[START] {task_name}{cls.ENDC}")

        def animate():
            chars = ['|', '/', '-', '\\']
            for i in range(duration * 4):
                time.sleep(0.25)
                sys.stdout.write(f"\r{cls.BLUE}[PROCESSING] {chars[i % 4]}{cls.ENDC}")
                sys.stdout.flush()
            sys.stdout.write(f"\r{cls.GREEN}[COMPLETE] {task_name}{cls.ENDC}\n")

        t = Thread(target=animate)
        t.start()
        t.join()

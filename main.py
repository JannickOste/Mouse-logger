import sys
from models.configuration import Configuration
from services.mouseLoggingService import MouseLoggingService


class Main:
    __config: Configuration = None
    __service: MouseLoggingService = None

    def __init__(self):
        self.__config = Configuration(
            minDistance=10,
            maxMoveDelay=150 * 1_000_000,
            maxTrainingQueueSize=5000
        )

        self.__service = MouseLoggingService(self.__config)

    def __call__(self, *args, **kwargs):
        try:
            self.__service.start_logging()
        except SystemExit:
            sys.exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit()


if __name__ == "__main__":
    (Main())()

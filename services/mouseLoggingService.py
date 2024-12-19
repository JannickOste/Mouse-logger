import time
import math
from datetime import datetime
from pynput.mouse import Controller
from models.mouseEntry import MouseEntry
from models.mouseMovement import MouseMovement
from serializers.mouseMovementCollectionSerializer import MouseMovementCollectionSerializer
from models.configuration import Configuration


class MouseLoggingService:
    def __init__(self, config: Configuration):
        self.__config = config
        self.__mouse = Controller()
        self.__serializer = MouseMovementCollectionSerializer()

    def start_logging(self):
        current_movement_data: list[MouseEntry] = []
        training_input_collections: list[MouseMovement] = []

        last_move_time: int = time.time_ns()
        last_position: tuple[int, int] = self.__mouse.position
        start_position: tuple[int, int] = None

        try:
            while True:
                move_delay = (time.time_ns() - last_move_time)
                current_position = self.__mouse.position

                # Check for new movement
                if current_position != last_position:
                    distance = math.sqrt((current_position[0] - last_position[0])**2 +
                                         (current_position[1] - last_position[1])**2)
                    if distance >= self.__config.minDistance:
                        entry = MouseEntry(
                            current_position,
                            move_delay
                        )
                        if start_position is None:
                            start_position = current_position

                        last_move_time = time.time_ns()
                        last_position = current_position
                        current_movement_data.append(entry)

                # Check if the movement data exceeds the max delay
                if (time.time_ns() - last_move_time) > self.__config.maxMoveDelay and len(current_movement_data):
                    end_position = current_movement_data[-1].position
                    training_input_collections.append(MouseMovement(
                        start_position,
                        end_position,
                        current_movement_data.copy()
                    ))
                    current_movement_data.clear()
                    start_position = None
                    print(self.__log_entry_added())

                # Check stack size
                if len(training_input_collections) >= self.__config.maxTrainingQueueSize:
                    self.__flush_data(training_input_collections)

        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Writing remaining data...")
            self.__flush_data(training_input_collections, force=True)

    def __flush_data(self, training_input_collections: list[MouseMovement], force: bool = False):
        """Flush data to the serializer."""
        if training_input_collections or force:
            self.__serializer(training_input_collections.copy())
            training_input_collections.clear()
        else:
            print("No data to write.")

    def __log_entry_added(self):
        """Generate log message for entry addition."""
        current_datetime = datetime.now().strftime("%H:%M:%S") + f":{datetime.now().microsecond // 1000:03d}"
        return f"[{current_datetime}]: Entry added"

from .mouseEntry import MouseEntry

class MouseMovement:
    """
    Represents a collection of mouse movements between a start and an end position.

    Attributes:
        start (tuple[int, int]): The (x, y) coordinates of the starting position.
        end (tuple[int, int]): The (x, y) coordinates of the ending position.
        entries (list[MouseEntry]): A list of MouseEntry objects representing the steps taken during the movement.
    """

    def __init__(self, start: tuple[int, int], end: tuple[int, int], entries: list[MouseEntry]):
        """
        Initializes a MouseMovement object.

        Args:
            start (tuple[int, int]): The (x, y) coordinates of the starting position.
            end (tuple[int, int]): The (x, y) coordinates of the ending position.
            entries (list[MouseEntry]): A list of MouseEntry objects representing the movement entries.
        """
        self.__start = start
        self.__end = end
        self.__entries = entries

    @property
    def entries(self) -> list[MouseEntry]:
        """
        Gets the list of mouse movement entries.

        Returns:
            list[MouseEntry]: A list of MouseEntry objects.
        """
        return self.__entries

    @property
    def start(self) -> tuple[int, int]:
        """
        Gets the starting position of the mouse movement.

        Returns:
            tuple[int, int]: The (x, y) coordinates of the starting position.
        """
        return self.__start

    @property
    def end(self) -> tuple[int, int]:
        """
        Gets the ending position of the mouse movement.

        Returns:
            tuple[int, int]: The (x, y) coordinates of the ending position.
        """
        return self.__end

    def to_dict(self) -> dict:
        """
        Converts the MouseMovement object into a dictionary representation.

        Returns:
            dict: A dictionary with `start`, `end`, and `entries` as keys.
        """
        return {
            "start": self.__start,
            "end": self.__end,
            "entries": [entry.to_dict() for entry in self.__entries],
        }

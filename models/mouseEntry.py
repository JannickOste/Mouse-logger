class MouseEntry:
    """
    Represents a single entry of mouse movement data.

    Attributes:
        position (tuple[int, int]): The position of the mouse on the screen as (x, y) coordinates.
        delaySinceMove (int): The time delay in nanoseconds since the last mouse movement.
    """

    def __init__(self, position: tuple[int, int], delaySinceMove: int):
        """
        Initializes a MouseEntry object.

        Args:
            position (tuple[int, int]): The (x, y) coordinates of the mouse position.
            delaySinceMove (int): The time delay in nanoseconds since the last mouse movement.
        """
        self.__position = position
        self.__delaySinceMove = delaySinceMove

    @property
    def position(self) -> tuple[int, int]:
        """
        Gets the mouse position.

        Returns:
            tuple[int, int]: The (x, y) coordinates of the mouse position.
        """
        return self.__position

    @property
    def delaySinceMove(self) -> int:
        """
        Gets the time delay since the last mouse movement.

        Returns:
            int: The time delay in nanoseconds since the last mouse movement.
        """
        return self.__delaySinceMove

    def to_dict(self) -> dict:
        """
        Converts the MouseEntry object into a dictionary representation.

        Returns:
            dict: A dictionary with `position` and `delaySinceMove` as keys.
        """
        return {
            "position": self.__position,
            "delaySinceMove": self.__delaySinceMove,
        }

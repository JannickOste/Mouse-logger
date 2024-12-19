class Configuration:
    """
    Configuration class for mouse movement data collection.

    This class holds the configuration values used to determine the conditions 
    for recording and saving mouse movement data, such as minimum movement 
    distance, maximum delay between movements, and the maximum size of the training queue.
    """

    __minDistance: int = None
    __maxMoveDelay: int = None
    __maxTrainingQueueSize: int = None

    def __init__(
        instance: "Configuration",
        minDistance: int,
        maxMoveDelay: int,
        maxTrainingQueueSize: int
    ):
        """
        Initialize the Configuration object.

        :param minDistance: The minimum distance required between consecutive moves (in pixels).
        :param maxMoveDelay: The maximum delay allowed between moves (in nanoseconds).
        :param maxTrainingQueueSize: The maximum size of the training data queue (number of entries).
        """
        instance.__minDistance = minDistance
        instance.__maxMoveDelay = maxMoveDelay
        instance.__maxTrainingQueueSize = maxTrainingQueueSize

    @property
    def minDistance(
        instance: "Configuration"
    ) -> int:
        """
        Get the minimum distance required between moves.

        :return: Minimum distance in pixels.
        """
        return instance.__minDistance

    @property
    def maxMoveDelay(
        instance: "Configuration"
    ) -> int:
        """
        Get the maximum delay allowed between moves.

        :return: Maximum delay in nanoseconds.
        """
        return instance.__maxMoveDelay

    @property
    def maxTrainingQueueSize(
        instance: "Configuration"
    ) -> int:
        """
        Get the maximum allowed size of the training data queue.

        :return: Maximum number of entries in the training queue.
        """
        return instance.__maxTrainingQueueSize

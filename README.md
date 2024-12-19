# Mouse Logger for Brain.js Training Data

This project is a **Mouse Logger** designed to collect and serialize mouse movement data for training machine learning models using [Brain.js](https://brain.js.org/). The collected data can be used to build models that analyze or predict mouse movement patterns.

## Features

- Tracks and logs mouse movements, including positions and delays.
- Converts raw mouse data into a structured format (`MouseEntry`, `MouseMovement`, `TrainingDataCollection`).
- Configurable parameters for movement thresholds and queue size.
- Serializes training data for use in machine learning models.
- Handles graceful shutdown on interruption, ensuring no data is lost.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mouse-logger.git
   cd mouse-logger
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > Note: Ensure you have Python 3.9 or higher installed.

3. Install the required system libraries for `pynput` if needed (refer to the [pynput documentation](https://pynput.readthedocs.io/)).

## Usage

1. Run the logger:
   ```bash
   python main.py
   ```

2. The logger will start tracking mouse movements in real time. It will:
   - Log movements exceeding the configured distance threshold.
   - Group movements into training collections based on a timeout.
   - Serialize the training data when the queue reaches the configured size.

3. Stop the logger using `Ctrl + C`. The logger will save any remaining data before exiting.

## Configuration

The behavior of the logger is controlled by the `Configuration` class, which includes:

- **`minDistance`**: The minimum distance (in pixels) a mouse must move to be recorded.
- **`maxMoveDelay`**: The maximum allowable delay (in nanoseconds) between movements.
- **`maxTrainingQueueSize`**: The maximum number of entries in a single training data file.

You can modify these values in the `main.py` file:

```python
self.__config = Configuration(
    minDistance=10,                    # Minimum distance in pixels
    maxMoveDelay=150 * 1_000_000,      # Max delay in nanoseconds
    maxTrainingQueueSize=5000          # Max queue size
)
```

## Data Format

### MouseEntry
- **`position`**: `(x, y)` coordinates of the mouse.
- **`delaySinceMove`**: Delay (in nanoseconds) since the last movement.

### MouseMovement
- **`start`**: Starting position of the movement.
- **`end`**: Ending position of the movement.
- **`entries`**: List of `MouseEntry` objects within the movement.

### TrainingDataCollection
- A collection of `MouseMovement` objects.

### Serialized Output
The serialized data is stored in JSON format, ready to be fed into Brain.js for training.

## Example Output

```json
[
  {
    "start": [100, 200],
    "end": [150, 250],
    "entries": [
      {"position": [100, 200], "delaySinceMove": 12000000},
      {"position": [120, 220], "delaySinceMove": 15000000},
      {"position": [150, 250], "delaySinceMove": 18000000}
    ]
  }
]
```

## Dependencies

- Python 3.9 or higher
- `pynput` for mouse tracking
- Any additional dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! If you find a bug or have a feature request, fork the repository, create a new branch and submit a merge request. 

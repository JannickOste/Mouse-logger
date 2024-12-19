import os
import json
from datetime import datetime
from typing import List
from models.mouseMovement import MouseMovement

class MouseMovementCollectionSerializer:
    def __call__(self, training_data: List[MouseMovement]) -> None:
        serialized_data = self.__serialize(training_data)
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"data/{current_datetime}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as json_file:
            json.dump(serialized_data, json_file, indent=4)
        print(f"Data written to {filename}")

    def __serialize(self, training_data: List[MouseMovement]) -> List[dict]:
        """Convert the training data into a serializable format."""
        return [collection.to_dict() for collection in training_data]

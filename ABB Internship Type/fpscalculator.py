import time
from collections import deque

"""
Given a stream of inference timestamps (e.g., when each image is processed), calculate the moving average FPS in real-time.
Frame compute: FPS = Frames / Time elapsed
"""

def update_fps(timestamps = None):
    final_timestamps = []
    if timestamps is None:
        timestamps = time.time()
    final_timestamps.append(timestamps)

    if len(timestamps) < 2:
        return 0.0

    elapsed = timestamps[-1] - timestamps[0]
    return len(final_timestamps)-1 / elapsed

timestamps = [0.00, 0.05, 0.10, 0.15,0.20,0.25,0.50]
print(f" FPS: {update_fps(timestamps)}")




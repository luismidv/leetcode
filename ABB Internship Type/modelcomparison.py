"""
Write a utility to profile model inference (measure latency, average, and standard deviation) in real-time.
Useful for checking if a vision model meets real-time constraints on a robot (e.g., 30 FPS).
"""

import time
import statistics
import torch
from torch import device


def profiler_python(model, input_data, runs = 10):
    latencies = []

    #HERE YOU CAN DO A WARM UP RUN BEFORE RUNNING THE MODEL TO GET STATS

    for i in range(runs):
        start = time.time()
        _ = model(input_data)
        end = time.time()
        latencies.append((end-start)*1000)

    avg = statistics.mean(latencies)
    std = statistics.stdev(latencies)
    fps = 1000/avg #WE CALCULATING FRAMES PER SECOND 1SECOND -> 1000MS

    return (avg, std, fps)

"""
NOW WE ARE GOING TO USE CUDA SYNCHRONIZE. SINCE USING TIME.TIME ONLY MEASURES HOW LONG IT TOOK TO QUEUE THE OPERATION
NOT THE GPU LAUNCH OF THE MODEL.
USING CUDA.SYNCHRONIZE MEASURES HOW LONG THE GPU TOOK TO LAUNCH THE PREVIOUS ACTION
"""
def profiler_pytorch(model, input_data, runs = 10):
    latencies = []

    #GPU WARM UP
    with torch.no_grad():
        _ = model(input_data)

    for i in range(runs):
        torch.cuda.synchronize() if device == "GPU" else None
        start = time.time()

        with torch.no_grad():
            _ = model(input_data)
        torch.cuda.synchronize() if device == "GPU" else None
        end = time.time()
        latencies.append((end-start)*1000)

    avg = statistics.mean(latencies)
    std = statistics.stdev(latencies)
    fps = 1000/avg
    return (avg, std, fps)



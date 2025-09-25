"""
Sliding Window Maximum
Problem: Given an array of sensor readings, return the maximum reading in each sliding window of size k.
Relevance: Efficiently handling sensor streams.
"""
import time
#SLOW APPROACH O(N*K)

def slow_sliding_windows(readings, k):
    for num in range(len(readings)-k):
        sub_array = readings[num:num+k]
        max_window = max(sub_array)


from collections import deque


def fast_sliding_windows(nums: list[int], k: int) -> list[int]:
    if not nums or k == 0:
        return []

    dq = deque()  # stores indices
    res = []

    for i in range(len(nums)):
        # Remove indices that are out of this window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing order in deque
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Record the max (front of deque) once window size is reached
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

numbers = [3,3,-1,-5, 0, 2, 5, -3]
initial_slow = time.time()
slow_sliding_windows(numbers,3)
final_slow = time.time()

initial_fast = time.time()
fast_sliding_windows(numbers,3)
final_fast = time.time()


print(f"Supposed slow approach {final_slow - initial_slow}")
print(f"Supposed fast approach {final_fast - initial_fast}")
print(f"Total time: {(final_fast - initial_fast) - (final_slow - initial_slow)}")
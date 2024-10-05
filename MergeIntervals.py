def merge_intervals(intervals):
    # If the list of intervals is empty, return an empty list
    if not intervals:
        return []

    # Sort intervals by the start value
    intervals.sort(key=lambda x: x[0])

    # Initialize a list to hold merged intervals
    merged = [intervals[0]]

    # Traverse the intervals
    for i in range(1, len(intervals)):
        # Get the last merged interval
        last_merged = merged[-1]
        
        # If the current interval overlaps with the last merged interval
        if intervals[i][0] <= last_merged[1]:
            # Merge the intervals by updating the end of the last merged interval
            last_merged[1] = max(last_merged[1], intervals[i][1])
        else:
            # Otherwise, add the current interval to the merged list
            merged.append(intervals[i])

    return merged


# Example case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Get the result
result = merge_intervals(intervals)

# Print the result
print("Merged Intervals:", result)

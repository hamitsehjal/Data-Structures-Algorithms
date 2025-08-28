# Intervals

1. How to find overlapping intervals
	- sort the intervals by start time
	- compare the start_time with previous end_time
2. Merge Overlapping intervals
3. Insert a new interval
4. Non-Overlapping Intervals
	- sort the intervals by end_time (greedy approach)
	- we always pick the interval that finishes first, so gives us more room for other later
	- Keep track of end and the skip the one's where `intervals[i][0] < end `
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjE0NjI0MDc0NywtMzk1Mzk2MzcxXX0=
-->
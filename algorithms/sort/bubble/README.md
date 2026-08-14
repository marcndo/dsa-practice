# Bubble sort

## How it works
This is based on 0-index array

We find the largest element in the array and push it the last position of the array(n-1), then the second largest element and push it to the second to the last position((n-1)-1), then the third, fouth till the entire array is sorted.

## Why it works
[See prof](proof.md)

## Time and space complexity

### Space complexity
The operation is simply a permutation of the elements in the original array.No new space is created that grows as the array size grows. Thus the space complexity is constant(O(1)).

### Time Complexity
Following similar analysis in [insertion sort](../insertion/README.md), the time complexity is O(n^2) where n is the size of the given array.
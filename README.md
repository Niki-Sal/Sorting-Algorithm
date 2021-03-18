## Introduction to Sorting
- Types of sorting: comparison sort & Distribution Sort
- sorting can be stable or unstable

- Time complexity: O(1) O(log(N)) O(N) O(N**2) O(N!)
- Space complexity: In place: O(1) or O(log(N)) , Out of place: O(N) O(N**2) 

#### considration before choosing sorting algorithm:
- time and space complexity
- stability
- sorting method (comparison or distribution or combination of both)
- the size and sturture of data 

![Image 1](assets/sorting-algorithms.png)

## Basic Sorting Algorithms
- Bubble sort: put values in order by iterating through a data set and comparing neighboring numbers. The sort continues through the data set, value by value, swapping them until the array is properly sorted. until you can go through the whole list without making any swaps.
- Insertion Sort: an insertion sort takes each item and inserts it into the right place in the array. faster than bubble sort and works more efficiently in a wider variety of circumstances. But still not that efficient.

## Divide-and-Conquer Sorting Algorithms
- Both merge sort and quick sort use divide and conquer sorting and solve problem with recursion: repeating, dividing, sorting until data is sorted

#### Merge sort - O(N log(N))
- It takes an array and splits it in half over and over again until it’s small and sorted (there’s the divide part). Then, it merges small sorted pieces together on their way back up (that’s how it conquers)
###### has two algorithms: 
- merge sort algorithm: Split the array in half until you can’t anymore (aka, divide) - Recursion is used here. Merge sort algorithm divides arrays until they’re down to single-item arrays but does not check to see if those arrays are sorted. 0(log(N))

- merge algorithm: Merge those pieces back together (aka, conquer). he merge algorithm is not recursive. O(N)

#### Quick sort - O(N**2)!!
- Merge sorts divide an array into two pieces, while quick sorts divide an array into three parts: pivot, left partition(containing numbers lower than the pivot), right partition (containing numbers higher than the pivot)
- It’s conventional to use either the first or last value in an array as the pivot
- Quick sort gets tripped up on data sets with very similar values.


![Image 1](assets/quick-vs-merge.png)

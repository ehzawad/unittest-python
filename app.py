from helper import getNextGap

def combSort(arr):
    n = len(arr)

    # Initialize gap
    gap = n

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap !=1 or swapped == 1:

        # Find next gap
        gap = int(getNextGap(gap))

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # print(n, gap)
        # Compare all elements with current gap
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True


    return arr


# Driver code to test above
# arr = [ 8, 4, 1, 3, -44, 23, -6, 28, 0]
# combSort(arr)

# print ("Sorted array:")
# for i in range(len(arr)):
#     print (arr[i]),

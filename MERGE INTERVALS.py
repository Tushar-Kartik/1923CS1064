def merge(intervals): #O(nlogn)
    intervals.sort()
    output=[intervals[0]]  #putting first element to tackle corner case

    for start , end in intervals[1:]:
        lastend=output[-1][1]

        if start<= lastend:
            output[-1][1]=max(lastend,end)
        else:
            output.append([start,end])
    return output

intervals=[[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

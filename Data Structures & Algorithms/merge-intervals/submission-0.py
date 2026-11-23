class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0][:]] # put the first interval in the output

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # Option 1: Extend previous interval end
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd)
            else: 
                # Option 2: Append non-overlapping intervla
                output.append([start, end])
        
        return output
        
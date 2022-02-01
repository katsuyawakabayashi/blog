class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        restRows = numRows - 1
        
        # rest rows
        for i in range(restRows):
            prevRow = res[-1]
            # inserting 0 to both sides
            # res[-1] refers to the latest array added
            tempRow = [0] + prevRow + [0]
            newRow = []
            
            # generating new row
            # new row has (prev row + 1) row
            for j in range(len(prevRow) + 1):
                newRow.append(tempRow[j] + tempRow[j+1])
            res.append(newRow)
            
        return res

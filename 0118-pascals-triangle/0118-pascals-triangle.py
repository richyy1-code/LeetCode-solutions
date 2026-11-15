class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
                return [[1],[1,1]]
        else:
            result = [[1],[1,1]]
            for i in range(numRows-2):
                cur_list = []
                pre_list = result[-1]
                for i in range(len(pre_list)+1):
                    if i == 0 or i == len(pre_list):
                        cur_list.append(1)
                    else:
                        cur_list.append(pre_list[i-1] + pre_list[i])
                result.append(cur_list)
            return result

                    
                
            return result
            

            

    
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_dict = {num: i for i, num in enumerate(arr2)}
        arr1_index = []
        arr1_special = []
        
        for j in arr1:
            if j in arr2:
                arr1_index.append(index_dict[j])
            else:
                arr1_special.append(j)
                
        arr1 = [j for j in arr1 if j not in arr1_special]
        
        result_arr1 = [x for y, x in sorted(zip(arr1_index, arr1))]
                
        return result_arr1 + sorted(arr1_special)
            
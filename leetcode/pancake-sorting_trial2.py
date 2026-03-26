class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        result = []
        while i >= 0:
            # print(i)
            # print(arr)
            val = max(arr[0: i + 1])
            idx = arr[0: i + 1].index(val)
            if idx == i:
                None

            elif idx == 0:
                new_arr = list(reversed(arr[0:(i + 1)]))
                arr = new_arr + arr[i + 1: ]
                # print("here 1")
                result.append(i + 1)

            else:
                #first flip 
                new_arr = list(reversed(arr[0:(idx + 1)]))
                arr = new_arr + arr[idx + 1:]
                result.append(idx + 1)

                new_arr = list(reversed(arr[0:(i + 1)]))
                arr = new_arr + arr[i + 1: ]
                result.append(i + 1)

            i -= 1

        return(result)
#!/usr/bin/env python


class Quanpailie(object):
    def __init__(self):
        pass
    
    def solver(self, in_array, out_array):
        if len(in_array) == 0:
            print out_array
            return
        for i in range(len(in_array)):
            new_out_array = out_array + [in_array[i]]
            # mei ceng xun huan dou yao ding yi yige xin de neicun lie biao bian liang
            # ru ruo yong xiamian de append fang fa,meici de hui shuoxun huan dou shi zhui jia
            # xie le
            #out_array.append(in_array[i])
            new_in_array = in_array[:i] + in_array[i+1:]
            self.solver(new_in_array, new_out_array)

    def solver2(self, count):
        if count == 3:
            print result

        for i in range(3):
            if used[i] == 0:
                used[i] = 1
                result[count] = test_array[i]
                self.solver2(count + 1)
                used[i] = 0


inst = Quanpailie()
test_array = ['a', 'b', 'c']
inst.solver(test_array, [])

test_array = ['a', 'b', 'c']

result = [0] * len(test_array)
used = [0] * len(test_array)
inst.solver2(len(test_array))
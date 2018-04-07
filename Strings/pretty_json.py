""" Problem statement:
https://www.interviewbit.com/problems/pretty-json/
"""


class Solution:
    # @param A : string
    # @return a list of strings
    def pretty_json(self, data):
        """ Time complexity: O(n). Space complexity: O(n), n is len(data).
        """
        indent = 0  # indent in tabs
        tab = chr(9)
        result = []
        curr = []  # current string
        for char in data:
            if char == "{" or char == "[":
                if curr:  # if there's something to add
                    curr = tab * indent + "".join(curr)
                    result.append(curr)
                result.append(tab * indent + char)
                indent += 1
                curr = []
            elif char == ",":
                if curr:  # if there's something to add
                    curr = tab * indent + "".join(curr) + char
                    result.append(curr)
                    curr = []
                else:  # add "," to the last bracket
                    result[-1] += ","
            elif char == "}" or char == "]":
                if curr:
                    curr = tab * indent + "".join(curr)
                    result.append(curr)
                    curr = []
                indent -= 1
                result.append(tab * indent + char)
            elif char == " ":  # skip spaces in the input string
                continue
            else:
                curr.append(char)
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.pretty_json

    data1 = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
    data2 = '["foo", {"bar":["baz",null,1.0,2]}]'
    data3 = '{"id":100,"firstName":"Jack","lastName":"Jones","age":12}'
    data4 = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},\
             "vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":\
             "SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,\
             "Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map",\
             "status":"SUCCESS","lmd":41962}]}'

    for data in [data1, data2, data3, data4]:
        print("-" * 30)
        print(data)
        print("-" * 15)
        result = func(data)
        for line in result:
            print(line)
        print("-" * 30)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for c in tokens:
            if c == '+':
                nums.append(nums.pop() + nums.pop())
            elif c == '-':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num2 - num1)
            elif c == '*':
                nums.append(nums.pop() * nums.pop())
            elif c == '/':
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num2/num1))
            else:
                nums.append(int(c))
            
        return nums[0]


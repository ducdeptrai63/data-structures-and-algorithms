from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_vals = []

        for token in tokens:
            if token not in '+-*/':
                stack_vals.append(int(token))
            else:
                l = stack_vals.pop()
                r = stack_vals.pop()

                if token == '+':
                    stack_vals.append(r + l)
                elif token == '-':
                    stack_vals.append(r - l)
                elif token == '*':
                    stack_vals.append(r * l)
                else:
                    stack_vals.append(int(r / l))

        return stack_vals[-1]

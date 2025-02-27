class Solution:
    def isValid(self, s: str) -> bool:
        # Define lists of opening and closing brackets
        open_bracket: list[str] = "([{"
        close_bracket: list[str] = ")]}"

        # List of lists to store indices of brackets in the input string
        oc_b: list[list[int]] = [[], [], [], [], [], []]

        #List to check if there is single bracket in pairs bracket
        s_pairs = [0] * len(s)

        # First check: Ensure each type of bracket has an equal number of opening and closing brackets
        for idx, c in enumerate(open_bracket):
            if s.count(c) == s.count(close_bracket[idx]):
                continue  # If counts match, continue checking the next bracket type
            else:
                return False  # If counts mismatch, the string is invalid

        # Store indices of each bracket type
        for idx, c in enumerate(s):
            if c == open_bracket[0]:
                oc_b[0].append(idx)  # Store index of '('
                s_pairs[idx] = 1
            elif c == open_bracket[1]:
                oc_b[1].append(idx)  # Store index of '['
                s_pairs[idx] = 1
            elif c == open_bracket[2]:
                oc_b[2].append(idx)  # Store index of '{'
                s_pairs[idx] = 1
            elif c == close_bracket[0]:
                oc_b[3].append(idx)  # Store index of ')'
                s_pairs[idx] = -1
            elif c == close_bracket[1]:
                oc_b[4].append(idx)  # Store index of ']'
                s_pairs[idx] = -1
            elif c == close_bracket[2]:
                oc_b[5].append(idx)  # Store index of '}'
                s_pairs[idx] = -1

        # Second redundant check: Ensure each bracket type has equal occurrences
        for idx, c in enumerate(open_bracket):
            if s.count(c) == s.count(close_bracket[idx]):
                continue
            else:
                return False

        #Pcheck if there is single bracket in pairs bracket
        for i in range(3):
            if not oc_b[i] or not oc_b[i + 3]:
                continue  # Skip this bracket type if it's missing
            if sum(s_pairs[oc_b[i][0]:oc_b[i + 3][-1] + 1]) == 0:
                continue
            else:
                return False

        return True  # If all checks pass, return True

input1 = "(})"  # Expected: True "()"
s1 = Solution.isValid(Solution, input1)
print(f"s1 {s1}")

input2 = "(()[]{})"  # Expected: True "(()[]{})"
s2 = Solution.isValid(Solution, input2)
print(f"s2 {s2}")

input3 = "(]"  # Expected: False "(]"
s3 = Solution.isValid(Solution, input3)
print(f"s3 {s3}")

input4 = "a[v(cc{d})ee]f"  # Expected: True "({}{})"
s4 = Solution.isValid(Solution, input4)
print(f"s4 {s4}")
#["a[v(cc{d})ee]f", "a[b]c]d[e", "ad({dfd[g}bv]bv)", "(nv[]nv})vnv", "(v][n)mm", "(c([bc] ])nn{}[)", "[t(y])"]

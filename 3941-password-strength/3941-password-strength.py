class Solution:
    def passwordStrength(self, password: str) -> int:
        password = set(password)
        total = 0
        for char in password:
            if char.isupper():
                total += 2
            elif char.islower():
                total += 1
            elif char.isdigit():
                total += 3
            else:
                total += 5
        return total

        
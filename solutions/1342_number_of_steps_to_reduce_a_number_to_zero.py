class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps_count = 0

        current_num = num
        while current_num != 0:
            current_num = current_num / 2 if current_num % 2 == 0 else current_num - 1
            steps_count += 1

        return steps_count

    # def numberOfSteps(self, num: int) -> int:
    #     if num == 0:
    #         return 0
    #
    #     return num.bit_length() - 1 + num.bit_count()

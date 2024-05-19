class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account_amounts) for account_amounts in accounts])

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = (purchaseAmount // 10 + 1) * 10
        return 100 - roundedAmount
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        roundedAmount = (purchaseAmount + 5) // 10 * 10
        return 100 - roundedAmount

The function first calculates the roundedAmount by adding 5 to purchaseAmount, dividing the result by 10 and then multiplying by 10. This ensures that the roundedAmount is the nearest multiple of 10 to purchaseAmount. 

Then, the function subtracts roundedAmount from 100 to get the new account balance after the purchase. Finally, it returns this balance.
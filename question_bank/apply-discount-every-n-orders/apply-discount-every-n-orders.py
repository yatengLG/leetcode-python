# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：172 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：20.3 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    Cashier __init__ 中，
        使用字典保存商品及其价格
        初始化顾客计算为0，为保持计数数值不超预期，计数数值保存当前顾客/3的余数
    getBill 中，
        顾客数累加，并更新
        计算是否该打折
        从商品字典中获取商品对应价格并计算总价
"""
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products_prices_dict = dict(zip(products, prices))

        self.num = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.num = (self.num + 1) % self.n
        price = 0
        for prod, amou in zip(product, amount):
            price += self.products_prices_dict[prod] * amou
        if self.num == 0:
            price = price - self.discount / 100 * price

        return price

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
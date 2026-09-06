class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            previous_price, previous_span = self.stack.pop()
            span += previous_span

        self.stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
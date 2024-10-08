class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur+1]
        self.history.append(url)
        self.cur += 1
        

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur-steps)
        return self.history[self.cur]
        

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.history)-1, self.cur+steps)
        return self.history[self.cur]
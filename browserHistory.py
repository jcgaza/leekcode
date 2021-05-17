class BrowserHistory:
  def __init__(self, homepage: str):
    self.currentIndex = 0
    self.urls = [homepage]
      

  def visit(self, url: str) -> None:
    self.urls = self.urls[:self.currentIndex+1]
    self.urls.append(url)
    self.currentIndex = len(self.urls)-1

      

  def back(self, steps: int) -> str:
    print("current:", self.currentIndex)
    if steps > self.currentIndex:
      self.currentIndex = 0
    else:        
      self.currentIndex -= steps
    
    return self.urls[self.currentIndex]

  def forward(self, steps: int) -> str:
    print(steps, self.currentIndex)
    if steps > len(self.urls)-self.currentIndex-1:
      self.currentIndex = len(self.urls)-1
    else:
      self.currentIndex += steps
    
    return self.urls[self.currentIndex]

ans = []
browserHistory = BrowserHistory("zav.com")
ans.append(None)
ans.append(browserHistory.visit("kni.com"))       # You are in "leetcode.com". Visit "google.com"
ans.append(browserHistory.back(7))                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
ans.append(browserHistory.back(7))                   # You are in "facebook.com", move back to "google.com" return "google.com"
ans.append(browserHistory.forward(5))                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
ans.append(browserHistory.forward(1))                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
ans.append(browserHistory.visit("pwrrbnw.com"))     # You are in "facebook.com". Visit "linkedin.com"
ans.append(browserHistory.visit("mosohif.com"))     # You are in "facebook.com". Visit "linkedin.com"
ans.append(browserHistory.back(9))                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

print(ans)
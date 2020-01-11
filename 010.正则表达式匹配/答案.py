class Solution(object):
  def isMatch(self, s, p):
    """
    :s类型: str
    :p类型: str
    :返回类型: bool
    """
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(1, len(p) + 1):
      if p[j - 1] == "*":
        dp[0][j] = dp[0][j - 2]

    for i in range(1, len(s) + 1):
      for j in range(1, len(p) + 1):
        if p[j - 1] != "*":
          dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
        else:
          dp[i][j] = dp[i][j - 2] or dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == ".")
    return dp[-1][-1]
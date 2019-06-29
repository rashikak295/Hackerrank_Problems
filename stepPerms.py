def stepPerms(n):
    memo = [0 for i in range(n)]
    return stepPerms2(n,memo)
def stepPerms2(n,memo):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    elif memo[n-1]==0:
        memo[n-1] = stepPerms2(n-1,memo)+stepPerms2(n-2,memo)+stepPerms2(n-3,memo)
    return memo[n-1]
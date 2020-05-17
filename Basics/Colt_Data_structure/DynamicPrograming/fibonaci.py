def fibonaci_recursive(n):
    if n == 1:
        return 1
        
    if n == 2:
        return 1

    return (fibonaci_recursive(n-1)+ fibonaci_recursive(n-2))


def fibonaci_memo(n, memo = {}):
    if memo.get(n) is not None:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fibonaci_memo(n-1, memo) + fibonaci_memo(n-2, memo)

    return (fibonaci_memo(n-1, memo) + fibonaci_memo(n-2, memo))

def fibonaci_tabulation(n):
    if( n<= 2 ):
        return 1
    memo = {}
    memo[0] = 0
    memo[1] = 1
    memo [2] = 1
    i = 3

    while i <= n:
        memo[i] = memo[i-1] + memo[i-2]
        i += 1

    return memo[n]



# print(fibonaci_memo(100))
# print(fibonaci_memo(100))
print(fibonaci_tabulation(100)- fibonaci_memo(100))

# print(fibonaci_recursive(100))

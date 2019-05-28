# Using the sieve of eratostheneses we can find prime number in a bounded range, i.e, prime number less than a given number.

class Solution():

    def get_prime_LT_n(self,n):
        #Sieve of Eratosthenes
        n = int(n)
        if n <=1:
            return -1

        if n == 2:
            return 2

        if n > 2:
            nPrime = [2]
            List   = list(range(nPrime[-1], n + 1))
            while nPrime[-1] < List[-1]:
                List   = [n for n in List if n%nPrime[-1]!=0]
                nPrime.append(List[0])
        return nPrime



if __name__ == "__main__":
    n = 3000
    S = Solution()
    nPrime = S.get_prime_LT_n(n)
    print("Prime numbers between 1 and "+repr(n)+" are: \n"+ repr(nPrime) +
          "\nTotal "+ repr(len(nPrime)) + " prime numbers were found")
    #print(repr(n)+"th prime number is: "+repr(S.get_nPrime(n)))

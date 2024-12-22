from functools import lru_cache



# @lru_cache(None)
def kmp_search(sublist, main_list):
    # Preprocess the sublist (pattern) to get the partial match table
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # KMP search algorithm
    m = len(main_list)
    n = len(sublist)

    if n == 0:
        return 0  # An empty sublist is always found at index 0

    lps = compute_lps(sublist)
    i = j = 0  # i for main_list, j for sublist (pattern)

    while i < m:
        if main_list[i] == sublist[j]:
            i += 1
            j += 1

        if j == n:
            return i - j  # Sublist found, return the start index
        elif i < m and main_list[i] != sublist[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1  # Sublist not found



@lru_cache(None)
def mix(n1, n2):
    return n1 ^ n2

@lru_cache(None)
def prune(n1):
    return n1 % 16777216

@lru_cache(None)
def transform(secret, n):
    MOD = 2**24 
    secret_changes = []
    last_secret = None
    for _ in range(n):
        last_secret = secret
        secret = ((secret << 6) ^ secret) % MOD
        secret = (secret ^ (secret >> 5)) % MOD
        secret = ((secret << 11) ^ secret) % MOD   
        secret_changes.append((secret % 10, secret % 10 - last_secret % 10))
    return secret,  secret_changes

def solve(real_input = True):
    sum1 = 0  
    sum2 = 0
    secrets = []
    
   
    with open("day22/input.txt" if real_input else "day22/sample_input.txt", "r") as file:
        secrets = file.read().split("\n")
    _,secret_data = transform(int(123), 10)
    scores = {}
    for secret in secrets:
        current_score,secret_data = transform(int(secret), 2000)
        pointer1 = 0
        pointer2 = 4
        seen = set()
        while pointer2 <= len(secret_data):
            
            potential_change_seq = tuple([i[1] for i in secret_data[pointer1:pointer2]])
            if potential_change_seq in seen:
                pass
            else:
                if potential_change_seq not in scores:
                    scores[potential_change_seq] = secret_data[pointer2-1][0]
                else:
                    scores[potential_change_seq] += secret_data[pointer2-1][0]
            seen.add(potential_change_seq)
            pointer1 += 1
            pointer2 += 1
        sum1 += current_score
    
    sum2 = max(scores.values()) 

   
    return f"Sum 1: {sum1}\nSum 2: {sum2}"
if __name__ == "__main__":
    print(solve(False))
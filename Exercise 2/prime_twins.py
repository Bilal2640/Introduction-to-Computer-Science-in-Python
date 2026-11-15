def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True



def prime_twins(n: int) -> list[tuple[int, int]]:
    twins = []
    candidate = 2
    while len(twins) < n:
        if is_prime(candidate) and is_prime(candidate + 2):
            twins.append((candidate, candidate + 2))
        candidate += 1
    return twins



def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    triplets = []
    candidate = 2
    while len(triplets) < n:
        # Check for triplet form: (p, p+2, p+6) or (p, p+4, p+6)
        p = candidate
        if is_prime(p):
            if is_prime(p + 2) and is_prime(p + 6):
                triplets.append((p, p + 2, p + 6))
            elif is_prime(p + 4) and is_prime(p + 6):
                triplets.append((p, p + 4, p + 6))
        candidate += 1
    return triplets



if __name__ == "__main__":
    print("First 3 Prime Twins:", prime_twins(3))
    print("First 3 Prime Triplets:", prime_triplets(3))
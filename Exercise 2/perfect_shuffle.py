def interleave(a: list[int], b: list[int]) -> list[int]:
    result = []
    for i in range(len(a)):
        result.append(a[i])
        result.append(b[i])
    return result



def perfect_shuffle(deck: list[int]) -> list[int]:
    mid = len(deck) // 2
    left = deck[:mid]
    right = deck[mid:]
    return interleave(left, right)



def shuffle_number(n: int) -> int:
    original = list(range(n))
    current = perfect_shuffle(original)
    count = 1
    
    while current != original:
        current = perfect_shuffle(current)
        count += 1
        
    return count



if __name__ == "__main__":
    # Test interleave
    print("Interleave:", interleave([1, 2, 3], [4, 5, 6]))
    
    # Test perfect_shuffle
    print("Perfect Shuffle:", perfect_shuffle([1, 2, 3, 4, 5, 6]))
    
    # Test shuffle_number for a standard 52-card deck
    print("Shuffle number for 52 cards:", shuffle_number(52))
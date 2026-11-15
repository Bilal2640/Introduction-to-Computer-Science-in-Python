import random



def create_random(n: int) -> list[int]:
    result = []
    for _ in range(n):
        result.append(random.randint(5, 99))
    return result



def to_string(a: list[int]) -> str:
    s = "["
    for i in range(len(a)):
        s += str(a[i])
        if i < len(a) - 1:
            s += ", "
    s += "]"
    return s



def pos_min(a: list[int]) -> int:
    if not a:
        return -1
    min_index = 0
    min_val = a[0]
    for i in range(1, len(a)):
        if a[i] < min_val:
            min_val = a[i]
            min_index = i
    return min_index



def swap(a: list[int]) -> None:
    if len(a) > 1:
        temp = a[0]
        a[0] = a[-1]
        a[-1] = temp
    return None



if __name__ == "__main__":
    arr = create_random(5)
    print("Generated Array:", to_string(arr))
    
    m_idx = pos_min(arr)
    print(f"Smallest value index: {m_idx}")
    
    swap(arr)
    print("After swap:", to_string(arr))
import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    width = 4 * size - 3
    
    for i in range(size):
        s = "-".join(alphabet[i:size])
        row = s[::-1] + s[1:]
        lines.append(row.center(width, "-"))
    
    full_pattern = lines[::-1] + lines[1:]
    for line in full_pattern:
        print(line)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
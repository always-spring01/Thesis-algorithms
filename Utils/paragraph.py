def paragraph():
    string_list = []
    while True:
        raw = input().rstrip()
        if raw == "0":
            break
        string_list.append(raw)
    print(''.join(string_list))

# For Debug
if __name__ == "__main__":
    paragraph()
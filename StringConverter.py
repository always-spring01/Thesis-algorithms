'''
StringConverter with Python3

Author: CHB. Kookmin Univ
Date: 20240724
'''

# Import Modules
import sys



# Main
if __name__ == "__main__":
    str_list = []
    while True:
        string = input()
        if string == '0':
            break
        str_list.append(string)

    print(' '.join(str_list))
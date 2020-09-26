def function(n):
    if n < 10:
        return n
    while True:
        if str(n) == str(n)[::-1]:
            return n
            break
        else:
            n += 1

if __name__ == '__main__':
    restart = ('y')
    while restart == 'y':
        print("Palindromifiaction Method")
        n = int(input("Enter the number of elements : "))
        list = []
        new_list = []
        for i in range(n):
            num = int(input("\nEnter the Numbers : "))
            list.append(num)

            l = function(num)
            new_list.append(l)

        print(f"\nList is {list}")
        print(f"\nPalindromify List is {new_list}")
        restart = input("\nPress y to restart : ").lower()
        if restart != 'y':
            print("Thank You")
            break



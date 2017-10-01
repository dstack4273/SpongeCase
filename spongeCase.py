import re


def spongecase(feedMe):
    swapped = ""
    looper = list(feedMe)
    index = 0

    for i in feedMe:

        if index == 0:
            if i.isupper():
                # print("before increment " + str(index))
                index += 1
                # print("after increment " + str(index))
                swapped += i.lower()
                # print(swapped + " this is the " + str(index) + " loop")

            else:
                swapped += i.upper()
                index += 1
                # print(swapped + " this is the " + str(index) + " loop")
        # elif swapped[index-1].isspace():
        elif bool(re.match('[\W]+$', swapped[index-1])):
            if swapped[index-2].isupper():
                swapped += i.lower()
                index += 1
            else:
                swapped += i.upper()
                index += 1

        elif swapped[index-1].isupper():
            swapped += i.lower()
            index += 1
            # print(swapped + " this is the " + str(index) + " loop")
        else:
            swapped += i.upper()
            index += 1
            # print(swapped + " this is the " + str(index) + " loop")
    return swapped


def main():
    print(spongecase(feeder))


if __name__ == "__main__":
    feeder = str(input('Enter your string to convert to Sponge-Case! '))
    main()

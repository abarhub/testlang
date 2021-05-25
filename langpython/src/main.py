import sys

last = 0


def randomNumber(max):
    global last
    last = (25214903917 * last + 11) % 281474976710656
    if last >= 0:
        tmp = last
    else:
        tmp = -last
    return tmp % max


def createArray(len, maxValue):
    return [randomNumber(maxValue) for x in range(len)]


def main():
    tabSize = 10000000
    maxValue = 5000000
    noOutput = False
    debug = False

    for arg in sys.argv:
        if arg == "--nooutput":
            noOutput = True
        elif arg.startswith("--nbop="):
            n = int(arg[7:])
            if n > 0:
                tabSize = n
        elif arg == "--debug":
            debug = True

    if debug:
        print("lang=c;tabSize=%d;maxValue=%d;noOutput=%d;debug=%d\n" %
              (tabSize, maxValue, noOutput, debug))

    tab = createArray(tabSize, maxValue)

    tab.sort()

    if not noOutput:
        print("array:"+str(tab[:10]))


if __name__ == "__main__":
    main()

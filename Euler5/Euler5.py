def main(num,ii):
    original = num
    list = [y for y in range(2,21)]
    while num % list[ii] != 0 and ii < len(list):
        num += original
    else:
        print(str(ii+2))
        print(str(num))
        main(num,(ii+1))

main(2520,0)

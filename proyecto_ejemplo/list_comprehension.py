def run():
    squares = []
    # for i in range(1, 1000):
    #     if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 :
    #         squares.append(i)

    [squares.append(i) for i in range(1, 10001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]    

    print(squares)

    


if __name__ == "__main__":
    run()
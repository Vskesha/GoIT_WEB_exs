from threading import Thread


def workeer(arg):
    print(arg)


if __name__ == '__main__':
    for i in range(5):
        th = Thread(target=workeer, args=(i,))
        th.start()

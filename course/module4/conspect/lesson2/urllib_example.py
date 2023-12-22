import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://www.python.org/') as f:
        print(f.read(300))

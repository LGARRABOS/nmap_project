# pip install pythonping


from pythonping import ping

host = input("Enter Host: ")
ping(host, verbose=True)
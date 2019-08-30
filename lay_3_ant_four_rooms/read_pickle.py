import pickle

objects = []
with (open("performance_log.p", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

print(len(objects[0]))

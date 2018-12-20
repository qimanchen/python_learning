import multiprocessing

def dead_loop():
    while True:
        pass


# son process dead loop
p1 = multiprocessing.Process(target=dead_loop)
p1.start()

# main process dead loop
dead_loop()


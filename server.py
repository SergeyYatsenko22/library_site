from livereload import Server


def rebuild():
    ... # do things
    print("Site rebuilt")

rebuild()

server = Server()

server.watch('template.html', rebuild)

server.serve(root='.')
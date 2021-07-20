from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import shutil

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('192.168.100.188', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def CREATE(arch):
        file = open(arch, "w")
        file.close()
        return True
    server.register_function(CREATE, 'create')

    def READ(arch):
        file = open(arch, "r")
        try:
            content = file.read()
        except:
            content = "0"
        file.close()
        return content
    server.register_function(READ, 'leer')

    def WRITE(arch, text):
        file = open(arch, "a")
        file.write('\n' + text)
        file.close()
        return True
    server.register_function(WRITE, 'escribir')

    def RENAME(arch, newArch):
        os.rename(arch, newArch)
        return True
    server.register_function(RENAME, 'rename')

    def REMOVE(arch):
        os.remove(arch)
        return True
    server.register_function(REMOVE, 'remove')

    def MKDIR(dir):
        try:
            os.mkdir(dir)
        except OSError:
            return False
        else:
            return True
    server.register_function(MKDIR, 'mkdir')

    def RMDIR(dir):
        try:
            os.rmdir(dir)
        except OSError:
            shutil.rmtree(dir)
            return True
        else:
            return True
    server.register_function(RMDIR, 'rmdir')

    def READDIR():
        return os.listdir(".")
    server.register_function(READDIR, 'readdir')

    # Inicio
    server.serve_forever()
from sys import stdin


def main():
    f =  open("data.txt","r")
    name,path,tipo = f.readline().split()
    while name != "0" and path != "0" and tipo != "0":
        if name != "1":
            print('class ' + str(name) +"{")
            print('    displayName = "[' + str(tipo)+ '] ' +str(name)+'";' )
            print('    texture = "'+str(path)+str(name)+'.paa'+'";')
            print('    author = "Xitech";')
            print('};')
        else:
            print("//  "+str(path) + "  //")
        name,path,tipo = f.readline().split()
    f.close()
    
main()
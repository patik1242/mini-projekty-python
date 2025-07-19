print("Tabliczka mnozenia\n")

a = int(input("Podaj wymiar x: "))
b = int(input("Podaj wymiar y: "))

#pętla for
for j in range(a):
    for i in range(b):
        print((i+1)*(j+1), end="\t") 
    print(end = "\n")

#end -> przerwa 
#end = " " == cout<<" ";
#\t - tabulator
#\n - nowa linijka == cout<<endl;
    
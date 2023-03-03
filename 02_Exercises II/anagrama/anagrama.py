word1 = input("Dime una palabra ")
word2 = input("Dime otra palabra ")

p1 = list(word1)
p2 = list(word2)
ctde1 = 0
ctde2 = 0

for n in p1:
    ctde1 = ctde1 +1
for n in p2:
    ctde2 = ctde2 +1

if ctde1 == ctde2:
    for n in p1:
        try:
            p2.remove(n)
        except ValueError:
            print("No es un anagrama")
    if p2 == []:
        print(f"Las palavras {word1} y {word2} son anagramas") 
else:
    print("No es un anagrama")





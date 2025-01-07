fin = open("input_033_01.txt")
fout = open("output_033_01.txt", "w")

for string in fin:
    fout.write(string)
fout.close()

score_a = open("input_033_02.txt", "w", encoding="utf-8")
print("2 4 3 5 4 3 2 11 10 41")
score_aa = open("input_033_02.txt", "a", encoding="utf-8")
print("1 2 3 4 5 6 7 8 9 10")

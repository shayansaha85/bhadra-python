firstname = ["Pranjit", "Prasanta"]
lastname = ["Choudhury", "Debnath"]

fullname = []

length_of_single_names = len(firstname)

for i in range(length_of_single_names):
    vfullname = firstname[i] + " " + lastname[i]
    fullname.append(vfullname)

print(fullname)
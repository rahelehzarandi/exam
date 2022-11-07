def morgens_to_sqm(morgens):
    return (morgens / 0.38685)




def create_list(number):
    even_list = []
    for i in range (1,number+8):
        if (i % 2) == 0:
            even_list.append(i)
    return even_list





morgens = 17.5
sqm = morgens_to_sqm(morgens)
print(f"{morgens:.2f} Schaumburg's morgens = {sqm:.2f} square meters")

number = 7
even_list = create_list(number)
print(f"{number} parillista lukua / even numbers: " + str(even_list))
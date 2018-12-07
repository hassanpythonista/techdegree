'''name = 'hassan'
prenom = 'tijani'
print('i am {} {}'.format(name, prenom))
print('i am {1} {0}'.format(name, prenom))
print(f'i am {name} {prenom}')'''

#variables
'''a = 1
b = 2
print("bigger") if a > b else print("smaller")'''


musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
# Your code here
for group in musical_groups:
        if len(group) == 4:
            print(", ".join(group))

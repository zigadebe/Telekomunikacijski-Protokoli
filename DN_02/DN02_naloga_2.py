# ----------- NALOGA 2 -----------
# Iz sledečega lista our_list odstranite vrednost, ki se nahaja na indexu 4. 
# Vrednost dodajte v dictionary pod ključ d. 
# Nato iz dictionary our_dict pridobite vse vrednosti. 
# Te vrednosti shranite v nov tuple in novonastali tuple primerjajte ali je enak podanemu tuple-u our_tuple.

our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)


vrednost = our_list.pop(4)

our_dict['d'] = vrednost

vrednost_a = our_dict['a']
vrednost_b = our_dict['b']
vrednost_c = our_dict['c']
vrednost_d = our_dict['d']
vrednost_e = our_dict['e']
vrednost_f = our_dict['f']

my_tuple = (vrednost_a, vrednost_b, vrednost_c, vrednost_d, vrednost_e, vrednost_f)

if my_tuple == our_tuple:
    print('je enak')
else:
    print('ni enak')

print('-')
print('-')
print('our_tuple ima vrednosti: ')
print(our_tuple)
print('-')
print('my_tuple ima vrednosti: ')
print(my_tuple)


# -------------------------------

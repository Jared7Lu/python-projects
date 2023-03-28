grades = [('English', 88), ('Science', 90), 
          ('Maths', 97), ('Social sciences', 
          82)] 
sorted_tuples = sorted(grades,
key= lambda x: x[1])
print(sorted_tuples) 

cubes = lambda list: [num **3 for num in list]
print(cubes)

equal_num_or_nah = lambda num: num % 2 == 0
t_f = [equal_num_or_nah(num) for num in [0, 1, 2, 3, 4, 5]]
print(t_f)

num_lst = [num for num in range(1, 101)]
print(num_lst)

sentence = "The quick brown fox jumper over the fence"
word_length = {word: len(word) for word in sentence.split() if len(word == 3)}
print (word_length)
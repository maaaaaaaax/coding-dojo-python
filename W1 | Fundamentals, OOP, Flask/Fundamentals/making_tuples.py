# making_tuples.py

# # function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def makingTuples(dictionary):
    tuples = []
    # two values come out with each iteration - dictionary unpacking
    for key, value in dictionary.items():
        tuples.append((key, value))
    return tuple(tuples)

print makingTuples(my_dict)

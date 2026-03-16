print(r"""
 //// //// ###################################################################### //// //// / |||| |||| ||
//// //// ###################################################################### //// //// // |||| |||| ||
/// //// ####*'   ___ // /_         ___ ___   _ ____ ___  _ ___  ____  `*###### //// //// /// |||| |||| ||
// //// ####*  // _ ,`/ __ `  __,// __ `_, `/_/ __,/ __,/_/ _ ,`/ __ \  *##### //// //// ///  |||| |||| ||
/ //// *****  // /_/ / / / ///_/ / / / / / / /__  /__  / / /_/ / / / /  ***** //// //// ////  |||| |||| ||
 //// ******. \\____/_/ /_/    //_/ /_/ /_/_/____/____/_/\____/_/ /_/ ,***** //// //// //// / |||| |||| ||
//// ********************************************************************** //// //// //// // |||| |||| ||                                   
/// **************************** Josh Melick ***************************** //// //// //// /// |||| |||| ||
################################## CS-161P ###############################################################
##########################################################################################################


      
      (C#/Db)(D#/Eb)   (F#/Gb)(G#/Ab)(A#/Bb)   (C#/Db)(D#/Eb)    (F#/Gb)(G#/Ab)(A#/Bb)   (C#/Db)(D#/Eb)
         |     |           |     |     |           |     |           |     |     |           |     |     
   |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
   |    |||   |||    |    |||   |||   |||    |    |||   |||    |    |||   |||   |||    |    |||   |||    |   
   |    |||   |||    |    |||   |||   |||    |    |||   |||    |    |||   |||   |||    |    |||   |||    | 
   |    |||   |||    |    |||   |||   |||    |    |||   |||    |    |||   |||   |||    |    |||   |||    |
   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |  C  |  D  |  E  |  F  |  G  |  A  |  B  |  C  |  D  |  E  |  F  |  G  |  A  |  B  |  C  |  D  |  E  |
   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
   |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
""")


# variable declaring list literal to the notes on a keyboard
chromatic_scale = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

# a dictionary mapping the key signatures to their respected pitch class
circle_fifths = {
    'c':  ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b'],
    #5THS
    'g':  ['g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#'],
    'd':  ['d', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#'],
    'a':  ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#'],
    'e':  ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#'],
    'b':  ['b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#'],
   'f#':  ['f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f'],
    #4THS
     'f': ['f', 'gb', 'g', 'ab', 'a', 'bb', 'b', 'c', 'db', 'd', 'eb', 'e'],
    'bb': ['bb', 'b', 'c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a'],
    'eb': ['eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b', 'c', 'db', 'd'],
    'ab': ['ab', 'a', 'bb', 'b', 'c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g'],
    'db': ['db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b', 'c'],
# ENHARMONIC HANDLER
# Horn players prefer seeing Eb and Bb instead of D# and A#
    'd#': ['eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b', 'c', 'db', 'd'],
    'a#': ['bb', 'b', 'c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a'],
    'gb': ['f#', 'g', 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'e#']
}

root = ""

while root not in circle_fifths:
    root = input("Enter Root Note: ").strip().lower()
    if root not in circle_fifths:
        print(f" '{root}' isn't a valid note. Try again.")
third = ""
while third not in ["maj", "min"]:
    third = input("Major or Minor (maj/min)? ").strip().lower()
    if third not in ["maj", "min"]:
        print(f" '{third}' isn't a valid choice. Try again.")

fifth = ""
while fifth not in ["dim", "perf", "aug"]:
    fifth = input("Diminished, Perfect, Augmented (dim/perf/aug)? ").strip().lower()
    if fifth not in ["dim", "perf", "aug"]:
        print(f" '{fifth}' isn't a valid choice. Try again.")

seventh = ""
while seventh not in ["maj", "min"]:
    seventh = input("Major or Minor Seventh (maj/min)? ").strip().lower()
    if seventh not in ["maj", "min"]:
        print(f" '{seventh}' isn't a valid choice. Try again.")

# Extension
print("\n*** Extensions (n=natural, #=sharp, b=flat) ***")
ninth = input("9th? ").strip().lower()
eleventh = input("11th? ").strip().lower()
thirteenth = input("13th? ").strip().lower()

# CHORD BUILDER
interval_distance = [0]

# 3RD
if third == "maj":
    interval_distance += [4]
else:
    interval_distance += [3]

# 5TH
if fifth == "dim":
    interval_distance += [6]
elif fifth == "aug":
    interval_distance += [8]
else:
    interval_distance += [7]

# 7TH
if seventh == "maj":
    interval_distance += [11]
else:
    interval_distance += [10]

# 9TH
if ninth == "n":
    interval_distance += [14]
elif ninth == "b":
    interval_distance += [13]
elif ninth == "#":
    interval_distance += [15]

# 11TH
if eleventh == "n":
    interval_distance += [17]
elif eleventh == "#":
    interval_distance += [18]

# 13TH
if thirteenth == "n":
    interval_distance += [21]
elif thirteenth == "b":
    interval_distance += [20]


def final_chords(root_val, intervals, label):
    final_chord = circle_fifths.get(root_val, circle_fifths['c'])
    print(f"{label} ({root_val.capitalize()}): ", end="")
    for step in intervals:
        chord_notes = final_chord[step % 12]
        print(f"{chord_notes.capitalize()} ", end="")
    print()

print()

final_chords(root, interval_distance, "Concert")

if root in chromatic_scale:
    first_note = chromatic_scale.index(root)
else:
    first_note = 0

# Bb
bb_trans = (first_note + 2) % 12
bb_root = chromatic_scale[bb_trans]
final_chords(bb_root, interval_distance, "Bb")

# Eb
eb_trans = (first_note + 9) % 12
eb_root = chromatic_scale[eb_trans]
final_chords(eb_root, interval_distance, "Eb")

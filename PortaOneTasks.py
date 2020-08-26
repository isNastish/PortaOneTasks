file = open('original_file.txt').readlines() # read file.
list1 = [int(i.rstrip()) for i in file] # create a list of all values in file

LengthGrow = [] # here will be stored the value of the biggest increasing sequence(how much elements in one sequence)
LengthFall = [] # the same, but decresing sequence.
Average = 0 # summing up all values into this veriable to find average value in future.

# median.
for j in range(len(list1)):
    if (len(list1) % 2) != 0: 
        if j == ((len(list1) - 1) / 2): 
            print('Median: %i' % (list1[j]))
            break # if found - break
    else:
        if j == (len(list1) // 2): # the next value after average.
            print('Median: %.4f' % ((list1[j] + list1[j - 1]) / 2))
            break
# biggest incresing sequence.
for k in range(len(list1)):
    Average += list1[k]
    if not k:
        Grow = []
        Grow.append(list1[k])
        countGrow = 1
    elif k:
        if (list1[k] > list1[k - 1]):
            Grow.append(list1[k])
            countGrow += 1
            if k == (len(list1) - 1) and countGrow > LengthGrow[0]: # for the case if the last value will create the biggest sequence
                LengthGrow[0] = countGrow
                tempGrow = [] # for storing the biggest single sequence
                tempGrow += Grow
        else:
            if not LengthGrow:LengthGrow.append(countGrow)
            if (countGrow > LengthGrow[0]): # if the len of following sequence bigger then len of sequence before
                LengthGrow[0] = countGrow # append value (amount of numbers in the biggest sequence).
                tempGrow = [] # if the len of the sequence will be bigger then seq. before we freeing tempGrow and add all seq. from Grow to tempGrow
                tempGrow += Grow
            Grow = [] # if we found a number in file that destroy our sequence we make Grow free
            Grow.append(list1[k]) # add the first value of the first new sequence.
            countGrow = 1
            
# biggest increasing sequence
for k in range(len(list1)):
    if not k:
        Fall = []
        Fall.append(list1[k])
        countFall = 1
    elif k:
        if (list1[k] < list1[k - 1]):
            Fall.append(list1[k])
            countFall += 1
            if k == (len(list1) - 1) and countFall > LengthFall[0]:
                LengthFall[0] = countFall
                tempFall = []
                tempFall += Fall
        else:
            if not LengthFall:LengthFall.append(countFall)
            if (countFall > LengthFall[0]):
                LengthFall[0] = countFall
                tempFall = []
                tempFall += Fall
            Fall = []
            Fall.append(list1[k])
            countFall = 1
print('Biggest Decrease list:',tempFall,\
    'Length:',len(tempFall),'\n'\
    'Biggest Increase list:',tempGrow,\
    'Length:',len(tempGrow),'\n'\
    'Maximum:',max(list1),'\n'\
    'Minimum:',min(list1),'\n'\
    'Average: %.5f' % (Average / len(list1)))

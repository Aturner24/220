
def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    classaverage = 0
    numberofkids = 0
    for line in infile:
        kidname = line[0 : line.find(":")]
        grades = (line[line.find(":") + 2: line.find('\n')].split(' '))
        outfile.write(kidname+"'s"+" average:")
        weightaccum = 0
        formulaaccum = 0

        #for the love of god find a better way to do this
        #weight test
        for num in range(0, (len(grades)), 2):
            weightaccum = weightaccum + float(grades[num])
        if weightaccum<100:
            outfile.write("Error: The weights are less than 100. \n")
        elif weightaccum>100:
            outfile.write("Error: The weights are more than 100. \n")

        else:
            numberofkids = numberofkids + 1
            for newnum in range(0, len(grades), 2):
                formulaaccum = formulaaccum + (int(grades[newnum])*int(grades[newnum+1]))
            outfile.write(str(formulaaccum/100)+'\n')
            classaverage = classaverage + (formulaaccum/100)
    outfile.write("class average:"+ str(classaverage/numberofkids))








    infile.close()
    outfile.close()
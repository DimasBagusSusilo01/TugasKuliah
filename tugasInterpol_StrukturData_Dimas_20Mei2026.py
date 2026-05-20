listdata = [7,20,25,36,42,51,64,76,83,99,100]
print(listdata)

rumus = 0 + ((76 - listdata[0])/(listdata[-1]-listdata[0])) * ((len(listdata)-1) - listdata.index(7))

print (round(rumus))

f = open (‘myfile.txt’, 'r')
 
for line in f:
print (line, end = ‘’)
 
f.close()


f = open (‘myfile.txt’, 'a')
 
f.write(‘\nParagraphe a ajouter.’)
f.write(‘\nPython!’)
 
f.close()


inputFile = open (‘myfile.txt’, 'r')
outputFile = open (‘myoutputfile.txt’, 'w')

msg = inputFile.read(10)
 
while len(msg):
  outputFile.write(msg)
  msg = inputFile.read(10)

inputFile.close()
outputFile.close()

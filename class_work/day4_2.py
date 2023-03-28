# acivity for errors
fileName = input("Please enter hte name of the file you would like to read: ")
myfile = open(fileName, 'r') # Open a file for reading.
contents = myfile.readlines() # Read in the content by line.
myfile.close() # Explicitly close the file
print(contents) #print the contents of the file

class FileManipulator:
    def __init__(self, file_name):
        self.contents = None
        while self.contents == None:
            try:
                self.myfile = open(file_name, 'r')
                self.contents = self.myfile.readlines()          
            except(FileNotFoundError, TypeError, OSError) as e:
                print(f"Input file not found or misconfigured, {e}")
                file_name = input("Please enter the name of he file you would like to read")
            else:
                print(self.contents)
                myfile.close()
    def reverse(self, new_filename):
        print()
# '''
# test code:

# f = FileManipulator("tmp.txt")
# print(f.contents)
# f.reverse("tmp2.txt")
# '''
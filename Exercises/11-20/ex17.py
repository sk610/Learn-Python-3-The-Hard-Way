from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done. Closing the files.")

out_file.close()
in_file.close()

'''
Study Drills

1.Ok
2. Couldn't figure it out at this time.
3. Ok.
4. Ok - preventing the system from wasting resources.
5. Ok


'''

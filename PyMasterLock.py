import argparse
import iteritems

parser = argparse.ArgumentParser()
parser.add_argument("--first", help="""Find the "First Locked Position"Rotate dial to the left (towards 10) hard until the dial gets locked.Notice how the dial is locked into a small groove. If you're directly between two digits such as 3 and 4, release the shackle and turn the dial left further until you're into the next locked groove. However, if the dial is between two half digits (e.g., 2.5 and 3.5), then enter the digit in-between (e.g., 3) into First Locked Position in the calculator below.""", type=float)
parser.add_argument("--second", help="""Find the "Second Locked Position"Do all of the above again until you find the second digit below 11 that is between two half digits (e.g., 5.5 and 6.5), and enter the whole number (e.g., 7) into Second Locked Position in the calculator below.""", type=float)
parser.add_argument("--third", help="""Find the "Resistant Location"Apply half as much pressure to the shackle so that you can turn the dial.Rotate dial to the right until you feel resistance. Rotate the dial to the right several more times to ensure you're feeling resistance at the same exact location.Enter this number into Resistant Location. If the resistance begins at a half number, such as 14.5, enter 14.5.""", type=float)
args = parser.parse_args()

def combo(x):
	second = []
	third = []
	l1 = args.first # first locked position
	l2 = args.second # second locked position
	rl = args.third # resistance lock position

	first = (rl + 5) % 40
	mod = first % 4

	for i in xrange(4):
		if (((10 * i) + l1) % 4) == mod:
			third.append(float((10 * i) +l1))
		if (((10 * i) + l2) % 4) == mod:
			third.append(float((10 * i) +l2))

	for i in third:
		print "[*] Third Digit is : %i\r\n" % i

	for i in xrange(10):
		temp = ((mod + 2) % 4) + (4 * i)
		if ( not x or ( (third[x-1] +2) %40 != temp and (third[x-1] -2) %40) ):
			second.append(float(temp))

	print "[*] First Digit is :" + str(first)
	print "[*] Second digits could be: + ', '.join(itertools.imap(str, second))
	print "[*] third digits could be: + ', '.join(itertools.imap(str, third))
	for i in third:
		print "[*] Third Digit is : %i\r" % i


combo(0)

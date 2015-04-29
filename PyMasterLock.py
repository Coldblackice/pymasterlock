import itertools
import sys

class MasterLock():
	def __init__(self):
		self.x = 0
		self.second = []
		self.third = []
		
		self.l1 = float( sys.argv[1] )
		self.l2 = float( sys.argv[2] )
		self.r1 = float( sys.argv[3] )

		self.first = ( self.r1 + 5 ) % 40
		self.mod = self.first % 4

	def get_first(self):
		"""Find the "First Locked Position"Rotate dial
		to the left (towards 10) hard until the dial gets
		locked.Notice how the dial is locked into a small
		groove. If you're directly between two digits such
		as 3 and 4, release the shackle and turn the dial
		left further until you're into the next locked groove.
		However, if the dial is between two half digits
		(e.g., 2.5 and 3.5),then enter the digit in-between
		(e.g., 3) into First Locked Position in the calculator below."""

		return float( ( self.r1 + 5 ) % 40 )

	def get_second(self):
		"""Find the "Second Locked Position"Do 
		all of the above again until you find the 
		second digit below 11 that is between two 
		half digits (e.g., 5.5 and 6.5), and enter 
		the whole number (e.g., 7) into Second 
		Locked Position in the calculator below."""
		for i in xrange(10):
			temp = ( ( self.mod + 2 ) % 4 ) + ( 4 * i )
			if ( not self.x or ( ( third[self.x-1] +2 ) %40 != temp and ( third[self.x-1] -2 ) %40 ) ): self.second.append( float( temp ) )
				
		return ', '.join( itertools.imap( str, self.second ) )

	def get_third(self):
		"""Find the "Resistant Location"Apply 
		half as much pressure to the shackle 
		so that you can turn the dial.Rotate 
		dial to the right until you feel 
		resistance. Rotate the dial to the 
		right several more times to ensure 
		you're feeling resistance at the 
		same exact location.Enter this number 
		into Resistant Location. If the resistance 
		begins at a half number, such as 14.5, enter 14.5."""
		for i in xrange(4):
			if ( ( ( 10 * i ) + self.l1 ) % 4 ) == self.mod: self.third.append( float( (10 * i ) + self.l1 ) )
			if ( ( ( 10 * i ) + self.l2 ) % 4 ) == self.mod: self.third.append( float( (10 * i ) + self.l2 ) )
				
		return ', '.join( itertools.imap( str, self.third ) )

	if len(sys.argv) != 4:
		sys.exit('Usage: %s firstnumber secondnumber thirdnumber' % sys.argv[0] + '\n' + "Example: python2 %s 3 6 10" % sys.argv[0])

ml = MasterLock()
print "[+] First number : " + str(ml.get_first())
print "[+] possible Second numbers : " + str(ml.get_second())
print "[+] Two Possible Third numbers : " + str(ml.get_third()) + " ( increased accuracy coming in future)"

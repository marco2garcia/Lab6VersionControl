# this is my first github addition

def encode_password(password):
	encoded_password = ""
	for i in password:
		encoded_i = str(int(i) + 3)
		if int(encoded_i) > 10:
			encoded_i = str(int(encoded_i) - 10)
		encoded_password += encoded_i
	return encoded_password

#Lucas Nardin decode() function
def decode_password(encoded_password):
	decoded_password = ''
	for i in encoded_password:   #revert numbers to their original values
		decoded_i = str(int(i) - 3)
		if int(decoded_i) < 0:   #numbers can only be from 0-9
			decoded_i = str(int(decoded_i) + 10)
		decoded_password += decoded_i
	return decoded_password

def main(encoded_password=None):
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")
	print()
	user_option = int(input("Please enter an option: "))

	if user_option == 1:
		password = input("Please enter your password to encode: ")
		encoded_password = encode_password(password)
		print("Your password has been encoded and stored!")
		print()
		main(encoded_password)

	elif user_option == 2:
		if encoded_password is None:
			print("You must encode a password first.")
		else:
			decoded_password = decode_password(encoded_password)
			print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
		print()
		main(encoded_password)
	else:
		print()

if __name__ == "__main__":
	main()


## Starting Steps

1. Set up pycharm
2. Create two directories
	1. Python(Project)
	2. Cyrptography
3. Create first .py file named "keylogger" under project Directory
4. Now install the following third party modules
	1. Go to pycharm settings, under project:video project files -> project interpreter. You can simply add modules by clicking the plus sign
	2. Add the following modules:
		1. pywin32
		2. pynput
		3. scipy
		4. cryptography
		5. requests
		6. pillow
		7. sounddevice

## The coding begins 

1. Import the libraries now, (import the following ones)
	- Basic libraries we need for email stuff![[Pasted image 20260110162007.png]]
	- For collecting default computer information![[Pasted image 20260110162120.png]]
	- for Clipboard and keyboard/ Logging keys![[Pasted image 20260110162210.png]]
	- For time and system information ![[Pasted image 20260110162418.png]]
	- For microphone ![[Pasted image 20260110162406.png]]
	- For encryption/cryptography ![[Pasted image 20260110162454.png]]
	- To get the user info ![[Pasted image 20260110162606.png]]
	- Multi support freeze control to take one screenshot at a time ![[Pasted image 20260110162636.png]]
2. creating Variables for 
	1. Keylogger = Keylog.txt -> To store All our keystrokes appended 
	2. file_path = {file path of the keylog.txt} (by right clicking the file)
		1. Add double backslashed for each back slash so that is an escape sequence ![[Pasted image 20260110164302.png]]
		2. another variable under file_path named "extend= "\\" " for extending the original file_path in case
	3. Count = 0 -> for counting 
	4. keys = [] -> list for storing keystrokes and appending in the keylogger variable/file
	5. Email_address -> {address of your mail to send email from} 
	6. password for the gmail address mentioned abocve
	7. toaddr = the one you are sending the mail to 
	8. System_information = "system_info.txt" -> to get the system information in a new file
	9. Clipboard_information = "clipboard.txt" -> to get the clipboard information from the device into this new file 
	10. similarly audiofile.wav and screenshot.png
	11. num_of_iteration = 0
	12. Current_time= time.time()
	13. Stoppingtime= time.time() + time_iteration(set this variable as constant(12sec for example) near the vairbales of microphone time)
	14. num_of_iterations_end, for the times you want to run the whole while loop before ending it. (3 for example)
3. Creating functions 
	1. Logging the keys and counting them
		1. ![[Pasted image 20260110165513.png]]
			1. Add global variable "currentTime" when creating a while loop later on
			2. also declare "currentTime= time.time()"
		2.  If the count goes above 1, the keys count is reset and keys are sent to the "write_file" function for processing and appending the keys in the Keylogger file  
			1. ![[Pasted image 20260110172527.png]]
	2.  To write keys to a specific file (keys.txt)
		1. Opening the file with "with open()" function 
		2. eliminated the " ' "
		3. Adding new line for every "space" to differentiate words 
		4. ![[Pasted image 20260110171033.png]]
		5. elif statement in case things go south
			1. ![[Pasted image 20260110172745.png]]
	3. To exit from our keylogger when we are done. 
		1. escaping the keylogger program after using the "escape" key. 
		2. ![[Pasted image 20260110171544.png]]
			1. new exit statement: "if current time> stoppingTime: return false"
	4.  Setting up a listenertt
		1. infinite loop to just monitor the keyboard and mouse clicks. 
		![[Pasted image 20260110173248.png]]
	5. Send email function
		1. ![[Pasted image 20260110180130.png]]
		2. ![[Pasted image 20260110180524.png]]
	6. Computer information function
		1. ![[Pasted image 20260110183230.png]]
	7. Clipboard information collection
		1. ![[Pasted image 20260110184034.png]]
	8. Microphone
		1. set up a default sampling frequency as fs=  44100hz 
		2. Default seconds the microphone listens by "Seconds = Microphone time" and later set "microphone time" with constants as "microphone_time = 10" for 10 seconds
		3. Varibale for storing the recorded audio.  
		4.  Create a .wav file for storing audio information. 
		5. ![[Pasted image 20260112160247.png]]
	9. Function for storing screenshots
		1. using library "Image grab" as variable IM
		2. Create a png file for storing screenshot
		3. ![[Pasted image 20260112160455.png]]
	10. Not a function but a if statement
		1. current time > stoppingtime
		2. 
4. While loop
	1. number  iterations we want to run for the time. 
	2. Just select all the functions and ident them one time, so it all comes under a while loop of num_of_iteration< num_of_iteration_end
	3. Add "Current_time = time.time() & stopping time = current_time+ time_interval" 
		1. Declare it before the while loop starts
		2. also in the on_release function
		3. in if statement for terminalting the while loop
		4. ![[Pasted image 20260113174820.png]]

## Encryption 

make a encrypted version copies of all the files you have created... which is key_info, clipboard_info, Screenshot_info, mic_info. 
- ![[Pasted image 20260113175122.png]]

new variable at the very end of the code 
- " files_to_encrypt", it shall include all the paths of the first files we created.
- "encrypted_file_names", includes the paths of all the new encrypted files we created before

for loop encrypting_file in files_to_encrypt
- with open block to open all the files with 'rb' property
- declaring variable fernet for our key
- New variable "encrpted" ro encrypt the files with help of fernet
- with open block to append the encrypted data in the e-files we created, with 'wb' property
- send the emailcontaining all the encrypted files

![[Pasted image 20260113180048.png]]

"time.sleep(120)" for properly sending the mails. 

lastly to clean up our tracks and delete files
![[Pasted image 20260113182146.png]]
## Cryptography directory

create two files 
- for generating a key to encrypt our data (generatekey.py)
- for decrypting the encrypted data

1. Generating the key
	1. Import the libraries of cryptography
	2. key variable to assign it as a key, used fernet.generate_key()
	3. open file to generate a file for encryption key in encryption.txt
	4. File.write to store in the opened file. 
	5. close the file. file.close()
	6. ![[Pasted image 20260113181218.png]]
2. in the project.py add the key we generated just now under variable "key" add it above file path, or before the taddr
3. decrypt.py for decryption of the files
	1. ![[Pasted image 20260113181959.png]]


## References 

YouTube video from which this whole is copied from 
- <iframe width="565" height="300" src="https://www.youtube.com/embed/25um032xgrw?si=_G0E2wHMHPDJi0Vj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
- Video which inspired him to make an advanced version 
	- <iframe width="560" height="315" src="https://www.youtube.com/embed/TbMKwl11itQ?si=QGthGHkVmaqG-JFa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Getting inspiration from gfg for sending mail and attachements in the mail
	 1. https://www.geeksforgeeks.org/python/send-mail-attachment-gmail-account-using-python/
	 2. Just copy paste the code in here link to your code in your IDE after the file_path variable declaration. 

Special mention to google for helping us for the library. 
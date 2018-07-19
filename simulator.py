# RAM and register definitions
r0 = [False] * 4
r1 = [False] * 4
mem = [[False] * 4] * 4
page = [False] * 4
pc = [False] * 4

'''
Commands:
run -> run the code
select -> select one binary file
show -> print out RAM and register content
step -> run a single step
'''

def process(input_text):
	instruction = input_text.split(" ")[0]
	if instruction == "run":
		run()
	elif instruction == "select":
		select(input_text.split(" ")[1])
	elif instruction == "show":
		show()
	elif instruction == "step":
		step()

def run():
	print("running")

def select(file):
	print(file)

def show():
	print("show")

def step():
	print("step")

if __name__ == "__main__":
	while 1:
		input_text = str(input(">"))
		process(input_text)

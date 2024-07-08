import multiprocessing

from multiprocessing import Pool

def print_number(number):
    print(number)

data_list = list(range(10000))

print("This is going to use one CPU core.")
for d in data_list:
	print_number(d)

if __name__ == '__main__':
	print("This is going to use all of your CPU cores.")
	with Pool(multiprocessing.cpu_count()) as p:
		p.map(print_number, data_list)
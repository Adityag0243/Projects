import random

# for reading IP address from ip_addresses.txt as size can be a larger value
def read_ip_file(filename):
    with open(filename, "r") as file:
        ip_list = [line.strip() for line in file]  # Read and remove extra spaces/newlines
    return ip_list



# format of IPv4  xxx.xxx.xxx.xxx  which has 2^32 possibilities
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def generate_ip_file(filename, count):
    with open(filename, "w") as file:
        for _ in range(count):
            file.write(generate_random_ip() + "\n")  # Write each IP on a new line


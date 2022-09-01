from hashlib import sha256
import sys

def process_args(args):
    cleaned_data = []
    for arg in args:
        if "." in arg:
            try:
                with open(arg, "rb") as file:
                    data = file.read()
            except:
                print(f"Couldn't Read the file [{arg}]. File Omitted in hash check!")
            else:
                cleaned_data.append(data)
            finally:
                continue
        cleaned_data.append(arg)
    return cleaned_data

def compute_hash(data=" "):
    try:
        return sha256(data).hexdigest()
    except TypeError:
        print("Object type must be Unicode")
        return sha256(data.encode("utf-8")).hexdigest()
    finally:
        print("_"*88)

if __name__ == "__main__":
    args = [arg for arg in sys.argv[1:]]

    if not args:
        file = input("Please Enter Path to file: ")
        try:
            open_file = open(file, 'r')
        except Exception as err:
            print(f"Can't Open the file, error = {err}")

    clean_data = process_args(args)

    container = {k:len(v) for k,v in zip(args,clean_data)}
    print("Container = {Object name : Length}\n", container)

    for index, obj in enumerate(clean_data):
    	hash_value = compute_hash(obj)
    	print(f"'{args[index]}' : ", hash_value)

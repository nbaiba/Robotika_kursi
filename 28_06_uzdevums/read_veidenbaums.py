import os

##########
# 1a Task
##########

def file_line_len(fpath):
    os.chdir('28_06_uzdevums')
    with open(fpath, mode='r', encoding='utf-8') as f:
        veidenbaums_loaded = len(f.readlines())
    print(veidenbaums_loaded)


# print(file_line_len('veidenbaums.txt'))

##########
# 1b Task
##########

def get_poem_lines(fpath):
    os.chdir('28_06_uzdevums')
    with open(fpath, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip() and '***' not in line:
                print(line)
    
# get_poem_lines('veidenbaums.txt')

##########
# 1c Task
##########

def save_lines(destpath, lines):
    with open(destpath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)

# save_lines('my_dog.txt', 'bark')
# save_lines('my_cat.txt', 'meow')

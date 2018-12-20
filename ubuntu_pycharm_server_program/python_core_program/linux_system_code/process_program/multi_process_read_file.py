from multiprocessing import Pool,Manager
import os

def copy_file_task(name,old_folder_name,new_folder_name,queue):
    "finish copy one file function"
    fr = open(old_folder_name+"/"+name)
    fw = open(new_folder_name+"/"+name,"w")
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)


def copy_file_task_with(name,old_folder_name,new_folder_name,queue):
    "finish copy one file function"
    with open(old_folder_name+"/"+name) as fr:
        with open(new_folder_name+"/"+name,"w") as fw:
            content = fr.read()
            fw.write(content)
    queue.put(name)


def main():
    #0. get copy folder name
    old_folder_name = input("please input fold name: ")

    #1. create a file folder
    new_folder_name = old_folder_name+"attachment"
    os.mkdir(new_folder_name)

    #2. get all file name from ole folder
    file_names_list = os.listdir(old_folder_name)


    #3. use multiprocess copy original folder to new folder
    pool = Pool(5)
    queue = Manager().Queue()

    for name in file_names_list:
        pool.apply_async(copy_file_task_with, args=(name,old_folder_name,new_folder_name,queue))

    all_num = len(file_names_list)
    num = 0
    while True:
        queue.get()
        num += 1
        copy_rate = num/all_num
        print("\rcopy rate is :%.2f%%"%(copy_rate*100),end="")
        if num == all_num:
            break
    print("\n finish all copy work.....")


if __name__ == "__main__":
    main()

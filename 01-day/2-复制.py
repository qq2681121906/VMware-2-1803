file_name = input("请输入文件名要带后缀")
old_file = open(file_name,"r")
content = old_file.read()
position = file_name.rfind(".")
file_name[0:position]
file_name[position:]
new_file = open(file_name+"复制"+"2.txt","w")
new_file.write(content)
old_file.close()
new_file.close()


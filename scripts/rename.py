import re, subprocess

pattern = '(PM-)0*([1-9].*)'
f = open('ls.out', 'r')
file_names = [line.strip() for line in f if re.search('.*PM.*', line)]
reg = re.compile(pattern)

for i in range(len(file_names)):
    cmd = ["mv", file_names[i], "./newNames/morty" + str(i) + ".png"]
    subprocess.call(cmd)

# fixed_file_names = [re.search(pattern, name).group(2) for name in file_names]
# import code
# code.interact(local=locals())
# # #fix file names
# # fixed_file_names = []
# # for name in file_names:
# #     if reg.match(name):
# #         m = re.search(pattern, name)
# #         fixed_file_names.append(str(m.group(1) + m.group(2)))
# #     else:
# #         fixed_file_names.append(name)
# #
# # #run some mv commands
# # # subprocess.call(["command1", "arg1", "arg2"])
# #
# # for i in range(len(fixed_file_names)):
# #     cmd = ["mv", file_names[i], fixed_file_names[i]]
# #     subprocess.call(cmd)
# #     # print cmd

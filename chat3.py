
lines = []
with open('3.txt' , 'r' , encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())			#這邊是把換行去掉


for line in lines:
	s = line.split(' ')						# 這邊是字串 使用空格去做切割
	time = s[0][:5]
	name = s[0][5:]
	print(name)
	print(s)


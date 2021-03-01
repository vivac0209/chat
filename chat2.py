
def read_file(filename):
	lines = []
	with open(filename , 'r' , encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	
	person = None					# 沒有預設值
	v_word_count = 0
	m_word_count = 0
	l_word_count = 0

	v_sticker_count = 0
	m_sticker_count = 0
	l_sticker_count = 0

	v_image_count = 0
	m_image_count = 0
	l_image_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Viva':
			if s[2] == '貼圖':
				v_sticker_count += 1
			elif s[2] == '圖片':
				v_image_count += 1
			else:
				for m in s[2:]:
					v_word_count += len(m)

		elif name == 'Matt':
			if s[2] == '貼圖':
				m_sticker_count += 1
			elif s[2] == '圖片':
				m_image_count += 1
			else:
				for m in s[2:]:
					m_word_count += len(m)

		elif name == 'Leo':
			if s[2] == '貼圖':
				l_sticker_count += 1
			elif s[2] == '圖片':
				l_image_count += 1
			else:
				for m in s[2:]:
					l_word_count += len(m)

	print('viva說了' , v_word_count , '個字' , '傳' ,v_sticker_count, '個貼圖' , '傳' , v_image_count ,'個圖片')
	print('matt說了' , m_word_count , '個字' , '傳' ,m_sticker_count, '個貼圖' , '傳' , m_image_count ,'個圖片')
	print('leo說了' , l_word_count , '個字' , '傳' ,l_sticker_count, '個貼圖' , '傳' , l_image_count ,'個圖片')


def write_file(filename , lines):
	with open(filename , 'w' ) as f:
		for line in lines:
			f.write(line + '\n') 


def main():
	lines = read_file('LINE-sc.txt')
	lines = convert(lines)
	# write_file('ouput.txt', lines)

main()

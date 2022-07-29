import os
import sys
def count_code_lines(filename):
    res = os.walk(filename)
    count = 0
    for path, _, file_list in res:
        for file in file_list:
            filename = os.path.join(path, file)
            if filename.endswith('py'):
                with open(filename, 'r', encoding='utf8') as fr:
                    file_count = 0
                    for i in fr:
                        if i.startswith('#') or i.startswith('\n'):
                            continue
                        count += 1
                        file_count += 1
                    print(f'{filename}有{file_count}行')

    print(f'总共有{count}行')

if __name__ == '__main__':
    filename = sys.argv[1]
    filename = 'spss'
    count_code_lines(r'D:\realvideo')
    count_code_lines(filename)

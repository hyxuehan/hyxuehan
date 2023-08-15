'''
# 1、
def get_max(lst):
    """
    返回列表lst的最大值
    :param lst:
    :return:
    """
    lst.sort()
    return lst[-1]


lst = [4, 2, 1, 6, 7, 9]
max_value = get_max(lst)
print(max_value)
'''

'''
# 2、
def get_max_socre(score_dic):
    """
    返回学生考试成绩的最高分的科目和分数
    :param score_dic:
    :return:
    """
    max_score = 0
    max_course = ''
    for k,v in score_dic.items():
        if v > max_score:
            max_score = v
            max_course = k
    return max_course,max_score


dic = {
    '语文': 90,
    '数学': 97,
    '英语': 98
}

course, score = get_max_socre(dic)
print(course, score)
'''


# 3、
def is_palindrome(string):
    """
    判断字符串string是回文
    :param string:
    :return:
    """
    lst = list(string)
    lst.reverse()
    str = ''.join(lst)
    if string == str:
        return True
    return False


print(is_palindrome('abcddcba'))
print(is_palindrome('pythonohtyp'))
print(is_palindrome('bookkob'))

# import logging
#
# logging.basicConfig(filename='access.log', #不指定，默认打印到终端
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10)
# logging.debug('调试debug') #10
# logging.info('消息info') #20
# logging.warning('警告warn') #30
# logging.error('错误error') #40
# logging.critical('严重critical') #50

'''
WARNING:root:警告warn
ERROR:root:错误error
CRITICAL:root:严重critical
'''

# 拿到日志的产生者
# 第一个日志的产生者kkk
# 第二个日志的产生者bbb
# 但是需要先导入日志配置
# import settings
# # import logging.config
# from logging import config, getLogger
# config.dictConfig(settings.LOGGING_DIC)
# logger1=getLogger('kkk')
# logger1.info('这是一条info日志')
# logger2=getLogger('bbb')
# logger2.info('这是logger2产生的日志')
# logger3=getLogger('asdsa')
# logger3.info('这是logger3产生的日志')

# 1、日志名的命名
#   日志名是区别日志业务归属的一种非常重要的标识
# 2、日志轮转
# 日志记录着程序运行过程中的关键信息，需要归档
import re
print(re.findall('\w','abc123_*()-=')) #匹配字母数字及下划线
print(re.findall('\W','abc123_*()-=')) #匹配非字母数字下划线
print(re.findall('\s','ab\tc 12\n\r\f3_*() -=')) #匹配任意空白字符，等价于[\t\n\r\f]
print(re.findall('\S','ab\tc 12\n\r\f3_*() -='))# 匹配任意非空字符
print(re.findall('\d','abc123_*()-='))# 匹配任意数字，等价于[0-9]
print(re.findall('\D','abc123_*()-='))# 匹配非数字
print(re.findall('\Aabc','abcabc123_*()-='))# 匹配以什么开头
print(re.findall('^abc','abcabc123_*()-='))# 匹配以什么开头
print(re.findall('abc','abcabc123_*()-='))# 匹配第一个值
print(re.findall('abc\Z','abcabc123_*()-abc=abc'))#匹配结尾
print(re.findall('abc$','abcabc123_*()-abc=abc'))#匹配结尾
print(re.findall('c','abcabc123_*()-abc=abc'))#匹配结尾
# 重复匹配：| . | * | ? | .* | .*? | + | {n,m} |
# 1、 .:匹配除了\n之外任意一个字符,指定re.DOTALL之后才能匹配换行符
print(re.findall('a.b','a1b a2b a b abbb a\nb a\tb a*b'))#
# 2、 *：左侧字符重复0次或无穷次，性格贪婪
print(re.findall('ab*','abcabcabbbb123_*(a)-abc=abc'))#
# 3、 +：左侧字符重复1次或无穷次，性格贪婪
print(re.findall('ab+','abcabcabbbb123_*(a)-abc=abc'))#
# 4、 ?：左侧字符重复0次或1次，性格贪婪
print(re.findall('ab?','abcabcabbbb123_*(a)-abc=abc'))#
# 5、 {n,m}：左侧字符重复n次到m次，性格贪婪，可以只指定一个值
# {1,}
# {0,}
# {0,1}
print(re.findall('ab{2,5}','ababbbbbbbbcabcabbbb123_*(a)-abc=abc'))#

#1、找出所有的整数和小数
print(re.findall('\d+\.?\d*','12ab4.bb3bbbb4.6b0.4cs1232.098abcab3'))
#2、[]匹配指定字符一个
print(re.findall('a.b','a1b a3b aXb a b a\nb'))#
print(re.findall('a[\d]b','a1b a3b aXb a b a\nb'))#
print(re.findall('a[5-9a-z]b','a1b a3b a9b abb a\nb'))#
print(re.findall('a[^5-9a-z]b','a1b a3b a9b abb a\nb'))#中括号是取反
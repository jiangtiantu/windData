# 1. 启动Wind API 接口
from WindPy import *

w.start()

# 2. 命令区分大小写，且“w.”不能省略
如：w.tdaysoffset(-1)不能写成tdaysoffset(-1)，或者w.TDaysOffset(-1)；

# 3. 中文以及单字节码和双字节码的问题
# 中文常使用双字节编码，这在Python中使用时就会错误。比如引号、逗号、括号等；

# 输入的字符串中若存在中文，有的平台可以直接输入中文，而有的需要使用unicode编码，即如：u”上证50”

# 4. 品种、指标、参数等引号内的部分不区分大小写
# 比如w.wsd('090007.IB','close',Sys.Date()-5,Sys.Date(),'Priceadj=F;tradingcalendar=NIB')

# 和w.wsd('090007.ib','CLOSE',Sys.Date()-5,Sys.Date(),'Priceadj=f;tradingcalendar=nib') 一样；

# 5. 参数支持list输入
# 比如w.wss("600000.SH,600005.SH,600004.SH,600007.SH","roe_avg,roa","rptDate=20121231")

# 可以写成：

#    code=['600000.SH','600005.SH','600004.SH']

#    field=['roe_avg','roa']

#    w.wss(code,field,"rptDate=20121231")

# 6. 时间、日期支持Python语言的时间、日期格式
# 比如w.wsd('600000.SH','open','20130505')

# 也可以写成w.wsd('600000.SH','close','20130303',datetime.today())

# 7. 参数中有缺省值的可以不用输入
# 比如w.wsd定义为w.wsd(codes, fields, beginTime, endTime = None, options = None)，可选参数和结束时间都有缺省值，因此用户可以不输入可选参数，也可以不输入结束时间。不输入时使用缺省值。

# 如：w.wsd('600000.SH','open','20130505')等同于w.wsd('600000.SH','open','20130505',datetime.today())；

# 8. 可以带参数名输入
比如w.wsd定义为w.wsd(codes, fields, beginTime, endTime = None, options = None)。

w.wsd("600000.SH","high","2013-05-09",datetime.today(),"Period=W") 等同于

w.wsd("600000.SH","high","2013-05-09",datetime.today(),options="Period=W")等同于

w.wsd("600000.SH","high","2013-05-09",options="Period=W",endTime=datetime.today())

 

# 带参数名输入后，参数顺序就可以变化；

# 9. Showblank参数
# Showblank参数可以指定对返回的NaN单元进行特别处理，如：

# 把NaN用-1替换：

w.wsd('600001.sh','open,close','20130707','20130909','showblank=-1'); 

或w.wsd('600001.sh','open,close','20130707','20130909',showblank=-1); 



 

# 把NaN用0替换：

w.wsd('600001.sh','open,close','20130707','20130909','showblank=0'); 

或w.wsd('600001.sh','open,close','20130707','20130909',showblank=0);

# 10. 交易接口中Showfields参数
# 交易接口返回的内容的指标根据具体情况会有变化，而有的情况下，客户需要指定确切的返回字段和顺序，此时可以使用showfields参数。如：

w.tquery(1,logonid=1,'showfields=securitycode,Profit,securityBalance')

或：w.tquery(1,logonid=1,showfields='securitycode,Profit,securityBalance ')

# 11. ErrorCode定义
ErrorCode=0表示操作成功。

# 其他：

-40520001  未知错误 -40520002  内部错误

-40520003  系统错误 -40520004  登录失败

-40520005  无权限 -40520006  用户取消

-40520007  无数据 -40520008  超时错误      -40521010  超时错误

-40520009  本地WBOX错误 -40520010  需要内容不存在

-40520011  需要服务器不存在 -40520012  引用不存在

-40520013  其他地方登录错误 -40520014  未登录使用WIM工具，故无法登录

-40520015  连续登录失败次数过多

 

-40521001  IO操作错误 -40521002  后台服务器不可用

-40521003  网络连接失败 -40521004  请求发送失败

-40521005  数据接收失败 -40521006  网络错误

-40521007  服务器拒绝请求 -40521008  错误的应答

-40521009  数据解码失败 -40521010  网络超时

-40521011  频繁访问

 

-40522001  无合法会话 -40522002  非法数据服务

-40522003  非法请求 -40522004  万得代码语法错误

-40522005  不支持的万得代码 -40522006  指标语法错误

-40522007  不支持的指标 -40522008  指标参数语法错误

-40522009  不支持的指标参数 -40522010  日期与时间语法错误

-40522011  不支持的日期与时间 -40522012  不支持的请求参数

-40522013  数组下标越界 -40522014  重复的WQID

-40522015  请求无相应权限 -40522016  不支持的数据类型

-40522017  数据提取量超限

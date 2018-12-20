import hashlib
import datetime

KEY_VALUE = 'Itcast'
now = datetime.datetime.now()
m = hashlib.md5()
string = '%s%s' % (KEY_VALUE,now.strftime("%Y%m%d"))
m.update(string.encode('utf-8'))
value = m.hexdigest()
print(value)


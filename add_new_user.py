from pyad import *
#user = aduser.ADUser.from_cn("CISTRAININIG")
pyad.set_defaults(ldap_server="aashi.CISTRAINING.COM", username="aashima", password="123456")
ou = pyad.adcontainer.ADContainer.from_dn("OU=pdc, DC=CISTRAINING, DC=COM")
new_user = pyad.aduser.ADUser.create("aashiOU3", ou, password="Wipro@123456")
#new_user.set_user_account_control_setting("DONT_EXPIRE_PASSWD", True)

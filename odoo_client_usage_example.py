from Jumpscale import j

url = "https://incubaid.odoo.com"
db = "incubaid"
# username = "test"
username = "kristof@???"
password = "???"

import xmlrpc.client

common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
common.version()

uid = common.authenticate(db, username, password, {})

if not uid:
    raise RuntimeError("could not login")

models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))
r = models.execute_kw(db, uid, password, "res.partner", "check_access_rights", ["read"], {"raise_exception": False})

r2 = models.execute_kw(
    db,
    uid,
    password,
    "res.partner",
    "search",
    [[["is_company", "=", True], ["customer", "=", True]]],
    {"offset": 10, "limit": 5},
)
print(r2)

j.shell()

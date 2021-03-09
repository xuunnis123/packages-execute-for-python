import http.client
###authorization

conn = http.client.HTTPSConnection("api.zoom.us")

headers = {
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6ImVKQTU1QzhUVDZLUE1HTW9VcnhmREEiLCJleHAiOjE2MTU4ODQ0NDQsImlhdCI6MTYxNTI3OTY0NX0._ha_XlliNPex8DRnKKLgRcFvwM7o7rA7zk69FVIcy4g",
    'content-type': "application/json"
    }

conn.request("GET", "/v2/users?status=active&page_size=30&page_number=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

'''
#get UserId
conn = http.client.HTTPSConnection("api.zoom.us")

headers = { 'authorization': "Bearer  101867" }

conn.request("GET", "/v2/users?page_size=30&status=active", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
###

conn = http.client.HTTPSConnection("api.zoom.us")

headers = {
    'authorization': "Bearer 39ug3j309t8unvmlmslmlkfw853u8",
    'content-type': "application/json"
    }

conn.request("GET", "/v2/users?status=active&page_size=30&page_number=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
'''

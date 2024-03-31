import requests

params = {
    'type': 'user-id',
    'action': 'set',
    'key': 'INSERT-KEY-HERE',
}

openldap_event_dictionary = {'username': 'dthomas', 'group': 'employees', 'ip': '192.168.11.111'}

# input = open(sys.argv[-1])
# output = open("/output/foobar.out", "a")
# for line in input:

#     #  Pulling values out of list
#     values_list = re.sub(r"\s+", " ", line).split(' ')

#     #  Filling openldap_event_dictionary
#     openldap_event_dictionary['ip'] = values_list[3]
#     openldap_event_dictionary['username'] = values_list[4]
#     openldap_event_dictionary['group'] = values_list[5]
#     output.write(' '.join(openldap_event_dictionary.keys()))
#     output.write(' '.join(openldap_event_dictionary.values()))

# #  Closing output file
# output.close

#  Login XML Payload string
login_payload = '''<uid-message>
  <type>update</type>
  <payload>
    <login>
      <entry name="{group}\{username}" ip="{ip}" timeout="60"/>
    </login>
  </payload>
</uid-message>'''.format(**openldap_event_dictionary)

#  Convert the above string to file like object.

files = {
    'file': login_payload.encode('utf-8')
}

# response = requests.post('http://127.0.0.1:5000/api/', params=params, files=files, verify=False)
response = requests.post('http://127.0.0.1:5000/api/', params=params, data=login_payload.encode('utf-8'), verify=False)
print(response.text)
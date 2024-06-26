import requests,sys,re

params = {
    'type': 'user-id',
    'action': 'set',
    'key': '',
}

#  Creating empty dictionary that will hold username,group
#  and ip found in openldap login event.
openldap_event_dictionary = {'username': '', 'group': '', 'ip': ''}

input = open(sys.argv[-1])
output = open("/output/foobar.out", "a")

#  Getting data found from regex's.
line = input.readline()

#  Pulling values out of line and putting them in
#  a list.
values_list = re.sub(r"\s+", " ", line).split(' ')

#  Filling openldap_event_dictionary
openldap_event_dictionary['ip'] = values_list[3]
openldap_event_dictionary['username'] = values_list[4]
openldap_event_dictionary['group'] = values_list[5]

#  Login XML Payload string
login_payload = '''<uid-message>
  <type>update</type>
  <payload>
    <login>
      <entry name="{group}\{username}" ip="{ip}" timeout="60"/>
    </login>
  </payload>
</uid-message>'''.format(**openldap_event_dictionary)

#  Converting to a byte string to simulate a file being
#  read.
files = {
    'file': login_payload.encode('utf-8')
}

#  Posting data found to Palo Alto XML api.
response = requests.post('https://10.30.11.11/api/', params=params, files=files, verify=False)
#  Writting response to log file. Closing file handler.
output.write(response.text)
output.close()

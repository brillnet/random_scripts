import re,sys,requests

palo_api_info = {'api_url':'https://10.30.11.11/api/?type=user-id&action=set&key=',
                 'key':'ajksndhf98789ajsdkf89yaj032==='}
openldap_event_dictionary = {'username': '', 'group': '', 'ip': ''}

input = open(sys.argv[-1])
output = open("/output/foobar.out", "a")
for line in input:

    #  Pulling values out of list
    value_list = re.sub(r"\s+", " ", line).split(' ')

    #  Filling openldap_event_dictionary
    openldap_event_dictionary['ip'] = values_list[3]
    openldap_event_dictionary['username'] = values_list[4]
    openldap_event_dictionary['group'] = values_list[5]
    output.write(' '.join(openldap_event_dictionary.keys())
    output.write(' '.join(openldap_event_dictionary.values())

#    output.write(line)
output.close


#  Login XML Payload string
login_payload = '''<uid-message>
  <type>update</type>
  <payload>
    <login>
      <entry name="{group}\{username}" ip="{ip}" timeout="60"/>
    </login>
  </payload>
</uid-message>'''.format(**openldap_event_dictionary)

headers = {'Content-Type': 'application/xml'}

try:
    requests.post('{api_url}{key}'.format(**palo_api_info),
                        data=login_payload, headers=headers,timeout=3).text
except requests.exceptions.ConnectionError:
    print("A connection error occurred. Please check your internet connection.")
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

print('{api_url}{key}'.format(**palo_api_info))
print(login_payload)

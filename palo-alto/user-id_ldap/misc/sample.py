from flask import Flask, request, jsonify
from lxml import etree

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def xml_endpoint():

    # if request.content_type != 'application/xml':
    #     return jsonify({"error": "Unsupported Media Type"}), 415

    try:
        xml_payload = request.data.decode('utf-8')
        xml_data = etree.fromstring(xml_payload)
        # Process your XML data here
        # For demonstration, let's just echo back the root tag name

        response_data = {"rootTagName": xml_data.tag}
        return jsonify(response_data), 200
    except etree.XMLSyntaxError:
        return jsonify({"error": "Invalid XML"}), 400

if __name__ == '__main__':
    app.run(debug=True) 
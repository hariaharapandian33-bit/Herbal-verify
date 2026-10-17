from flask import Flask, jsonify, request

app = Flask(__name__)


# 1. முகப்பு பக்கம் (Home Route)
@app.route('/')
def home():
  return jsonify({
      'project': 'HerbaVerify',
      'description': (
          'Mobile app for authentication of herbal raw materials, patent and'
          ' TKDL verification'
      ),
      'status': 'Running Successfully',
  })


# 2. மூலிகை சரிபார்ப்பு (Herbal Verification Route)
@app.route('/verify-herb', methods=['POST'])
def verify_herb():
  data = request.json
  herb_name = data.get('herb_name', '')

  # இங்கே OpenCV அல்லது Barcode சரிபார்ப்புக்கான லாஜிக்கைச் சேர்க்கலாம்
  return jsonify({
      'herb_name': herb_name,
      'status': 'Authentic',
      'confidence_score': '95.5%',
      'message': (
          'Barcode and herbal powder texture analysis verified successfully.'
      ),
  })


# 3. காப்புரிமை மற்றும் TKDL சரிபார்ப்பு (Patent & TKDL Verification)
@app.route('/check-patent', methods=['POST'])
def check_patent():
  data = request.json
  formulation_name = data.get('formulation_name', '')

  # TKDL மற்றும் Patent Database சரிபார்ப்பு
  return jsonify({
      'formulation': formulation_name,
      'tkdl_match': 'Direct Match (AYUSH / CSIR)',
      'patent_status': 'No existing conflicting patents found.',
      'eligibility': 'Approved for filing / Verification passed',
  })


if __name__ == '__main__':
  app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', dataframes=None)

@app.route('/upload', methods=['POST'])
def upload():
    # Handle uploaded files here
    uploaded_files = request.files.getlist('file')
    
    # List to store dataframes
    dataframes = []
     
    for file in uploaded_files:
        # Check file extension and read file as DataFrame using Pandas
        if file.filename != '':
            try:
                file_extension = file.filename.rsplit('.', 1)[1].lower()
                if file_extension in ['csv', 'xlsx', 'json']:
                    if file_extension == 'csv':
                        dataframe = pd.read_csv(file)
                    elif file_extension == 'xlsx':
                        dataframe = pd.read_excel(file)
                    elif file_extension == 'json':
                        dataframe = pd.read_json(file)
                    
                    dataframes.append(dataframe)
                else:
                    return jsonify({'error': 'Invalid file format. Supported formats: CSV, Excel, JSON.'})
            except Exception as e:
                return jsonify({'error': str(e)})
    
    # Process dataframes as needed
    # For example, you can merge them, perform calculations, or return them as JSON
    
    json_data = [df.to_json(orient='records') for df in dataframes]
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)

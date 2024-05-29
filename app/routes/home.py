import os
from flask import render_template
from app import app

# Get the filename of the generated JavaScript bundle
js_bundle_dir = os.path.join(app.static_folder, 'assets')
js_bundle_filename = [f for f in os.listdir(js_bundle_dir) if f.endswith('.js')][0]  # Assuming there's only one .js file

# Extract the hash from the filename (assuming the format is "index-{hash}.js")
bundle_hash = js_bundle_filename.split('-')[1]

@app.route('/')
def index():
    return render_template('index.html', bundle_hash=bundle_hash)

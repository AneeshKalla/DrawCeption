from flask import Flask, render_template

print("worked")

app = Flask(__name__)

api_key = 'acc_123214ecf4f0a57'
api_secret = 'fee73d3021ed776c284ef5c6797f2306'

@app.route('/')
def index():
  return("hello world")
    #return render_template('index.html')

@app.route('/about')
def about():
    return 'This is the about page.'


@app.route('/process', methods=['POST'])
def process_image():
    # Get the image data URL from the request
    data = request.json
    image_data_url = data['image']

    # Remove the header from the data URL
    image_data = image_data_url.split(',')[1]

    # Decode the base64 image data
    image_bytes = io.BytesIO(base64.b64decode(image_data))

    print("test: " + str(type(image_bytes)))

    # Open the image using PIL
    image = Image.open(image_bytes).convert('RGBA')

    print(type(image), file=sys.stderr)

    # Perform your image processing operations on the image here
    # ...

    # Save the processed image to a file or create a new data URL
    pre_image_path = 'pre_image.png'
    image.save(pre_image_path)
    print(image)

    files = {'image': open(pre_image_path, 'rb')}
    headers = {'Authorization': 'Basic ' + base64.b64encode((api_key + ':' + api_secret).encode()).decode()}

    # Make the API request
    response = requests.post('https://api.imagga.com/v2/tags', files=files, headers=headers)
    print(response.json())


    # Return the path or data URL of the processed image
    return redirect(url_for('display_image'))

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)



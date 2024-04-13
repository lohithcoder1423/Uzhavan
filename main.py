from flask import Flask, render_template, request, redirect, url_for
import openai
import urllib.request
x = 4
y = 2
z = 1
nn = []
pn=[]
kn=[]
ll = []
vv = []
kk = []

Main_url = "your IP_address"  # Replace with the actual IP address of your NodeMCU
def send(url):
    urllib.request.urlopen(url)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ulavan.html')


@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        # Get data from the text box
        user_input = request.form['user_input']

        # Process the data (you can perform any operation here)
        processed_data = user_input
        user_input1 = request.form['user_input1']

        # Process the data (you can perform any operation here)
        processed_data1 = user_input1
        user_input2 = request.form['user_input2']

        # Process the data (you can perform any operation here)
        processed_data2 = user_input2
        user_input3 = request.form['user_input3']

        # Process the data (you can perform any operation here)
        processed = user_input3

         # Convert input to uppercase as an example
        # Redirect to the result page with processed data
        global n, p, k
    n = int(processed_data)
    p = int(processed_data1)
    k = int(processed_data2)
    user_input = str('chennai')

    def find_max(*args):
        max_val = max(args, key=lambda value: int(value))
        return int(max_val)

    # Input

    a = len(str(n))
    b = len(str(p))
    c = len(str(k))
    e = []
    d = 0
    f = 0
    h = 0
    g = 0
    x = 4
    y = 2
    z = 1
    m = []
    j = 0

    # Finding the maximum value and its length
    max_val = find_max(n, p, k)
    max_length = len(str(max_val)) - 1

    j = 10 ** max_length
    x *= j
    y *= j
    z *= j

    print(j)
    print(max_length)

    print(j)
    print(x, y, z)

    # Adding the appropriate power of 10 to each variable
    power_of_ten = 10 ** max_length
    n += power_of_ten
    p += power_of_ten
    k += power_of_ten
    x += power_of_ten
    y += power_of_ten
    z += power_of_ten

    print(n, p, k)
    print(x, y, z)

    # Calculating accuracy
    y_true = [x, y, z]
    y_pred = [n, p, k]
    nn = x - n
    pn = y - p
    kn = z - k
    if n!=x:
      nn = nn
    else:
        nn = "none"
    if p!=y:
       pn = pn
    else:
        pn = "none"
    if k!=z:
       kn = kn
    else:
        kn = "none"
               #DEfeact


    correct_count = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    accuracy = correct_count / len(y_true)
    accuracy_percentage = accuracy * 100



    print(f"Farming in the field percentage: {accuracy_percentage:.2f}%")

    # Set your OpenAI API key
    openai.api_key = "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"

    def chat_with_gpt(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a valid engine name
            prompt=prompt,
            max_tokens=150  # You can adjust the maximum number of tokens in the response
        )

        return response.choices[0].text.strip()

    if __name__ == "__main__":
        prompt = f"answer should be like bulet points nitrogen:{n}kg phosporus:{p}kg potasium:{k}kg what kind of crops can be grown in this field and how it can be grown in India the accuracy we got is {accuracy_percentage} according to the nutritient"
        response = chat_with_gpt(prompt)


        print("Chatbot:", response)
    if accuracy_percentage < 20:
        response = "add sufficient fertilizer"



    import requests

    api_key = 'your_key'
    user_input = processed


    weather_data = requests.get(
        f"your_key)

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºF")
        processed_data3 = f"The weather in {user_input} is: {weather} and temp is: {temp}ºF"
        return redirect(url_for('result', processed_data=processed_data,processed_data1=processed_data1,processed_data2=processed_data2,accuracy_percentage=accuracy_percentage,response=response,processed_data3=processed_data3,nn=nn,pn=pn,kn=kn))

@app.route('/result/<processed_data>/<processed_data1>/<processed_data2>/<accuracy_percentage>/<response>/<processed_data3>/<nn>/<pn>/<kn>')
def result(processed_data,processed_data1,processed_data2,accuracy_percentage,response,processed_data3,nn,pn,kn):
    return render_template('ulavan.html', processed_data=processed_data,processed_data1=processed_data1,processed_data2=processed_data2,accuracy_percentage=accuracy_percentage,response=response,processed_data3=processed_data3,nn=nn,kn=kn,pn=pn)

@app.route('/answer', methods=['POST'])
def show_answer():
    if request.method == 'POST':
        # Get data from the text box
        user_ques = request.form['ques']
        openai.api_key = "Your_key"

        def chat_with_gpt(prompt1):
            response1 = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt1,
                max_tokens=150
            )

            return response1.choices[0].text.strip()

        if __name__ == "__main__":
            prompt1 = f'{user_ques} your name is Uzhavan in india'
            response1 = chat_with_gpt(prompt1)

            print("Chatbot:", response1)
            return redirect(url_for('answer', response1=response1))


@app.route('/show_answer/<response1>')
def answer(response1):
    return render_template('ulavan.html', response1=response1)

@app.route('/on', methods=['POST'])
def motor_on():
    # Handle the button click event here
    send(Main_url+"/motoron")
    on = 'motor is on now'
    return render_template("ulavan.html",on=on)


@app.route('/off', methods=['POST'])
def motor_off():
    # Handle the button click event here
    send(Main_url+"/motoroff")
    off = 'motor is off now'
    return render_template("ulavan.html",off=off)


@app.route('/auto', methods=['POST'])
def motor_auto():
    # Handle the button click event here
    send(Main_url+"/auto")
    auto = 'motor is in auto mode now'
    return render_template("ulavan.html",auto=auto)
@app.route('/protect', methods=['POST'])
def pro():
    # Handle the button click event here
    send(Main_url+"/pro")
    pro = 'Field is in control'
    return render_template("ulavan.html",pro=pro)

@app.route('/rest', methods=['POST'])
def res():
    # Handle the button click event here
    send(Main_url+"/rest")
    rest = 'Field is not in control'
    return render_template("ulavan.html",rest=rest)

@app.route('/fer', methods=['POST'])
def fer():
    # Handle the button click event here
   
    
    return render_template("ulavan.html",nn=nn,pn=pn,kn=kn)


if __name__ == '__main__':
   app.run(debug=True)



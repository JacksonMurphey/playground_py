from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('playground.html')

@app.route('/play')
def play():
    return render_template('playground.html', num=0)

@app.route('/play/<int:num>')
def repeat(num):
    return render_template('playground.html', num=num)

@app.route('/play/<int:num>/<color>')
def change(num, color):
    return render_template('playground.html', num=num, color=color)




if __name__=='__main__':  #Ensure this file is being run directly and not from a different module.
    app.run(debug=True)   #Run the app in 'DEBUG' mode. this should be the last statement in our files. 
from flask import  Flask, render_template 
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('checkerboard.html')
@app.route('/4')
def smallerBoard():
    return render_template('smallerBoard.html')

@app.route('/<int:loop>/<int:loop2>')
def multiplyBoard(loop,loop2):
    return render_template('multiplyBoard.html', loop_this_number_of_times = loop, loop_this_number_of_times2 = loop2)

if __name__=="__main__" :
    app.run(debug=True)


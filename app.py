from flask import Flask, render_template, request, redirect
import bokeh
import quandl
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_quand():

    if request.method == 'GET':
        return render_template('userinfo_lulu.html')
    else:
        # request was a POST
        wk = 'WIKI/'
        stk = request.form['name_lulu']
        wkstk = wk + stk

        # Get the data for Coca-cola
        data = quandl.get(wkstk, start_date="2016-01-01", end_date="2018-01-01", api_key="ykWz-sF54JasM3SZyA5h")
        source = ColumnDataSource(data)

        output_file("test.html")
        p = figure(x_axis_type="datetime")
        p.line(x='Date', y='Close', source=source)
        show(p)

        return redirect('/')



if __name__ == "__main__":
    app.run(port=33507)



###########################



#app = Flask(__name__)

#@app.route('/')
#def index():
 # return render_template('index.html')

#@app.route('/about')
#def about():
 # return render_template('about.html')

#if __name__ == '__main__':
 # app.run(port=33507)

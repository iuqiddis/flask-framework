from flask import Flask,render_template,request,redirect
import bokeh
import quandl
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

app_quand = Flask(__name__)

app_quand.vars={}


@app_quand.route('/index_quand', methods=['GET', 'POST'])
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

        return redirect('/index_quand')



if __name__ == "__main__":
    app_quand.run()
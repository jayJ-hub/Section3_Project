from flask import Flask, render_template,url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_app.predict import process_input
app = Flask(__name__)
# For Security
app.config['SECRET_KEY'] = "mysecretkey"

class MusicInput(FlaskForm):
    music_name = StringField("Input Music Here")
    submit = SubmitField("Submit!")

@app.route('/',methods=["GET","POST"]) 
def index():
    # Create object that process user input
    form = MusicInput()
    # After user hit submit button
    if form.validate_on_submit():
        music_name =  form.music_name.data # data saved here
        music_name = music_name.replace(" ","-")
        return redirect(f'result/{music_name}')
    return render_template('index.html', form=form)


@app.route('/result/',defaults = {'num':0})
@app.route('/result/<uri>')
def show_result(uri):
    predicted_popularity = process_input(uri)    
    return f"Your Result: {predicted_popularity}"


if __name__ == '__main__':
   app.run(debug=True)
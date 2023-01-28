import pickle
from flask import Flask , render_template, request

#create an object of class Flask




app=Flask(__name__)
#Now firstly we need to Un-Dump our model 
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
    temp=request.form.get('temperature')
    tempra = [int(x) for x in temp]
    pred=model.predict([[tempra[0]]])
    output=round(pred[0],2)
    print(output)
    return render_template('index.html',prediction_text=f"total Revenue Earned is Rs.{output}")

if __name__=='__main__':
    app.run(debug=True) 
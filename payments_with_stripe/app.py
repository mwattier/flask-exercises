from flask import Flask ,render_template,request,url_for
import os
import stripe

app= Flask(__name__)

stripe_keys = {
  'secret_key': os.environ['SECRET_KEY'],
  'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']


@app.route('/')
   def index():
       return render_template('index.html',public_key=public_key)

@app.route('/thankyou')
   def thankyou():
   	    return render_template('thankyou.html')

@app.route('/payments',methods=['POST'])
   def payments():

   	   customer= stripe.Customer.create(email=request.form['stripeEmail'],
   	   	                                source=request.form['stripeToken'])
      

       #PAYMENT INFORMATION
       charge= stripe.Charge.create(
              
               customer=customer.id,
               amount=1999,
               currency='usd',
               description='donation'   

       	)
       
    return(redirect(url_for(thankyou)))



if __name__='__main__':
	app.run(debug='True')

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/about')
def aboutpage():
    return render_template("about.html")

@app.route('/', defaults = {'name' : "0"})
@app.route('/<name>')
def mainpage(name):
    return render_template("index.html" , name = name)


@app.route('/submit' , methods = ['GET'])
def submit():
    if request.method =='GET':

        s1 = request.args['ST']

        x=len(s1)  

        if x==0:
            return redirect(url_for('mainpage' , name = "0"))

        original_words = []

        str0 = ""

        for i in range(x):

            if s1[i]=="'" or s1[i]=="-" or s1[i]=="_":
                str0+=s1[i]
                continue
            
            if i+1<x and ( s1[i+1]==" " or s1[i+1]=="," or s1[i+1]=="?" or s1[i+1]=="!" or s1[i+1]==".") or i+1==x:
                if s1[i]>='A' and s1[i]<='Z' or s1[i]>='a' and s1[i]<='z' or s1[i]>='0' and s1[i]<='9':
                    str0+=s1[i]
                    original_words.append(str0)
                    str0=""
            else:
                str0+=s1[i]
        
        if str0!="" and (str0!="-" or str0!=":" or str0!="`"):
            original_words.append(str0)
            
        p=len(original_words)
                    
        return redirect(url_for('mainpage' , name = p))
        
    else: 
        return redirect(url_for('mainpage'))



if __name__=='__main__':
    app.run(debug = True)

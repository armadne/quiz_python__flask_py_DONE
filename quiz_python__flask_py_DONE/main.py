from flask import Flask , redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/" , methods=["POST", "GET"])
def home():
    
    first_question = ""
    second_question = ""
    third_question = ""
    fourth_question = ""
    fifth_question = ""
    
    point = 0 
    
    if request.method == "POST":
        first_question = request.form["first"]
        second_question = request.form["second"]
        third_question = request.form["third"]
        fourth_question = request.form["fourth"]
        fifth_question = request.form["fifth"]
        
        if first_question == "print()":
            point += 1
            
        elif second_question == "hello" :
            point += 1
            
        elif third_question == "12":
            point += 1
            
        elif fourth_question == "for , while":
            point += 1
            
        elif fifth_question == "while True:":
            point += 1
            
            
        return render_template("quiz.html", point=point, first_question=first_question, second_question=second_question, 
                           third_question=third_question, fourth_question=fourth_question, fifth_question=fifth_question)
            
            
    
        
        
    if not first_question or not second_question or not third_question or not fourth_question or not fifth_question:
        return render_template("quiz.html")
    
    
    
    




if __name__ == "__main__":
    app.run(debug=True)
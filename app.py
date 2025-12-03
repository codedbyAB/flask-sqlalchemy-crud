from flask import Flask, request, jsonify # 👉 If the client SENDS something → you need request.
from db import db
from models import User





app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"




db.init_app(app) #call the method named init_app on the object db.”



with app.app_context():
        db.create_all()



@app.route('/add', methods=["POST"])
def receive_data():  #Flask turns JSON → a Python dict
    store_data = request.get_json() #Once your JSON is parsed by Flask, it becomes a Python dict
    user = User(
           full_name = store_data["full_name"],
           dob = store_data["date"],
           career = store_data["career"]
           )
    db.session.add(user)
    db.session.commit()
    return user


        



@app.route('/del_row/<id>', methods=['DELETE'])          
def row_delete(id):
       #Before I delete I need to query data
        user_del = db.session.query(User).filter_by(id=id).first()
        if user_del is None:
               return "This user does not exist"
        
        db.session.delete(user_del)
        db.session.commit()
        return "User has been deleted successfully"

             



@app.route('/get_all', methods=["GET"])
def get_all():
       my_data = db.session.query(User).all()
       users = []
       for x in my_data:
              info_dict = {
                     "id": x.id,
                     "full_name": x.full_name,
                     "dob": x.dob,
                     "career": x.career
              }
              users.append(info_dict)
       return jsonify(users)
              







          
              
              
              
       
              
              
              
       
              
              
              
              
              
       

       
       
  
    
       
       




        
       
      
       

    
 
        
        


    

  
if __name__ == "__main__":
        app.run(debug=True)

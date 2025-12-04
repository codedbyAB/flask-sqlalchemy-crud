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
    return jsonify(user.to_dict()), 201


        



@app.route('/del_row/<id>', methods=['DELETE'])          
def row_delete(id):
       #Before I delete I need to query data
        user_del = db.session.query(User).filter_by(id=id).first()
        if user_del is None:
               return {"error": "This user does not exist"}, 404
        
        db.session.delete(user_del)
        db.session.commit()
        return {"Success": "User has been deleted."}, 200

             



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





@app.route('/get_id/<id>', methods=["GET"])
def get_id(id):
       user_id = db.session.query(User).filter_by(id=id).first()
       if user_id is None:
              return jsonify({"error": "User not found"}), 404
       
       return jsonify({
              "id": user_id.id,
              "full_name": user_id.full_name,
              "dob": user_id.dob,
              "career": user_id.career
       }), 200





@app.route('/update/<id>', methods=["PATCH"])
def update(id):
       update_user = db.session.query(User).filter_by(id=id).first()
       store_data = request.get_json()
       # update_user.full_name = store_data["full_name"]
       # update_user.dob = store_data["dob"]
       print(update_user.to_dict())

       if update_user is None:
              return "User does not exist"
       if "full_name" in store_data:
              update_user.full_name = store_data["full_name"]
       
       if "career" in store_data:
              update_user.career = store_data["career"]
       
       if "dob" in store_data:
              update_user.dob = store_data["dob"]

       
       db.session.commit()


       return jsonify(update_user.to_dict()), 200
          
       
      

      
     




     
      







          
              
              
              
       
              
              
              
       
              
              
              
              
              
       

       
       
  
    
       
       




        
       
      
       

    
 
        
        


    

  
if __name__ == "__main__":
        app.run(debug=True)

from pyscript import document, display


#list of members
club_members = ["Joaquin Hizon", "Eron Almiron", "Jeff De Jesus","Cassandra De Jesus","Sebastian Stan"]

def whitelist(e):
    
    #clearing the previous result to display the new message 
    document.getElementById("output").innerHTML = ""

   
    #getting the values
    first_name = document.getElementById("firstname").value
    last_name = document.getElementById("lastname").value
    full_name = first_name + " " + last_name

    #checking if inputted name is in the list
    is_member = full_name in club_members


    message = {
        True: "Congratulations "+ full_name +"! You are part of the Varsity team.",
        False: "Sorry "+ full_name +", your name is not on the list."
    }


    display(message[is_member], target="output")
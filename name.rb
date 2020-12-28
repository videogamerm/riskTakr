puts"Type your name."
name = gets
File.write("name.txt",name , mode: "w")
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['question_paper']
collection = db['questions']

collection.delete_many({})  # Clear old entries

# Complete sample questions with proper structure
sample_questions = [
    # Unit 1 - Group Q1 (Compulsory)
    {"subject": "fxe", "unit": "Unit 1", "question": "With the help of neat circuit diagram and waveform, explain the working of full wave bridge rectifier", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "With the help of neat circuit diagram and waveform, explain the working of full wave rectifier with centre tapped transformer.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},
      
      
      {"subject": "fxe", "unit": "Unit 1", "question": "Explain the V-I characteristics of p-n junction diode with neat diagram.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "With the help of diagram explain the working of Zener diode", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 1 - Group Q2 (Solve Any Two)
    {"subject": "fxe", "unit": "Unit 1", "question": "Compare half wave rectifier and full wave rectifier with center tapped transformer.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "Explain the line regulation in case of Zener diode.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "Explain the application of zener diode as a voltage regulator when the input is variable.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "A bridge rectifier is applied with input from a step-down transformer having turns ratio 8:1 and input 230V, 50 Hz. Calculate maximum, average and rms value of load current.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},
     #medium
     {"subject": "fxe", "unit": "Unit 1", "question": "A half wave rectifier circuit connected to a 230V, 50Hz source, through a transformer of turns ratio of 10:1. The rectifier is to supply power to a 500 Ohm resistor and diode forward resistance is 10 Ohm. Calculate maximum, average and rms value of output current.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "Explain the application of p-n junction diode as a full wave rectfier with centre tapped transformer with neat circuit diagram and input-output waveforms.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "Compare LED and Photodiode.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 1", "question": "give advantage of bridge rectifier with capacitor filter.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

    # Unit 2 - Group Q1 (Compulsory)
    {"subject": "fxe", "unit": "Unit 2", "question": "With the help of circuit diagram, explain how the BJT can be used as a switch?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Explain the different operating regions of a BJT with their biasing conditions and applications.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "fxe", "unit": "Unit 2", "question": "Explain the construction of BJT.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Draw and explain the circuit diagram of CE configuration of the transistor along with its output characteris cs.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 2 - Group Q2 (Solve Any Two)
    {"subject": "fxe", "unit": "Unit 2", "question": "Draw and explain the drain characteristics of n-channel enhancement type MOSFET.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Draw and explain the circuit diagram of CB configuration of the transistor along with its input characteristics.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Explain the working principle of JFET with neat diagram.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Compare BJT and MOSFET with respect to their characteristics and applications.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "fxe", "unit": "Unit 2", "question": "Explain BJT as a switch.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Explain voltage divider bias circuit.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Draw and Explain the output characteristics of CE configuration.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 2", "question": "Explain BJT region s of operation.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

    # Unit 3 - Group Q1 (Compulsory) - Adding Unit 3 questions for your test
    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the concept of feedback in amplifiers and its types.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "Derive the expression for voltage gain of common emitter amplifier.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "fxe", "unit": "Unit 3", "question": "Explain the concept of virtual ground and virtual short.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "Define and give typical values of the following op-amp parameters: i) PSRR ii) Input bias current.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 3 - Group Q2 (Solve Any Two)
    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the frequency response of RC coupled amplifier.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "Draw and explain the circuit of differential amplifier.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the concept of common mode rejection ratio (CMRR).", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "Design a common emitter amplifier for given specifications.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "fxe", "unit": "Unit 3", "question": "Define and give typical values of the following op-amp parameters: i) CMRR ii) Input offset voltage.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "An op-amp is used in a non inverting mode with R1=10KΩ,RF=12kΩ, VCC=±15. Calculate Output voltage for i)Vin =250mV ii) Vin= 3V and comment on the result.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "For the inverting amplifier using Op-Amp, if RF=100KΩ ,R1=10KΩ, V CC= ±10V, Vi= 2V i) Calculate output voltage ii) Is the result in part (i) practically possible? Justify.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 3", "question": "define CMRR.Derive the expression for CMRR and explain its importance in differential amplifier performance.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #unit4----->> 
      # Unit 4 - Group Q1 (Compulsory) - Adding Unit 4 questions for your test
    {"subject": "fxe", "unit": "Unit 4", "question": "Name the basic gates. Draw symbol and their truth table. 2. i) Convert (132.52)10 to binary.ii) Convert (110111010111.101101)2 to octal.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "Why NAND and NOR gates are called as universal gates? Draw truth table and symbol.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "fxe", "unit": "Unit 4", "question": "Convert (25)10 and (12)10 into binary numbers and add binary numbers. Perform (9)10-(4)10 using 1's complement method .", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "State law of commutation, law of association and law of distribution.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 4 - Group Q2 (Solve Any Two)
    {"subject": "fxe", "unit": "Unit 4", "question": "State and prove De' Morgan's sum & product theorem with the help of truth table.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "Design and implement full adder circuit. Write the expressions for sum and carry", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "What is flipflop? Draw & Explain the working D flip-flop.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "Name the derived gates. Draw symbol and their truth table.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "fxe", "unit": "Unit 4", "question": " i) Convert (155.33)10  to binary.ii) Convert (110111010111.101101)2 to hexadecimal.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": " i) Convert (26)10and (32)10 into binary numbers and add binary numbers. ii) Perform (8)10 (3)10 using 1's complement method.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "What is flipflop? Draw & Explain the working SR flip-flop.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 4", "question": "Draw NAND gate implementa on of the SR flip-flop and explain its working.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

      #unit5----->> 
      # Unit 5 - Group Q1 (Compulsory) - Adding Unit 5 questions for your test
    {"subject": "fxe", "unit": "Unit 5", "question": "Explain modes of transmission.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Write a short note on coaxial cable and optical fibre cable", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "fxe", "unit": "Unit 5", "question": "Write short note on Frequency modulation.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Draw and explain electromagnetic spectrum along with their applications.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 5 - Group Q2 (Solve Any Two)
    {"subject": "fxe", "unit": "Unit 5", "question": "Explain the elements of communication system with the help of block diagram.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Explain GSM architecture.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Write short note on Amplitude modulation.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Explain different types of cables used in communication system with neat diagrams.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "fxe", "unit": "Unit 5", "question": "Draw and explain electromagnetic spectrum along with their applications.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Explain the types of twisted pair cables.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "What is the need of modula on? Explain amplitude modulation with waveforms.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "fxe", "unit": "Unit 5", "question": "Compared wired and wireless communication.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},



     #OOP -------------->>>

       # Unit 1 - Group Q1 (Compulsory)
    {"subject": "oop", "unit": "Unit 1", "question": "What is inline function? What are their advantages?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "What is Friend Function? Explain with suitable sample code in C++. What are the merits and demerits of using friend function?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},
      
      
      {"subject": "oop", "unit": "Unit 1", "question": "List and explain various features of OOP.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "Compare Procedure oriented programming Vs Object oriented programming.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 1 - Group Q2 (Solve Any Two)
    {"subject": "oop", "unit": "Unit 1", "question": "Write a program in C++ to use scope resolution operator.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "Write a C++ program to calculate the area and circumference of circle using member function outside the class.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "What is data hiding in a class? Explain with suitable sample code in C++ and diagram.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "Write a cpp program to display information of 2 employees . Declare a class of employee. Create an array of class objects. Read and display the content of array .", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},
     #medium
     {"subject": "oop", "unit": "Unit 1", "question": "what is the significance of static data and member functions in C++?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "Explain the static variable in C++ with help of sample code.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "How does a C++ structure differ from a C++ class? ", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 1", "question": "Define terms: encapsulation, abstraction, polymorphism, binding .", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

    # Unit 2 - Group Q1 (Compulsory)
    {"subject": "oop", "unit": "Unit 2", "question": "What is ambiguity problem in inheritance and how is it resolved?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "Explain friend class with help of sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "oop", "unit": "Unit 2", "question": "Explain virtual base class & virtual function with a suitable sample code in C++?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "What does inheritance mean in C++? Explain Multilevel Inheritance with example", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 2 - Group Q2 (Solve Any Two)
    {"subject": "oop", "unit": "Unit 2", "question": "Explain abstract class concept along with sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "What is purpose of virtual keyword in inheritance? Explain with suitable example.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "What are different types of inheritance in C++, Explain with suitable diagrams.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "What is meant by initialization list? Explain with suitable sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "oop", "unit": "Unit 2", "question": "Explain multiple inheritance with example.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "Write a C++ Program to find Area of Rectangle using inheritance.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "Demonstrate hybrid inheritance with the help of suitable example.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 2", "question": "Write a C++ program to create a base class Person (name and phone number).Derive Academic Performance (Degree, percentage) class from Person class. Display biodata of the person.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

    # Unit 3 - Group Q1 (Compulsory) - Adding Unit 3 questions for your test
    {"subject": "oop", "unit": "Unit 3", "question": "Compare run time and compile time polymorphism in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "Explain pure virtual function. Illustrate use of pure virtual function in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "oop", "unit": "Unit 3", "question": "What is role of this pointer in C++ programming?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "What is operator overloading? Why is it necessary to overload an operator?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 3 - Group Q2 (Solve Any Two)
    {"subject": "oop", "unit": "Unit 3", "question": "Compare operator overloading and function overloading.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "What is role of runtime and compile-time polymorphism for a C++ programs?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "Explain call-by-value and call-by-reference with suitable code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "Write a program that will calculate the area of rectangle, square and circle. Using function overloading.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "oop", "unit": "Unit 3", "question": "Write a C++ program to implement a class called string, which represents the array of characters and its length. Implement strings concatenation using operator overloading for binary + operator.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "How array can be represented using pointer? Explain pointer arithmetic.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "What are void pointer and invalid pointer? Explain with suitable code in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 3", "question": "What is pointer in programming? Explain with suitable code in C++. What are its advantages?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #unit4----->> 
      # Unit 4 - Group Q1 (Compulsory) - Adding Unit 4 questions for your test
    {"subject": "oop", "unit": "Unit 4", "question": "Explain generic programming with class & function template?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "What are types of templates? Explain with suitable sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "oop", "unit": "Unit 4", "question": "What is generic programming? What are its advantages?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "Explain Exception handling with sample code in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 4 - Group Q2 (Solve Any Two)
    {"subject": "oop", "unit": "Unit 4", "question": "What are advantages of Exception handling in programming?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "Explain the three keywords for Exception handling in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "What is default catch in exception handling? Explain with suitable sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "Explain multiple catch blocks in exception handling.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "oop", "unit": "Unit 4", "question": "The exception handling mechanism C++ deals with exceptions by performing four tasks.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "Write a C++ program with a function which can add numbers with data types like integer double, float. Use appropriate concept of programming in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "Write a C++ program to Create a class template to represent generic vectors. Include following functions: To create a vector, To modify the value of given vector, Multiply vector by a scalar value, Display vector", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 4", "question": "What is concept of nested try/catch blocks? Explain with suitable code.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

      #unit5----->> 
      # Unit 5 - Group Q1 (Compulsory) - Adding Unit 5 questions for your test
    {"subject": "oop", "unit": "Unit 5", "question": "Explain file input and output streams with suitable diagram.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "Explain role of istream and ostream classes for file handling in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
      {"subject": "oop", "unit": "Unit 5", "question": "What are two methods for opening a file? Explain with suitable code syntax.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "Explain various file opening modes in brief.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Unit 5 - Group Q2 (Solve Any Two)
    {"subject": "oop", "unit": "Unit 5", "question": "What are the possible reasons for errors during file operations?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "Describe how to determine number of objects in a file with suitable sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "What are steps involved in using a file in a C++ program?", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "Explain data hierarchy in programming. (data types/tree).", 
     "difficulty": "easy", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},

     #medium
      {"subject": "oop", "unit": "Unit 5", "question": "Write C++ Program for implementation of Error handling functions during file handling.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "Explain tellp(), tellg(), seekp() and seekg() functions with suitable code.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "What are the possible reasons for errors during file operations?", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 3, "group_instruction": "Solve Any Two"},
    
    {"subject": "oop", "unit": "Unit 5", "question": "Write C++ program for writing student data (Roll No, Name, Address, MobileNo) to a file and read the same. Use appropriate classes from fstream.h header file.", 
     "difficulty": "medium", "type": "theory", "examtype": "insem", "marks": 4, 
     "unit_group": "2", "option_id": 4, "group_instruction": "Solve Any Two"},


     #Endsem database------->>

    # Q1 - Unit 1 - Compulsory
    {"subject": "fxe", "unit": "Unit 1", "question": "Define energy band diagram and explain conduction in semiconductors.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "fxe", "unit": "Unit 1", "question": "Draw and explain V-I characteristics of Zener diode.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

       #medium--->>
      {"subject": "fxe", "unit": "Unit 1", "question": "Define energy band diagram and explain conduction in semiconductors.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "fxe", "unit": "Unit 1", "question": "Draw and explain V-I characteristics of Zener diode.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

    # Q2 - Unit 2 - Compulsory
    {"subject": "fxe", "unit": "Unit 2", "question": "Explain transistor action in CE configuration.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "fxe", "unit": "Unit 2", "question": "What are the different regions of operation in a BJT?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
     {"subject": "fxe", "unit": "Unit 2", "question": "Explain transistor action in CE configuration.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "fxe", "unit": "Unit 2", "question": "What are the different regions of operation in a BJT?", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Q3 - Unit 3 - OR groups
    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the working of a clipping circuit.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Explain clamping with suitable circuit and waveform.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the operation of a voltage regulator using Zener diode.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Describe the load and line regulation in detail.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Draw and explain UJT triggering circuit.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the working of SCR with V-I characteristics.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

     #medium
     {"subject": "fxe", "unit": "Unit 3", "question": "Explain the working of a clipping circuit.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Explain clamping with suitable circuit and waveform.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the operation of a voltage regulator using Zener diode.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Describe the load and line regulation in detail.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Draw and explain UJT triggering circuit.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 3", "question": "Explain the working of SCR with V-I characteristics.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

    # Q4 - Unit 4 - OR groups
    {"subject": "fxe", "unit": "Unit 4", "question": "Compare amplifier classes A, B and C.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Explain RC coupled amplifier with diagram.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Explain operation of differential amplifier.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Describe OPAMP as integrator with waveforms.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Explain gain and bandwidth in amplifiers.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Describe the frequency response of CE amplifier.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

     #medium
      {"subject": "fxe", "unit": "Unit 4", "question": "Compare amplifier classes A, B and C.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Explain RC coupled amplifier with diagram.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Explain operation of differential amplifier.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Describe OPAMP as integrator with waveforms.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Explain gain and bandwidth in amplifiers.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 4", "question": "Describe the frequency response of CE amplifier.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

    # Q5 - Unit 5 - OR groups
    {"subject": "fxe", "unit": "Unit 5", "question": "Explain types of filters used in power supplies.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Draw and explain pi-type filter.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Explain LCD construction and working.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Compare LCD and LED.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Describe the working of opto-isolator.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Explain IR sensor and its applications.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

     #medium
     {"subject": "fxe", "unit": "Unit 5", "question": "Explain types of filters used in power supplies.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Draw and explain pi-type filter.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Explain LCD construction and working.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Compare LCD and LED.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Describe the working of opto-isolator.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "fxe", "unit": "Unit 5", "question": "Explain IR sensor and its applications.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},




     #oop ----->>
      # Q1 - Unit 1 - Compulsory
    {"subject": "oop", "unit": "Unit 1", "question": "What is inline function? What are their advantages?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "oop", "unit": "Unit 1", "question": "hat is Friend Function? Explain with suitable sample code in C++. What are the merits and demerits of using friend function?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

       #medium--->>
      {"subject": "oop", "unit": "Unit 1", "question": "List and explain various features of OOP.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "oop", "unit": "Unit 1", "question": "Compare Procedure oriented programming Vs Object oriented programming.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

    # Q2 - Unit 2 - Compulsory
    {"subject": "oop", "unit": "Unit 2", "question": "What is ambiguity problem in inheritance and how is it resolved.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "oop", "unit": "Unit 2", "question": "Explain friend class with help of sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},

     #medium
     {"subject": "oop", "unit": "Unit 2", "question": "Explain virtual base class & virtual function with a suitable sample code in C++?", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Compulsory"},

    {"subject": "oop", "unit": "Unit 2", "question": "What does inheritance mean in C++? Explain Multilevel Inheritance with example", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 3, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Compulsory"},


    # Q3 - Unit 3 - OR groups
    {"subject": "oop", "unit": "Unit 3", "question": "Compare run time and compile time polymorphism in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "Explain pure virtual function. Illustrate use of pure virtual function in C++", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "What is role of this pointer in C++ programming?.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "What is operator overloading? Why is it necessary to overload an operator?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "Compare operator overloading and function overloading.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "What is role of runtime and compile-time polymorphism for a C++ programs?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

     #medium
     {"subject": "oop", "unit": "Unit 3", "question": "Explain call-by-value and call-by-reference with suitable code in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "Write a program that will calculate the area of rectangle, square and circle. Using function overloading.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "Write a C++ program to implement a class called string, which represents the array of characters and its length. Implement strings concatenation using operator overloading for binary + operator.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "How array can be represented using pointer? Explain pointer arithmetic.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "What are void pointer and invalid pointer? Explain with suitable code in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 3", "question": "What is pointer in programming? Explain with suitable code in C++. What are its advantages?", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

    # Q4 - Unit 4 - OR groups
    {"subject": "oop", "unit": "Unit 4", "question": "Explain generic programming with class & function template?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "What are types of templates? Explain with suitable sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "What is generic programming? What are its advantages?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "Explain Exception handling with sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "What are advantages of Exception handling in programming?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "Explain the three keywords for Exception handling in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

     #medium
      {"subject": "oop", "unit": "Unit 4", "question": "What is default catch in exception handling? Explain with suitable sample code in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "Explain multiple catch blocks in exception handling.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "The exception handling mechanism C++ deals with exceptions by performing four tasks.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "Write a C++ program with a function which can add numbers with data types like integer double, float. Use appropriate concept of programming in C++.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "Write a C++ program to Create a class template to represent generic vectors. Include following functions: To create a vector, To modify the value of given vector, Multiply vector by a scalar value, Display vector", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 4", "question": "what is concept of nested try/catch blocks? Explain with suitable code.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

    # Q5 - Unit 5 - OR groups
    {"subject": "oop", "unit": "Unit 5", "question": "Explain file input and output streams with suitable diagram.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Explain role of istream and ostream classes for file handling in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "What are two methods for opening a file? Explain with suitable code syntax.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Explain various file opening modes in brief.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "What are the possible reasons for errors during file operations?", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Describe how to determine number of objects in a file with suitable sample code in C++.", 
     "difficulty": "easy", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},

     #medium
     {"subject": "oop", "unit": "Unit 5", "question": "What are steps involved in using a file in a C++ program?", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Explain data hierarchy in programming. (data types/tree).", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 4, 
     "unit_group": "1", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Write C++ Program for implementation of Error handling functions during file handling.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Explain tellp(), tellg(), seekp() and seekg() functions with suitable code.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "2", "option_id": 2, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "What are the possible reasons for errors during file operations?", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 1, "group_instruction": "Solve any one"},

    {"subject": "oop", "unit": "Unit 5", "question": "Write C++ program for writing student data (Roll No, Name, Address, MobileNo) to a file and read the same. Use appropriate classes from fstream.h header file.", 
     "difficulty": "medium", "type": "theory", "examtype": "endsem", "marks": 6, 
     "unit_group": "3", "option_id": 2, "group_instruction": "Solve any one"},


]

# Insert questions with error handling
try:
    result = collection.insert_many(sample_questions)
    print(f"✅ Successfully inserted {len(result.inserted_ids)} questions into database")
except Exception as e:
    print(f"❌ Error inserting questions: {e}")

# Alternative approach using composite keys
def create_composite_group_key(unit, unit_group):
    """Create a unique composite key for groups"""
    unit_num = unit.split()[-1]  # Extract number from "Unit 1", "Unit 2", etc.
    return f"{unit_num}_{unit_group}"

# Update existing questions to add composite keys (optional)
def update_existing_questions():
    """Update existing questions to include composite group keys"""
    try:
        questions = collection.find({})
        update_count = 0
        
        for q in questions:
            if 'unit_group' in q and 'unit' in q:
                composite_key = create_composite_group_key(q['unit'], str(q['unit_group']))
                collection.update_one(
                    {'_id': q['_id']},
                    {'$set': {'composite_group_id': composite_key}}
                )
                update_count += 1
        
        print(f"✅ Updated {update_count} existing questions with composite group keys")
    except Exception as e:
        print(f"❌ Error updating questions: {e}")

# Improved query function with better error handling
def get_questions_for_units(subject, units, difficulty="easy", examtype="insem"):
    """
    Get questions for specific units with proper grouping
    """
    try:
        # Build query
        query = {
            "subject": subject,
            "unit": {"$in": units},
            "difficulty": difficulty,
            "examtype": examtype
        }
        
        print(f"🔍 Searching with query: {query}")
        
        questions = list(collection.find(query))
        print(f"📊 Found {len(questions)} total questions")
        
        if not questions:
            print("❌ No questions found matching the criteria")
            return {}
        
        # Group by unit and unit_group
        grouped = {}
        current_global_group = 1
        
        # Sort units to ensure consistent ordering
        sorted_units = sorted(units, key=lambda x: int(x.split()[-1]) if x.split()[-1].isdigit() else x)
        
        for unit in sorted_units:
            unit_questions = [q for q in questions if q['unit'] == unit]
            
            if not unit_questions:
                print(f"⚠️  No questions found for {unit}")
                continue
            
            print(f"📋 Processing {len(unit_questions)} questions for {unit}")
            
            # Group by unit_group within this unit
            unit_groups = {}
            for q in unit_questions:
                unit_group = str(q.get('unit_group', '1'))  # Ensure string comparison
                if unit_group not in unit_groups:
                    unit_groups[unit_group] = []
                unit_groups[unit_group].append(q)
            
            # Assign global group IDs
            for unit_group in sorted(unit_groups.keys()):
                grouped[current_global_group] = sorted(
                    unit_groups[unit_group], 
                    key=lambda x: x.get('option_id', 0)
                )
                current_global_group += 1
        
        return grouped
        
    except Exception as e:
        print(f"❌ Error querying questions: {e}")
        return {}

# Debug function to check what's in the database
def debug_database_contents():
    """Print all questions in database for debugging"""
    try:
        all_questions = list(collection.find({}))
        print(f"\n🔍 Database contains {len(all_questions)} total questions")
        
        # Group by unit for overview
        units = {}
        for q in all_questions:
            unit = q.get('unit', 'Unknown')
            if unit not in units:
                units[unit] = []
            units[unit].append(q)
        
        for unit, questions in units.items():
            print(f"\n📚 {unit}: {len(questions)} questions")
            for q in questions:
                print(f"  - Group {q.get('unit_group', 'N/A')}: {q['question'][:60]}...")
                
    except Exception as e:
        print(f"❌ Error debugging database: {e}")

# Test the function
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 STARTING DATABASE OPERATIONS")
    print("=" * 60)
    
    # First, let's see what's in the database
    debug_database_contents()
    
    # Test with Unit 1 and Unit 3
    print("\n" + "=" * 60)
    print("🧪 TESTING QUERY FUNCTION")
    print("=" * 60)
    
    test_grouped = get_questions_for_units("fxe", ["Unit 1", "Unit 3"])
    
    print(f"\n📋 Test Results for Unit 1 and Unit 3:")
    print(f"Found {len(test_grouped)} groups total")
    
    if test_grouped:
        for group_id, questions in test_grouped.items():
            unit = questions[0]['unit']
            unit_group = questions[0].get('unit_group', questions[0].get('group_id'))
            instruction = questions[0]['group_instruction']
            print(f"\n🏷️  Global Group {group_id} ({unit} - Unit Group {unit_group}): {instruction}")
            for i, q in enumerate(questions, 1):
                print(f"  {i}. {q['question'][:70]}... [{q['marks']} marks]")
    else:
        print("❌ No grouped questions returned")
    
    print("\n" + "=" * 60)
    print("✅ questions added .oop")
    print("=" * 60)
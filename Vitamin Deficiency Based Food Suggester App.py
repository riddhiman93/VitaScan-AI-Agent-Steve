from tkinter import *
import tkinter
from transformers import pipeline

#Initialization
root=Tk()
root.geometry("800x600")
root.resizable(0,0)
root.title("VitaScan AI Agent- Steve")

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

vitamins=[
        "Vitamin A - vision and eyes",
        "Vitamin B - energy and muscles",
        "Vitamin C - skin , anemia , scurvy and immunity",
        "Vitamin D - bones and sunlight",
        "Vitamin E - blood and antioxidants",
        "Vitamin K - bleeding and clotting"
    ]

vitamindata={
    "Vitamin A": {
        "sci": "Retinol", "func": "Healthy Vision, Boost Immune System", "def": "Xerophthalmia (Night Blindness)",
        "plant": "Carrots, sweet potatoes, pumpkin, spinach, mangoes.", "animal": "Salmon, sardines, milk, cheese, egg yolks.","vit":"Vitamin A"
    },
    "Vitamin B": {
        "sci": "B-Complex", "func": "DNA Replication and Red Blood Cell Production", "def": "Muscle and Body Weakness.",
        "plant": "Leafy greens, potatoes, broccoli, bananas, beans.", "animal": "Beef, chicken, liver, salmon, eggs, milk.","vit":"Vitamin B"
    },
    "Vitamin C": {
        "sci": "Ascorbic Acid", "func": "Anti-oxidant and Formation of Iron", "def": "Scurvy, Anemia.",
        "plant": "Citrus fruits, strawberries, kiwi, bell peppers, tomatoes.", "animal": "Raw liver, fish roe, and organ meats.","vit":"Vitamin C"
    },
    "Vitamin D": {
        "sci": "Calciferol", "func": "Bone Growth", "def": "Rickets, Osteoporosis.",
        "plant": "UV-exposed mushrooms, fortified soy/almond milk.", "animal": "Oily fish (salmon, sardines), red meat, egg yolks.","vit":"Vitamin D"
    },
    "Vitamin E": {
        "sci": "Tocopherol", "func": "Anti-oxidant and Boost Immune System", "def": "Neuropathy, Anemia.",
        "plant": "Vegetable oils, seeds, nuts, avocados, mangoes.", "animal": "Trout, salmon, egg yolks, butter.","vit":"Vitamin E"
    },
    "Vitamin K": {
        "sci": "Phylloquinone", "func": "Blood Coagulation", "def": "Hemorrhagic Diseases.",
        "plant": "Spinach, lettuce, broccoli, basil, olive oil.", "animal": "Eggs, cheese, liver, chicken, fatty fish.","vit":"Vitamin K"
    }
}

#Functions
def suggestvitamin():
    sym=feel.get()
    if not sym.strip():
        return
    
    for widget in outframe.winfo_children():
        widget.destroy()

    result=classifier(sym, candidate_labels=vitamins)
    fulllabel=result["labels"][0]
    predctn=fulllabel.split("-")[0].strip()
    confidence=result["scores"][0]*100

    data=vitamindata[predctn]
    outlabel=Label(outframe,text="AI Analysis By Steve",fg="blue",bg="yellow",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=30,y=20)
    adrs=Label(outframe,text=f"Hello , I am Steve , I think you have deficiency of {data["vit"]},hope you get well soon!  {"🩺⚕️💪"}",font=('Helvetica', 14),bg="white", fg="red",wraplength=560)
    adrs.place(x=30,y=60)
    sn=Label(outframe,text=f"Scientific Name :{data["sci"]}",font=('Helvetica', 14),bg="yellow", fg="blue",wraplength=560)
    sn.place(x=30,y=130)
    fn=Label(outframe,text=f"Functions :{data["func"]}",font=('Helvetica', 14),bg="yellow", fg="blue",wraplength=560)
    fn.place(x=30,y=160)
    dd=Label(outframe,text=f"Deficiency Disease :{data["def"]}",font=('Helvetica', 14),bg="yellow", fg="blue",wraplength=560)
    dd.place(x=30,y=190)
    pl=Label(outframe,text=f"Plant Sources :{data["plant"]}",font=('Helvetica', 14),bg="yellow", fg="blue",wraplength=560)
    pl.place(x=30,y=220)
    an=Label(outframe,text=f"Animal Sources :{data["animal"]}",font=('Helvetica', 14),bg="yellow", fg="blue",wraplength=560)
    an.place(x=30,y=250)


#Variables
predctn=StringVar()
sym=StringVar()


#Frames
inframe=LabelFrame(root,width=630,height=150,bg="yellow").place(x=75,y=100)
outframe=LabelFrame(root,width=630,height=300,bg="yellow")
outframe.place(x=75,y=300)

#Labels
headinglbl=Label(root,text="VitaScan AI Agent- Steve",fg="red",font=('Helvetica', 22, 'bold'),padx=0,pady=0).place(x=225,y=35)
loclabel=Label(inframe,text="Describe how you feel ?",fg="blue",bg="yellow",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=120,y=120)
feel=Entry(root,width=70,font=('Helvetica', 10, 'bold'))
feel.place(x=120,y=175,height=50)

#Button
aibtn=Button(root,text="Get AI Analysis",font=('Helvetica',12,'bold'),fg="white",command=suggestvitamin,width=26,bg="red",height=2,padx=0,pady=0).place(x=320,y=255,height=40,width=150)

root.mainloop()




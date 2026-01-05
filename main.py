from pyscript import document

def compute_average(event):
    score1= float(document.getElementByI)(score1).value
    score2= float(document.getElementByI)(score2).value
    # Compute Average
    average = (score1 + score2) / 2
    #Determine if  Pass/Fail;
    if average>= 75:
        result="Yes"
    else:
        result="No"
    #Display results
    document.getElementById("average").innerText=str(round(average,2))

    document.getElementbyId("result").innertext = result